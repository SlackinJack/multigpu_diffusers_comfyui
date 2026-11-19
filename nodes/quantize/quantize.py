from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    MODULE_QUANT_CONFIG,
    QUANT_CONFIG,
    CATEGORY_QUANTIZE,
)


class QuantizationConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "transformer": MODULE_QUANT_CONFIG,
                "encoder": MODULE_QUANT_CONFIG,
                "vae": MODULE_QUANT_CONFIG,
                "tokenizer": MODULE_QUANT_CONFIG,
                "misc": MODULE_QUANT_CONFIG,
            }
        }

    RETURN_TYPES = QUANT_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_QUANTIZE

    def run(self, **kwargs):
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"QuantizationConfig": QuantizationConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"QuantizationConfig": "Quantize"})
