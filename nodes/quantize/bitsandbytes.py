from ..data_types import (
    BOOLEAN_FALSE,
    DTYPE,
    MODULE_QUANT_CONFIG,
    CATEGORY_QUANTIZE,
)


class BitsAndBytesQuantizationConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "load_in_8bit": BOOLEAN_FALSE,
                "load_in_4bit": BOOLEAN_FALSE,
                "llm_int8_threshold": ("FLOAT", {"default": 6.0}),
                # "llm_int8_skip_modules":           ("STRING",),
                "llm_int8_enable_fp32_cpu_offload": BOOLEAN_FALSE,
                "llm_int8_has_fp16_weight": BOOLEAN_FALSE,
                "bnb_4bit_compute_dtype": DTYPE,
                "bnb_4bit_quant_type": (["nf4", "fp4"], {"default": "nf4"}),
                "bnb_4bit_use_double_quant": BOOLEAN_FALSE,
                "bnb_4bit_quant_storage": (
                    [
                        "bf16",
                        "fp8",
                        "fp16",
                        "fp32",
                        "int1",
                        "int2",
                        "int3",
                        "int4",
                        "int5",
                        "int6",
                        "int7",
                        "int8",
                        "int16",
                        "int32",
                        "bool",
                    ],
                    {"default": "fp16"},
                ),
            }
        }

    RETURN_TYPES = MODULE_QUANT_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_QUANTIZE

    def run(self, **kwargs):
        kwargs["backend"] = "bitsandbytes"
        return (kwargs,)
