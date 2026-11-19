from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    TORCH_CONFIG,
    BOOLEAN_FALSE,
    CATEGORY_GENERAL,
    OFFLOAD_CONFIG,
    GROUP_OFFLOAD_CONFIG,
    BOOLEAN_TRUE,
    DEEPCACHE_CONFIG,
    COMPILE_CONFIG,
    ATTN_BACKENDS,
    ATTN_BACKEND_CONFIG,
    INT_MAX,
    TRILEAN_DEFAULT,
    STEPS,
    CACHE_DIT_CONFIG,
    trilean,
)


class TorchConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "torch_cache_limit": ("INT", {"default": 16, "min": 0}),
                "torch_accumlated_cache_limit": (
                    "INT",
                    {
                        "default": 128,
                        "min": 0,
                    },
                ),
                "torch_capture_scalar": BOOLEAN_FALSE,
            }
        }

    RETURN_TYPES = TORCH_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_GENERAL

    def run(self, **kwargs):
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"TorchConfig": TorchConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"TorchConfig": "Torch"})


class GroupOffloadConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "transformer": OFFLOAD_CONFIG,
                "encoder": OFFLOAD_CONFIG,
                "vae": OFFLOAD_CONFIG,
                "misc": OFFLOAD_CONFIG,
            }
        }

    RETURN_TYPES = GROUP_OFFLOAD_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_GENERAL

    def run(self, **kwargs):
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"GroupOffloadConfig": GroupOffloadConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"GroupOffloadConfig": "Group Offloading"})


class OffloadConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "offload_device": (
                    "STRING",
                    {
                        "default": "cpu",
                        "multiline": False,
                    },
                ),
                "offload_type": (
                    ["leaf_level", "block_level"],
                    {"default": "leaf_level"},
                ),
                "num_blocks_per_group": (
                    "INT",
                    {
                        "default": 2,
                        "min": 1,
                    },
                ),
                "use_stream": BOOLEAN_FALSE,
            }
        }

    RETURN_TYPES = OFFLOAD_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_GENERAL

    def run(self, **kwargs):
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"OffloadConfig": OffloadConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"OffloadConfig": "Module Offloading"})


class CompileConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "compile_transformer": BOOLEAN_FALSE,
                "compile_vae": BOOLEAN_FALSE,
                "compile_encoder": BOOLEAN_FALSE,
                "compile_backend": (
                    ["default", "inductor", "eager"],
                    {"default": "default"},
                ),
                "compile_mode": (
                    [
                        "default",
                        "reduce-overhead",
                        "max-autotune",
                        "max-autotune-no-cudagraphs",
                    ],
                    {"default": "default"},
                ),
                "compile_options": (
                    "STRING",
                    {"default": "{}", "multiline": True},
                ),
                "dynamic": BOOLEAN_TRUE,
                "fullgraph": BOOLEAN_TRUE,
            }
        }

    RETURN_TYPES = COMPILE_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_GENERAL

    def run(
        self,
        compile_transformer,
        compile_vae,
        compile_encoder,
        compile_backend,
        compile_mode,
        compile_options,
        dynamic,
        fullgraph,
    ):
        out = {}
        if compile_transformer is True:
            out["compile_transformer"] = True
        if compile_vae is True:
            out["compile_vae"] = True
        if compile_encoder is True:
            out["compile_encoder"] = True
        if compile_backend != "default":
            out["compile_backend"] = compile_backend
        if compile_mode != "default":
            out["compile_mode"] = compile_mode
        if len(compile_options) > 0:
            out["compile_options"] = compile_options
        if dynamic is True:
            out["dynamic"] = True
        if fullgraph is True:
            out["fullgraph"] = True
        return (out,)


NODE_CLASS_MAPPINGS.update({"CompileConfig": CompileConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"CompileConfig": "Model Compile"})


class AttentionBackendConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"backend": ATTN_BACKENDS}}

    RETURN_TYPES = ATTN_BACKEND_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_GENERAL

    def run(self, **kwargs):
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"AttentionBackendConfig": AttentionBackendConfig})
NODE_DISPLAY_NAME_MAPPINGS.update(
    {"AttentionBackendConfig": "Attention Backend"}
)


class DeepCacheConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "deep_cache_interval": (
                    "INT",
                    {"default": 3, "min": 0, "max": INT_MAX},
                ),
                "deep_cache_id": (
                    "INT",
                    {"default": 0, "min": 0, "max": INT_MAX},
                ),
            }
        }

    RETURN_TYPES = DEEPCACHE_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_GENERAL

    def run(self, **kwargs):
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"DeepCacheConfig": DeepCacheConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"DeepCacheConfig": "Deep Cache"})


class CacheDiTConfig:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "max_warmup_steps": (
                    "INT",
                    {"default": 8, "min": 0, "max": INT_MAX},
                ),
                "max_cached_steps": (
                    "INT",
                    {"default": -1, "min": -1, "max": INT_MAX},
                ),
                "Fn_compute_blocks": (
                    "INT",
                    {"default": 8, "min": 0, "max": INT_MAX},
                ),
                "Bn_compute_blocks": (
                    "INT",
                    {"default": 8, "min": 0, "max": INT_MAX},
                ),
                "residual_diff_threshold": (
                    "FLOAT",
                    {
                        "default": 0.12000,
                        "min": 0,
                        "max": INT_MAX,
                        "step": 0.00001,
                    },
                ),
                "enable_separate_cfg": TRILEAN_DEFAULT,
                "enable_taylorseer": TRILEAN_DEFAULT,
                "taylorseer_order": (
                    "INT",
                    {"default": 1, "min": 0, "max": INT_MAX},
                ),
                "enable_scm": TRILEAN_DEFAULT,
                "scm_mask_policy": (
                    ["slow", "medium", "fast", "ultra"],
                    {"default": "fast"},
                ),
                "scm_total_steps": STEPS,
                "steps_computation_policy": (
                    ["dynamic", "static", "default"],
                    {"default": "default"},
                ),
            }
        }

    RETURN_TYPES = CACHE_DIT_CONFIG
    FUNCTION = "run"
    CATEGORY = CATEGORY_GENERAL

    def run(self, **kwargs):
        out = {}
        for k, v in kwargs.items():
            if k in ["enable_separate_cfg", "enable_taylorseer", "enable_scm"]:
                if trilean(v) is not None:
                    out[k] = v
            elif k in ["steps_computation_policy"]:
                if v != "default":
                    out[k] = v
            else:
                out[k] = v
        return (out,)


NODE_CLASS_MAPPINGS.update({"CacheDiTConfig": CacheDiTConfig})
NODE_DISPLAY_NAME_MAPPINGS.update({"CacheDiTConfig": "CacheDiT"})
