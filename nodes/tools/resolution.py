from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    INT_MAX,
    CATEGORY_TOOLS,
)


class ResolutionCalculator:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ratio_x": (
                    "INT",
                    {"default": 9, "max": INT_MAX, "min": 1, "step": 1},
                ),
                "ratio_y": (
                    "INT",
                    {"default": 16, "max": INT_MAX, "min": 1, "step": 1},
                ),
                "shortest": (
                    "INT",
                    {"default": 720, "max": INT_MAX, "min": 8, "step": 8},
                ),
                "div_by_16": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = (
        "INT",
        "INT",
    )
    RETURN_NAMES = (
        "x",
        "y",
    )
    FUNCTION = "run"
    CATEGORY = CATEGORY_TOOLS

    def run(self, ratio_x, ratio_y, shortest, div_by_16):
        divisor = 8 if not div_by_16 else 16
        m = shortest
        if m % divisor != 0:
            while m % divisor != 0:
                m += 1
        if ratio_x == ratio_y:
            return (
                m,
                m,
            )
        elif ratio_x > ratio_y:
            n = round(m / ratio_y * ratio_x)
            while n % divisor != 0:
                n += 1
            return (n, m)
        else:
            n = round(m / ratio_x * ratio_y)
            while n % divisor != 0:
                n += 1
            return (m, n)


NODE_CLASS_MAPPINGS.update({"ResolutionCalculator": ResolutionCalculator})
NODE_DISPLAY_NAME_MAPPINGS.update(
    {"ResolutionCalculator": "Resolution Calculator"}
)
