from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    CACHE_DIT_CONFIG,
    DEEPCACHE_CONFIG,
    BACKEND_CONFIG,
    CATEGORY_HOST,
    BOOLEAN_TRUE,
    BOOLEAN_FALSE,
)

DEEPSPEED_CONFIGS = {
    "wrap_transformer": BOOLEAN_TRUE,
    "wrap_encoder": BOOLEAN_FALSE,
    "wrap_vae": BOOLEAN_FALSE,
    "wrap_misc": BOOLEAN_FALSE
}


DEEPSPEED_CONFIGS_OPTIONAL = {
    "cache_dit_config": CACHE_DIT_CONFIG,
    "deepcache_config": DEEPCACHE_CONFIG,
}


class DeepSpeedConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": DEEPSPEED_CONFIGS,
            "optional": DEEPSPEED_CONFIGS_OPTIONAL,
        }

    RETURN_TYPES = BACKEND_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        kwargs["backend_name"] = "deepspeed"
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"DeepSpeedConfig": DeepSpeedConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"DeepSpeedConfig": "DeepSpeed Backend"})
