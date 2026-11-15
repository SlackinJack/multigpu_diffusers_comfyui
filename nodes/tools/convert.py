import json


from ..data_types import (
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
