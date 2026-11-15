import torch
from comfy.utils import ProgressBar

from ...multigpu_diffusion.modules.utils import (
    convert_tensor_to_b64,
    decode_b64_and_unpickle,
    convert_image_to_hwc_tensor,
)
from ..data_types import (
    HOST,
    IMAGE,
    PROMPT,
    SEED,
    STEPS,
    CFG,
    CATEGORY_SAMPLER,
)
from ..host.host import get_current_manager

IMAGE_SUCCESS_MESSAGE = "🏁 Successfully created image"
MULTI_SUCCESS_MESSAGE = "🏁 Successfully created frames"
NO_MEDIA_GENERATED = "No media generated.\nCheck console for details."


class SDUpscaleSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "host": HOST,
                "image": IMAGE,
                "positive": PROMPT,
                "seed": SEED,
                "num_inference_steps": STEPS,
                "guidance_scale": CFG,
            },
            "optional": {
                "negative_prompt": PROMPT,
            },
        }

    RETURN_TYPES = HOST + ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = CATEGORY_SAMPLER

    def run(
        self,
        host,
        image,
        positive,
        seed,
        num_inference_steps,
        guidance_scale,
        negative_prompt=None,
    ):
        assert len(positive) > 0, "You must provide a prompt."

        if image.size(0) > 1:
            images = list(torch.unbind(image, 0))  # NHWC -> [HWC], len == N
        else:
            images = [image.squeeze(0)]  # NHWC -> [HWC], len == 1
        tensors = []
        i = 0
        manager = get_current_manager()
        for i, im in enumerate(images):
            manager.log(f"⏳ Upscaling image: {i}/{len(images)}")
            b64_image = convert_tensor_to_b64(im)
            data = {
                "image": b64_image,
                "prompt": positive,
                "seed": seed,
                "num_inference_steps": num_inference_steps,
            }

            if negative_prompt is not None:
                data["negative"] = negative_prompt
            if guidance_scale >= 0.0:
                data["guidance_scale"] = guidance_scale

            try:
                pbar = ProgressBar(100)
                response = manager.get_result(host, data, pbar=pbar)
                if response is not None:
                    manager.log(
                        f"✅ Finished upscaling image: {i}/{len(images)}"
                    )
                    im2 = decode_b64_and_unpickle(response)
                    tensors.append(convert_image_to_hwc_tensor(im2))
                else:
                    if len(images) == 1:
                        manager.log("❌ No media generated")
                    else:
                        manager.log(
                            f"❌ Error processing image: {i}/{len(images)}"
                        )
            except Exception as e:
                manager.log("❌ Error getting data from server.\n" + str(e))
        assert len(tensors) > 0, NO_MEDIA_GENERATED
        manager.log(IMAGE_SUCCESS_MESSAGE)
        return (
            host,
            torch.stack(tuple(tensors)),
        )  # HWC -> NHWC
