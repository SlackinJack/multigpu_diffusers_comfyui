from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    MODULE_QUANT_CONFIG,
    CATEGORY_QUANTIZE,
)


class QuantoQuantizationConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "quant_type": (
                    ["float8", "int2", "int4", "int8"],
                    {"default": "int8"},
                ),
            }
        }

    RETURN_TYPES = MODULE_QUANT_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_QUANTIZE

    def run(self, **kwargs):
        kwargs["backend"] = "quanto"
        return (kwargs,)


NODE_CLASS_MAPPINGS.update(
    {"QuantoQuantizationConfig": QuantoQuantizationConfig}
)
NODE_DISPLAY_NAME_MAPPINGS.update(
    {"QuantoQuantizationConfig": "Quanto Quantize"}
)
