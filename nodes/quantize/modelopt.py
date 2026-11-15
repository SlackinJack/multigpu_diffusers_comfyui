from ..data_types import (
    TRILEAN_DEFAULT,
    MODULE_QUANT_CONFIG,
    CATEGORY_QUANTIZE,
    trilean,
)


class ModelOptQuantizationConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "quant_type": (
                    ["INT8", "FP8", "INT4", "NF4", "NVFP4"],
                    {"default": "INT8"},
                ),
                "disable_conv_quantization": TRILEAN_DEFAULT,
                # "algorithm": (["max"], { "default": "max" }),
            }
        }

    RETURN_TYPES = MODULE_QUANT_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_QUANTIZE

    def run(self, **kwargs):
        out = {}
        out["backend"] = out["quant_method"] = "modelopt"
        out["algorithm"] = "max"
        for k, v in kwargs.items():
            if k in ["quant_type", "algorithm"]:
                out[k] = v
            elif k in ["disable_conv_quantization"]:
                if trilean(v) is not None:
                    out[k] = trilean(v)
        return (out,)
