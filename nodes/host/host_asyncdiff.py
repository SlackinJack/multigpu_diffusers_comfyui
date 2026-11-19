from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    BOOLEAN_FALSE,
    BACKEND_CONFIG,
    CATEGORY_HOST,
)

ASYNCDIFF_CONFIGS = {
    "model_n": (
        "INT",
        {
            "default": 2,
            "min": 1,
        },
    ),
    "stride": (
        "INT",
        {
            "default": 1,
            "min": 1,
        },
    ),
    "synced_steps": (
        "INT",
        {
            "default": 10,
            "min": 0,
        },
    ),
    "time_shift": (
        "INT",
        {
            "default": 0,
            "min": 0,
        },
    ),
    "shifted_steps": (
        "INT",
        {
            "default": 0,
            "min": 0,
        },
    ),
    "ramped_time_shift": BOOLEAN_FALSE,
}


ASYNCDIFF_CONFIGS_OPTIONAL = {}


class AsyncDiffConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": ASYNCDIFF_CONFIGS,
            "optional": ASYNCDIFF_CONFIGS_OPTIONAL,
        }

    RETURN_TYPES = BACKEND_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"AsyncDiffConfig": AsyncDiffConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"AsyncDiffConfig": "AsyncDiff Backend"})
