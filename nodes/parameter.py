from .data_types import (
    PARAM,
    CATEGORY_PARAMETER,
    BOOLEAN_FALSE,
)


class Parameter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key": ("STRING", {"default": "", "multiline": False}),
                "value": ("*",),
            },
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_PARAMETER

    def run(self, key, value):
        return ({key: value},)


class BooleanParameter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key": ("STRING", {"default": "", "multiline": False}),
                "value": BOOLEAN_FALSE,
            },
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_PARAMETER

    def run(self, key, value):
        return ({key: value},)


class StringParameter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key": ("STRING", {"default": "", "multiline": False}),
                "value": ("STRING", {"default": "", "multiline": True}),
            },
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_PARAMETER

    def run(self, key, value):
        return ({key: value},)


class NumberParameter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key": ("STRING", {"default": "", "multiline": False}),
                "value": ("FLOAT", {"default": 0.00000, "step": 0.00001}),
                "number_type": (["int", "float"], {"default": "int"}),
            },
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_PARAMETER

    def run(self, key, value, number_type):
        match number_type:
            case "int":
                return ({key: int(value)},)
            case "float":
                return ({key: float(value)},)


class ParameterJoinerMini:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"param{i}": PARAM for i in range(4)}}

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_PARAMETER

    def run(self, **kwargs):
        return (
            {k: v for mapping in kwargs.values() for k, v in mapping.items()},
        )


class ParameterJoiner:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"param{i}": PARAM for i in range(16)}}

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_PARAMETER

    def run(self, **kwargs):
        return (
            {k: v for mapping in kwargs.values() for k, v in mapping.items()},
        )


class ParameterJoinerLarge:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"param{i}": PARAM for i in range(32)}}

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_PARAMETER

    def run(self, **kwargs):
        return (
            {k: v for mapping in kwargs.values() for k, v in mapping.items()},
        )
