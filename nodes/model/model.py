from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

import os

from ..data_types import (
    CHECKPOINTS,
    DEVICE_MAP,
    CLASS_OVERRIDE,
    MODEL,
    CATEGORY_MODEL,
    get_models_dir,
    MODELS,
    MODEL_CONFIGS,
    UNSAFE_MODELS,
)


class CheckpointSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "checkpoint": CHECKPOINTS,
                "device_map": DEVICE_MAP,
            },
            "optional": {
                "class_override": CLASS_OVERRIDE,
            },
        }

    RETURN_TYPES = MODEL
    FUNCTION = "run"
    CATEGORY = CATEGORY_MODEL

    def run(self, **kwargs):
        kwargs["checkpoint"] = os.path.join(
            get_models_dir(), kwargs["checkpoint"]
        )
        if kwargs["device_map"] == "none":
            del kwargs["device_map"]
        if len(kwargs["class_override"]) == 0:
            del kwargs["class_override"]
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"CheckpointSelector": CheckpointSelector})
NODE_DISPLAY_NAME_MAPPINGS.update({"CheckpointSelector": "Checkpoint"})


class ModelSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": MODELS,
                "config": MODEL_CONFIGS,
                "device_map": DEVICE_MAP,
            },
            "optional": {
                "class_override": CLASS_OVERRIDE,
            },
        }

    RETURN_TYPES = MODEL
    FUNCTION = "run"
    CATEGORY = CATEGORY_MODEL

    def run(self, **kwargs):
        kwargs["model"] = os.path.join(get_models_dir(), kwargs["model"])
        kwargs["config"] = os.path.join(get_models_dir(), kwargs["config"])
        if kwargs["device_map"] == "none":
            del kwargs["device_map"]
        if len(kwargs["class_override"]) == 0:
            del kwargs["class_override"]
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"ModelSelector": ModelSelector})
NODE_DISPLAY_NAME_MAPPINGS.update({"ModelSelector": "Model"})


class UnsafeModelSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": UNSAFE_MODELS,
                "config": MODEL_CONFIGS,
                "device_map": DEVICE_MAP,
            },
            "optional": {
                "class_override": CLASS_OVERRIDE,
            },
        }

    RETURN_TYPES = MODEL
    FUNCTION = "run"
    CATEGORY = CATEGORY_MODEL

    def run(self, **kwargs):
        kwargs["model"] = os.path.join(get_models_dir(), kwargs["model"])
        kwargs["config"] = os.path.join(get_models_dir(), kwargs["config"])
        if kwargs["device_map"] == "none":
            del kwargs["device_map"]
        if len(kwargs["class_override"]) == 0:
            del kwargs["class_override"]
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"UnsafeModelSelector": UnsafeModelSelector})
NODE_DISPLAY_NAME_MAPPINGS.update({"UnsafeModelSelector": "Model (Unsafe)"})
