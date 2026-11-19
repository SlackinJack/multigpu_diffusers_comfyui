import json
import os
import torch
from PIL import Image


from ..modules.model_finder import (
    getModelSubfoldersInFolder,
    getModelFilesInFolder,
    getModelFilesInFolderUnsafe,
    getModelConfigsInFolder,
)

from ..multigpu_diffusers.modules.utils import (
    pickle_and_encode_b64,
    convert_tensor_to_b64,
)


cwd = os.path.dirname(__file__)
comfy_root = os.path.dirname(os.path.dirname(os.path.dirname(cwd)))
node_dir = os.path.join(
    os.path.join(comfy_root, "custom_nodes"), "multigpu_diffusers_comfyui"
)
outputs_dir = os.path.join(comfy_root, "output")
comfy_models_dir = os.path.join(os.path.join(comfy_root, "models"))
checkpoints = getModelSubfoldersInFolder(comfy_models_dir, ["loras"])
models = getModelFilesInFolder(comfy_models_dir, ["loras"])
models_unsafe = getModelFilesInFolderUnsafe(comfy_models_dir, ["loras"])
model_configs = getModelConfigsInFolder(comfy_models_dir, ["loras"])
loras = getModelFilesInFolder(os.path.join(comfy_models_dir, "loras"))


INT_MAX = 2**32 - 1
INT_MIN = -1 * INT_MAX
BOOLEAN_TRUE = ("BOOLEAN", {"default": True})
BOOLEAN_FALSE = ("BOOLEAN", {"default": False})
TRILEAN_DEFAULT = (["true", "false", "default"], {"default": "default"})
CONDITIONING = ("CONDITIONING",)
IMAGE = ("IMAGE",)
LATENT = ("LATENT",)
DTYPE = (["bf16", "fp16", "fp32"], {"default": "fp16"})
ATTN_BACKENDS = (
    [
        "native",
        "flex",
        "_native_cudnn",
        "_native_efficient",
        "_native_flash",
        "_native_math",
        "_native_npu",
        "_native_xla",
        "flash",
        "flash_hub",
        "flash_varlen",
        "flash_varlen_hub",
        "aiter",
        "flash_4_hub",
        "_flash_3",
        "_flash_varlen_3",
        "_flash_3_hub",
        "_flash_3_varlen_hub",
        "sage",
        "sage_hub",
        "sage_varlen",
        "_sage_qk_int8_pv_fp8_cuda",
        "_sage_qk_int8_pv_fp8_cuda_sm90",
        "_sage_qk_int8_pv_fp16_cuda",
        "_sage_qk_int8_pv_fp16_triton",
        "xformers",
    ],
    {"default": "native"},
)


CHECKPOINT = ("_CHECKPOINT",)
CHECKPOINTS = (checkpoints,)
MODEL = ("_MODEL",)
MODELS = (models,)
UNSAFE_MODELS = (models_unsafe,)
MODEL_CONFIG = ("_MODEL_CONFIG",)
MODEL_CONFIGS = (model_configs,)
LORA = ("_LORA",)
LORAS = (loras,)
LORA_WEIGHT = (
    "FLOAT",
    {"default": 1.00000, "min": INT_MIN, "max": INT_MAX, "step": 0.00001},
)
DEVICE_MAP = (
    [
        "none",
        "auto",
        "balanced",
        "balanced_low_0",
        "sequential",
        "tp_plan_auto",
    ],
    {"default": "none"},
)


HOST = ("_HOST",)
HOST_CONFIG = ("_HOST_CONFIG",)
BACKEND = (["asyncdiff", "parallel", "single"], {"default": "parallel"})
BACKEND_CONFIG = ("_BACKEND_CONFIG",)
PORT = ("INT", {"default": 6000, "min": 1025, "max": 65535})
MASTER_PORT = ("INT", {"default": 29400, "min": 1025, "max": 65535})
# TIMEOUT = ("INT", {"default": 600, "min": 0, "max": INT_MAX})
LOGGING_LEVEL = (["basic", "info", "all"], {"default": "basic"})
CLASS_OVERRIDE = ("STRING", {"default": "", "multiline": False})


