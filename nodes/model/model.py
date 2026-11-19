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
    CHECKPOINT,
    MODEL_TARGETS,
)


class ModelJoiner:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"model{i}": MODEL for i in range(16)}}

    RETURN_TYPES = MODEL
    FUNCTION = "run"
    CATEGORY = CATEGORY_MODEL

    def run(self, **kwargs):
        return ({k: v for mapping in kwargs.values() for k, v in mapping.items()},)


NODE_CLASS_MAPPINGS.update({"ModelJoiner": ModelJoiner})
NODE_DISPLAY_NAME_MAPPINGS.update({"ModelJoiner": "Model Joiner"})


class CheckpointSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "checkpoint_path": CHECKPOINTS,
                "device_map": DEVICE_MAP,
            },
            "optional": {
                "class_override": CLASS_OVERRIDE,
            },
        }

    RETURN_TYPES = CHECKPOINT
    FUNCTION = "run"
    CATEGORY = CATEGORY_MODEL

    def run(self, **kwargs):
        kwargs["checkpoint_path"] = os.path.join(get_models_dir(), kwargs["checkpoint_path"])
        if kwargs["device_map"] == "none":
            del kwargs["device_map"]
        if len(kwargs["class_override"]) == 0:
            del kwargs["class_override"]
        return (kwargs,)


NODE_CLASS_MAPPINGS.update({"CheckpointSelector": CheckpointSelector})
NODE_DISPLAY_NAME_MAPPINGS.update({"CheckpointSelector": "Checkpoint"})


class ModelCheckpointSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "checkpoint_path": CHECKPOINTS,
                "target": MODEL_TARGETS,
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
        kwargs["checkpoint_path"] = os.path.join(get_models_dir(), kwargs["checkpoint_path"])
        if kwargs["device_map"] == "none":
            del kwargs["device_map"]
        if len(kwargs["class_override"]) == 0:
            del kwargs["class_override"]
        return ({kwargs.pop("target"): kwargs},)


NODE_CLASS_MAPPINGS.update({"ModelCheckpointSelector": ModelCheckpointSelector})
NODE_DISPLAY_NAME_MAPPINGS.update({"ModelCheckpointSelector": "Model Checkpoint"})


class ModelSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_path": MODELS,
                "config_path": MODEL_CONFIGS,
                "target": MODEL_TARGETS,
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
        kwargs["model_path"] = os.path.join(get_models_dir(), kwargs["model_path"])
        kwargs["config_path"] = os.path.join(get_models_dir(), kwargs["config_path"])
        if kwargs["device_map"] == "none":
            del kwargs["device_map"]
        if len(kwargs["class_override"]) == 0:
            del kwargs["class_override"]
        return ({kwargs.pop("target"): kwargs},)


NODE_CLASS_MAPPINGS.update({"ModelSelector": ModelSelector})
NODE_DISPLAY_NAME_MAPPINGS.update({"ModelSelector": "Model"})


class UnsafeModelSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model_path": UNSAFE_MODELS,
                "config_path": MODEL_CONFIGS,
                "target": MODEL_TARGETS,
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
        kwargs["model_path"] = os.path.join(get_models_dir(), kwargs["model_path"])
        kwargs["config_path"] = os.path.join(get_models_dir(), kwargs["config_path"])
        if kwargs["device_map"] == "none":
            del kwargs["device_map"]
        if len(kwargs["class_override"]) == 0:
            del kwargs["class_override"]
        return ({kwargs.pop("target"): kwargs},)


NODE_CLASS_MAPPINGS.update({"UnsafeModelSelector": UnsafeModelSelector})
NODE_DISPLAY_NAME_MAPPINGS.update({"UnsafeModelSelector": "Model (Unsafe)"})
