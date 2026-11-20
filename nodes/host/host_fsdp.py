from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    CACHE_DIT_CONFIG,
    DEEPCACHE_CONFIG,
    BACKEND_CONFIG,
    CATEGORY_HOST,
    BOOLEAN_TRUE,
    BOOLEAN_FALSE,
)

FSDP_CONFIGS = {
    "shard_transformer": BOOLEAN_TRUE,
    "shard_encoder": BOOLEAN_FALSE,
    "shard_vae": BOOLEAN_FALSE,
    "shard_misc": BOOLEAN_FALSE
}


FSDP_CONFIGS_OPTIONAL = {
    "cache_dit_config": CACHE_DIT_CONFIG,
    "deepcache_config": DEEPCACHE_CONFIG,
}


class FSDPConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": FSDP_CONFIGS,
            "optional": FSDP_CONFIGS_OPTIONAL,
        }

    RETURN_TYPES = BACKEND_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        kwargs["backend_name"] = "fsdp"
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"FSDPConfig": FSDPConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"FSDPConfig": "FSDP Backend"})
