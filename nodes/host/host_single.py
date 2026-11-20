from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    CACHE_DIT_CONFIG,
    DEEPCACHE_CONFIG,
    BACKEND_CONFIG,
    CATEGORY_HOST,
)

SINGLE_CONFIGS = {}


SINGLE_CONFIGS_OPTIONAL = {
    "cache_dit_config": CACHE_DIT_CONFIG,
    "deepcache_config": DEEPCACHE_CONFIG,
}


class SingleConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": SINGLE_CONFIGS,
            "optional": SINGLE_CONFIGS_OPTIONAL,
        }

    RETURN_TYPES = BACKEND_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        kwargs["backend_name"] = "single"
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"SingleConfig": SingleConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"SingleConfig": "Single Backend"})
