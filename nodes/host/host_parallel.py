from ..data_types import (
    BOOLEAN_TRUE,
    BOOLEAN_FALSE,
    CACHE_DIT_CONFIG,
    DEEPCACHE_CONFIG,
    BACKEND_CONFIG,
    CATEGORY_HOST,
)

PARALLEL_CONFIGS = {
    "context_parallel": BOOLEAN_TRUE,
    "tensor_parallel": BOOLEAN_FALSE,
    "tensor_parallel_encoders": BOOLEAN_FALSE,
    "ulysses_degree": (
        "INT",
        {
            "default": 2,
            "min": 1,
        },
    ),
    "ring_degree": (
        "INT",
        {
            "default": 1,
            "min": 1,
        },
    ),
    "ulysses_anything": BOOLEAN_FALSE,
    "ring_anything": BOOLEAN_FALSE,
    "tp_degree": (
        "INT",
        {
            "default": 1,
            "min": 1,
        },
    ),
}


PARALLEL_CONFIGS_OPTIONAL = {
    "cache_dit_config": CACHE_DIT_CONFIG,
    "deepcache_config": DEEPCACHE_CONFIG,
}


class ParallelConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": PARALLEL_CONFIGS,
            "optional": PARALLEL_CONFIGS_OPTIONAL,
        }

    RETURN_TYPES = BACKEND_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        return (kwargs,)
