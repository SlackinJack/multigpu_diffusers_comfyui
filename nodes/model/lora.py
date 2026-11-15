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
