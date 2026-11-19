from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    LORAS,
    LORA_WEIGHT,
    LORA,
    CATEGORY_MODEL,
    get_models_dir,
)


class LoraSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"lora": LORAS, "weight": LORA_WEIGHT}}

    RETURN_TYPES = LORA
    FUNCTION = "run"
    CATEGORY = CATEGORY_MODEL

    def run(self, lora, weight):
        return ({f"{get_models_dir()}/loras/{lora}": weight},)


NODE_CLASS_MAPPINGS.update({"LoraSelector": LoraSelector})
NODE_DISPLAY_NAME_MAPPINGS.update({"LoraSelector": "Lora"})


class MultiLoraJoiner:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"lora{i}": LORA for i in range(16)}}

    RETURN_TYPES = LORA
    FUNCTION = "run"
    CATEGORY = CATEGORY_MODEL

    def run(self, **kwargs):
        return (
            {
                adapter: scale
                for mapping in kwargs.values()
                for adapter, scale in mapping.items()
            },
        )


NODE_CLASS_MAPPINGS.update({"MultiLoraJoiner": MultiLoraJoiner})
NODE_DISPLAY_NAME_MAPPINGS.update({"MultiLoraJoiner": "Lora Joiner"})


class MultiLoraJoinerMini:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"lora{i}": LORA for i in range(4)}}

    RETURN_TYPES = LORA
    FUNCTION = "run"
    CATEGORY = CATEGORY_MODEL

    def run(self, **kwargs):
        return (
            {
                adapter: scale
                for mapping in kwargs.values()
                for adapter, scale in mapping.items()
            },
        )


NODE_CLASS_MAPPINGS.update({"MultiLoraJoinerMini": MultiLoraJoinerMini})
NODE_DISPLAY_NAME_MAPPINGS.update(
    {"MultiLoraJoinerMini": "Lora Joiner (Mini)"}
)


class MultiLoraJoinerLarge:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"lora{i}": LORA for i in range(32)}}

    RETURN_TYPES = LORA
    FUNCTION = "run"
    CATEGORY = CATEGORY_MODEL

    def run(self, **kwargs):
        return (
            {
                adapter: scale
                for mapping in kwargs.values()
                for adapter, scale in mapping.items()
            },
        )


NODE_CLASS_MAPPINGS.update({"MultiLoraJoinerLarge": MultiLoraJoinerLarge})
NODE_DISPLAY_NAME_MAPPINGS.update(
    {"MultiLoraJoinerLarge": "Lora Joiner (Large)"}
)
