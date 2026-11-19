from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

import json


from ..data_types import (
    INT_MAX,
    INT_MIN,
    LIST_STRING,
    LIST_NUMBER,
    DICT,
    CATEGORY_TOOLS,
)


class StringToListString:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"default": "", "multiline": True}),
                "delimiter": ("STRING", {"default": ",", "multiline": False}),
            },
        }

    RETURN_TYPES = LIST_STRING
    FUNCTION = "run"
    CATEGORY = CATEGORY_TOOLS

    def run(self, string, delimiter):
        return (string.split(delimiter),)


NODE_CLASS_MAPPINGS.update({"StringToListString": StringToListString})
NODE_DISPLAY_NAME_MAPPINGS.update(
    {"StringToListString": "String to List<String>"}
)


class StringToListNumber:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"default": "", "multiline": True}),
                "delimiter": ("STRING", {"default": ",", "multiline": False}),
                "number_type": (["int", "float"], {"default": "int"}),
            },
        }

    RETURN_TYPES = LIST_NUMBER
    FUNCTION = "run"
    CATEGORY = CATEGORY_TOOLS

    def run(self, string, delimiter, number_type):
        out = []
        for s in string.split(delimiter):
            match number_type:
                case "int":
                    out.append(int(s))
                case "float":
                    out.append(float(s))
        return (out,)


NODE_CLASS_MAPPINGS.update({"StringToListNumber": StringToListNumber})
NODE_DISPLAY_NAME_MAPPINGS.update(
    {"StringToListNumber": "String to List<Number>"}
)


class StringToDict:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"default": "{}", "multiline": True}),
            }
        }

    RETURN_TYPES = DICT
    FUNCTION = "run"
    CATEGORY = CATEGORY_TOOLS

    def run(self, string):
        return (json.loads(string),)


NODE_CLASS_MAPPINGS.update({"StringToDict": StringToDict})
NODE_DISPLAY_NAME_MAPPINGS.update({"StringToDict": "String to Dict"})


class StringToInteger:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"s": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("INT",)
    FUNCTION = "to_int"
    CATEGORY = CATEGORY_TOOLS

    def to_int(self, s):
        return (int(s),)


NODE_CLASS_MAPPINGS.update({"StringToInteger": StringToInteger})
NODE_DISPLAY_NAME_MAPPINGS.update({"StringToInteger": "String to Integer"})


class FloatToInteger:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "f": (
                    "FLOAT",
                    {
                        "default": 0.00000,
                        "max": INT_MAX,
                        "min": INT_MIN,
                        "step": 0.00001,
                    },
                )
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "to_int"
    CATEGORY = CATEGORY_TOOLS

    def to_int(self, f):
        return (int(f),)


NODE_CLASS_MAPPINGS.update({"FloatToInteger": FloatToInteger})
NODE_DISPLAY_NAME_MAPPINGS.update({"FloatToInteger": "Float to Integer"})


class StringToFloat:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"s": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "to_float"
    CATEGORY = CATEGORY_TOOLS

    def to_float(self, s):
        return (float(s),)


NODE_CLASS_MAPPINGS.update({"StringToFloat": StringToFloat})
NODE_DISPLAY_NAME_MAPPINGS.update({"StringToFloat": "String to Float"})


class IntegerToFloat:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "i": (
                    "INT",
                    {"default": 0, "max": INT_MAX, "min": INT_MIN, "step": 1},
                )
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "to_float"
    CATEGORY = CATEGORY_TOOLS

    def to_float(self, i):
        return (float(i),)


NODE_CLASS_MAPPINGS.update({"IntegerToFloat": IntegerToFloat})
NODE_DISPLAY_NAME_MAPPINGS.update({"IntegerToFloat": "Integer to Float"})


class FloatToString:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "f": (
                    "FLOAT",
                    {
                        "default": 0.00000,
                        "max": INT_MAX,
                        "min": INT_MIN,
                        "step": 0.00001,
                    },
                )
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "to_string"
    CATEGORY = CATEGORY_TOOLS

    def to_string(self, f):
        return (str(f),)


NODE_CLASS_MAPPINGS.update({"FloatToString": FloatToString})
NODE_DISPLAY_NAME_MAPPINGS.update({"FloatToString": "Float to String"})


class IntegerToString:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "i": (
                    "INT",
                    {"default": 0, "max": INT_MAX, "min": INT_MIN, "step": 1},
                )
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "to_string"
    CATEGORY = CATEGORY_TOOLS

    def to_string(self, i):
        return (str(i),)


NODE_CLASS_MAPPINGS.update({"IntegerToString": IntegerToString})
NODE_DISPLAY_NAME_MAPPINGS.update({"IntegerToString": "Integer to String"})