SCHEDULER = ("_SCHEDULER",)
SCHEDULER_CONFIG = ("_SCHEDULER_CONFIG",)
QUANT_CONFIG = ("_QUANTIZE",)
MODULE_QUANT_CONFIG = ("_MODULE_QUANTIZE",)
TORCH_CONFIG = ("_TORCH",)
GROUP_OFFLOAD_CONFIG = ("_GROUP_OFFLOAD",)
OFFLOAD_CONFIG = ("_OFFLOAD",)
COMPILE_CONFIG = ("_COMPILE",)
ATTN_BACKEND_CONFIG = ("_ATTN_BACKEND",)
ENVIRON_VAR = ("_ENVIRON_VAR",)
TIMESTEPS = ("_TIMESTEPS",)
SIGMAS = ("_SIGMAS",)
DEEPCACHE_CONFIG = ("_DEEPCACHE",)
CACHE_DIT_CONFIG = ("_CACHE_DIT",)


PROMPT = ("STRING", {"default": "", "multiline": True})
RESOLUTION = ("INT", {"default": 512, "min": 8, "max": INT_MAX, "step": 8})
SEED = ("INT", {"default": 0, "min": 0, "max": INT_MAX})
STEPS = ("INT", {"default": 60, "min": 1, "max": INT_MAX})
CLIP_SKIP = ("INT", {"default": 0, "min": 0, "max": INT_MAX})
DENOISING_START_STEP = ("INT", {"default": 0, "min": 0, "max": INT_MAX})
DENOISING_END_STEP = ("INT", {"default": INT_MAX, "min": 1, "max": INT_MAX})
CFG = (
    "FLOAT",
    {"default": 7.00000, "min": -1, "max": INT_MAX, "step": 0.00001},
)
CONTROLNET_SCALE = (
    "FLOAT",
    {"default": 0.50000, "min": 0.00000, "max": INT_MAX, "step": 0.00001},
)
NUM_FRAMES = ("INT", {"default": 25, "min": 1, "max": INT_MAX})


# Schedulers
NUM_TRAIN_TIMESTEPS = (
    "INT",
    {"default": 1000, "min": INT_MIN, "max": INT_MAX},
)
STEPS_OFFSET = ("INT", {"default": 0, "min": INT_MIN, "max": INT_MAX})


PARAM = ("_PARAM",)


CATEGORY = "MultiGPU (Diffusers)"
CATEGORY_HOST = f"{CATEGORY}/Host"
CATEGORY_MODEL = f"{CATEGORY}/Model"
CATEGORY_QUANTIZE = f"{CATEGORY}/Quantize"
CATEGORY_SAMPLER = f"{CATEGORY}/Sampler"
CATEGORY_SCHEDULER = f"{CATEGORY}/Scheduler"
CATEGORY_TOOLS = f"{CATEGORY}/Tools"
CATEGORY_GENERAL = f"{CATEGORY}/General"
CATEGORY_PARAMETER = f"{CATEGORY}/Parameter"


# tools:
LIST_STRING = ("LIST_STRING",)
LIST_NUMBER = ("LIST_NUMBER",)
DICT = ("DICT",)


def trilean(value):
    value = value.lower()
    if value == "true":
        return True
    if value == "false":
        return False
    return None


def get_root_dir():
    return comfy_root


def get_node_dir():
    return node_dir


def get_models_dir():
    return comfy_models_dir


def handle_parameter(key, value):
    if key in ["latent", "latents"]:
        return (key, pickle_and_encode_b64(value["samples"]))
    elif key in ["image", "images", "control_image", "ip_image"]:
        return (key, convert_tensor_to_b64(value.squeeze(0)))
    elif isinstance(value, dict) and value.get("scheduler") is not None:
        return ("scheduler", json.dumps(value))
    elif (
        key
        in [
            "prompt_embeds",
            "negative_prompt_embeds",
            "pooled_prompt_embeds",
            "negative_pooled_prompt_embeds",
        ]
        or torch.is_tensor(value)
        or isinstance(value, Image.Image)
    ):
        return (key, pickle_and_encode_b64(value))
    else:
        return (key, value)
