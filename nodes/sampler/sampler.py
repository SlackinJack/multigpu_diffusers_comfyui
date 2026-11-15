import torch
from comfy.utils import ProgressBar

from ...multigpu_diffusion.modules.utils import (
    convert_b64_to_nhwc_tensor,
    decode_b64_and_unpickle,
    convert_image_to_hwc_tensor,
)

from ..data_types import (
    HOST,
    RESOLUTION,
    STEPS,
    SEED,
    PROMPT,
    PARAM,
    CATEGORY_SAMPLER,
    handle_parameter,
)
from ..host.host import get_current_manager

IMAGE_SUCCESS_MESSAGE = "🏁 Successfully created image"
MULTI_SUCCESS_MESSAGE = "🏁 Successfully created frames"
NO_MEDIA_GENERATED = "No media generated.\nCheck console for details."


class DiffusersSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "host": HOST,
                "width": RESOLUTION,
                "height": RESOLUTION,
                "num_inference_steps": STEPS,
                "seed": SEED,
                "prompt": PROMPT,
            },
            "optional": {
                "call_kwargs": PARAM,
            },
        }

    RETURN_TYPES = HOST + (
        "IMAGE",
        "LATENT",
    )
    FUNCTION = "run"
    CATEGORY = CATEGORY_SAMPLER

    def run(
        self,
        host,
        width,
        height,
        num_inference_steps,
        seed,
        prompt,
        call_kwargs=None,
    ):
        data = {
            "width": width,
            "height": height,
            "num_inference_steps": num_inference_steps,
            "seed": seed,
            "prompt": prompt,
        }
        if call_kwargs is not None:
            for k, v in call_kwargs.items():
                key, value = handle_parameter(k, v)
                data[key] = value

        pbar = ProgressBar(100)
        response = get_current_manager().get_result(host, data, pbar=pbar)
        assert response is not None, NO_MEDIA_GENERATED
        image_out, latent_out = response
        get_current_manager().log(IMAGE_SUCCESS_MESSAGE)
        return (
            host,
            convert_b64_to_nhwc_tensor(image_out),
            {"samples": decode_b64_and_unpickle(latent_out)},
        )


class DiffusersSamplerVideo:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "host": HOST,
                "width": RESOLUTION,
                "height": RESOLUTION,
                "num_inference_steps": STEPS,
                "seed": SEED,
                "prompt": PROMPT,
            },
            "optional": {
                "call_kwargs": PARAM,
            },
        }

    RETURN_TYPES = HOST + (
        "IMAGE",
        "LATENT",
    )
    FUNCTION = "run"
    CATEGORY = CATEGORY_SAMPLER

    def run(
        host,
        width,
        height,
        num_inference_steps,
        seed,
        prompt,
        call_kwargs=None,
    ):
        data = {
            "width": width,
            "height": height,
            "num_inference_steps": num_inference_steps,
            "seed": seed,
            "prompt": prompt,
        }
        if call_kwargs is not None:
            for k, v in call_kwargs.items():
                key, value = handle_parameter(k, v)
                data[key] = value

        pbar = ProgressBar(100)
        response = get_current_manager().get_result(host, data, pbar=pbar)
        assert response is not None, NO_MEDIA_GENERATED
        images = decode_b64_and_unpickle(response)
        tensors = []
        for i in images:
            tensors.append(convert_image_to_hwc_tensor(i))
        get_current_manager().log(MULTI_SUCCESS_MESSAGE)
        return (
            host,
            torch.stack(tuple(tensors)),
        )  # HWC -> NHWC
