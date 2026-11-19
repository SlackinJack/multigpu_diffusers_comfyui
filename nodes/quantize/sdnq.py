from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    TRILEAN_DEFAULT,
    INT_MIN,
    INT_MAX,
    MODULE_QUANT_CONFIG,
    CATEGORY_QUANTIZE,
    trilean,
)


# https://github.com/vladmandic/sdnext/wiki/SDNQ-Quantization
class SDNQQuantizationConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "weights_dtype": (
                    [
                        "int16",
                        "int8",
                        "int7",
                        "int6",
                        "int5",
                        "int4",
                        "int3",
                        "int2",
                        "uint16",
                        "uint8",
                        "uint7",
                        "uint6",
                        "uint5",
                        "uint4",
                        "uint3",
                        "uint2",
                        "uint1",
                        "float16",
                        "float8_em4m3fn",
                        "float7_em3m3fn",
                        "float6_em3m2fn",
                        "float5_em2m2fn",
                        "float4_em2m1fn",
                        "float3_em1m1fn",
                        "float2_em1m0fn",
                        "float1_em1m0fnu",
                    ],
                    {"default": "int8"},
                ),
                "quantized_matmul_dtype": (
                    ["default", "uint8", "fp8", "int8", "fp16"],
                    {"default": "default"},
                ),
                "group_size": (
                    ["auto", "row-wise", "tensor-wise"],
                    {"default": "auto"},
                ),
                "use_svd": TRILEAN_DEFAULT,
                "svd_rank": (
                    "INT",
                    {"default": 32, "min": INT_MIN, "max": INT_MAX},
                ),
                "svd_steps": (
                    "INT",
                    {"default": 8, "min": INT_MIN, "max": INT_MAX},
                ),
                "quant_conv": TRILEAN_DEFAULT,
                "quant_embedding": TRILEAN_DEFAULT,
                "use_quantized_matmul": TRILEAN_DEFAULT,
                "use_quantized_matmul_conv": TRILEAN_DEFAULT,
                "dequantize_fp32": TRILEAN_DEFAULT,
                "non_blocking": TRILEAN_DEFAULT,
                "use_dynamic_quantization": TRILEAN_DEFAULT,
                "dynamic_loss_threshold": (
                    "FLOAT",
                    {"default": 0.01000, "step": 0.00001},
                ),
                "use_stochastic_rounding": TRILEAN_DEFAULT,
                "add_skip_keys": TRILEAN_DEFAULT,
                "quantization_device": (
                    "STRING",
                    {"default": "cuda", "multiline": False},
                ),
                "return_device": (
                    "STRING",
                    {"default": "cuda", "multiline": False},
                ),
            }
        }

    RETURN_TYPES = MODULE_QUANT_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_QUANTIZE

    def run(self, **kwargs):
        out = {}
        out["backend"] = "sdnq"
        for k, v in kwargs.items():
            if k in [
                "use_svd",
                "quant_conv",
                "quant_embedding",
                "use_quantized_matmul",
                "use_quantized_matmul_conv",
                "dequantize_fp32",
                "non_blocking",
                "use_dynamic_quantization",
                "use_stochastic_rounding",
                "add_skip_keys",
            ]:
                if trilean(v) is not None:
                    out[k] = trilean(v)
            elif k in ["quantized_matmul_dtype"]:
                if v != "default":
                    out[k] = v
            elif k == "group_size":
                match v:
                    case "row-wise":
                        out[k] = -1
                    case "tensor-wise":
                        out[k] = -2
                    case _:
                        out[k] = 0
            else:
                out[k] = v
        return (out,)


NODE_CLASS_MAPPINGS.update({"SDNQQuantizationConfig": SDNQQuantizationConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"SDNQQuantizationConfig": "SDNQ Quantize"})
