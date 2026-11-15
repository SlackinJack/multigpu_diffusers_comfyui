from comfy.utils import ProgressBar

from ...modules.host_manager import HostManager
from ..data_types import (
    PORT,
    MASTER_PORT,
    BACKEND,
    SEED,
    ENVIRON_VAR,
    HOST,
    CATEGORY_HOST,
    BACKEND_CONFIG,
    QUANT_CONFIG,
    DTYPE,
    MODEL,
    BOOLEAN_FALSE,
    LOGGING_LEVEL,
    LORA,
    COMPILE_CONFIG,
    TORCH_CONFIG,
    GROUP_OFFLOAD_CONFIG,
    ATTN_BACKEND_CONFIG,
    INT_MAX,
)


hm = HostManager()


def get_current_manager():
    return hm


class CreateHost:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "port": PORT,
                "master_port": MASTER_PORT,
                "backend": BACKEND,
                "cuda_visible_devices": (
                    "STRING",
                    {
                        "default": "",
                        "multiline": False,
                    },
                ),
                "s33d": SEED,
            },
            "optional": {
                "environ_vars": ENVIRON_VAR,
            },
        }

    RETURN_TYPES = HOST
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        kwargs.pop("s33d")
        kwargs["cuda_visible_devices"] = kwargs[
            "cuda_visible_devices"
        ].replace(" ", "")
        pbar = ProgressBar(100)
        host = hm.launch_host(kwargs, pbar=pbar)
        return (host,)


class CloseHost:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "host": HOST,
                "obj": ("*",),
            }
        }

    RETURN_TYPES = ("*",)
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, host, obj):
        hm.close_host_process(host, "Closed by node")
        return (obj,)


class ApplyPipeline:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "host": HOST,
                "backend": BACKEND_CONFIG,
                "torch_dtype": DTYPE,
                "checkpoint": MODEL,
                "vae_fp16": BOOLEAN_FALSE,
                "enable_vae_tiling": BOOLEAN_FALSE,
                "enable_vae_slicing": BOOLEAN_FALSE,
                "enable_attention_slicing": BOOLEAN_FALSE,
                "xformers_efficient": BOOLEAN_FALSE,
                "sd_fuse_qkv_projections": BOOLEAN_FALSE,
                "logging_level": LOGGING_LEVEL,
            },
            "optional": {
                "lora": LORA,
                "transformer": MODEL,
                "vae": MODEL,
                "control_net": MODEL,
                "text_encoder": MODEL,
                "text_encoder_2": MODEL,
                "text_encoder_3": MODEL,
                "compile": COMPILE_CONFIG,
                "quantize": QUANT_CONFIG,
                "torch": TORCH_CONFIG,
                "group_offload": GROUP_OFFLOAD_CONFIG,
                "attn_backend": ATTN_BACKEND_CONFIG,
            },
        }

    RETURN_TYPES = HOST
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        host = kwargs.pop("host")
        pbar = ProgressBar(100)
        response = hm.post_to_address(host, "apply", kwargs, pbar=pbar)
        if response is None or response.status_code != 200:
            hm.close_host_process(
                host,
                "Failed to initialize pipeline",
                with_assert="""Failed to initialize pipeline.

Check console for details.""",
            )
        return (host,)


class SleepHost:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "host": HOST,
                "time": (
                    "INT",
                    {
                        "min": 0,
                        "max": INT_MAX,
                        "step": 1,
                    },
                ),
                "obj": ("*",),
            }
        }

    RETURN_TYPES = HOST + ("*",)
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, host, time, obj):
        pbar = ProgressBar(100)
        data = {"sleep": True, "time": time}
        response = hm.post_to_address(host, "sleep", data, pbar=pbar)
        # TODO: maybe do something with response
        return (
            host,
            obj,
        )


class OffloadPipeline:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "host": HOST,
                "obj": ("*",),
            }
        }

    RETURN_TYPES = HOST + ("*",)
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, host, obj):
        pbar = ProgressBar(100)
        response = hm.get_from_address(host, "offload", pbar=pbar)
        # TODO: maybe do something with response
        return (
            host,
            obj,
        )
