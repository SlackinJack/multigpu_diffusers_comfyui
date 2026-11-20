from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS


from threading import Lock


from ..data_types import (
    INT_MAX,
    INT_MIN,
    LIST_STRING,
    LIST_NUMBER,
    DICT,
    CATEGORY_TOOLS,
)


_store = {}
_store_lock = Lock()


class SetVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": "example"}),
                "value": ("*", {"default": ""}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "run"
    CATEGORY = CATEGORY_TOOLS

    def run(self, key, value):
        with _store_lock:
            _store[key] = value
        return


NODE_CLASS_MAPPINGS.update({"SetVariable": SetVariable})
NODE_DISPLAY_NAME_MAPPINGS.update({"SetVariable": "Set Variable"})


class GetVariable:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": "key"}),
            }
        }

    RETURN_TYPES = ("*",)
    FUNCTION = "run"
    CATEGORY = CATEGORY_TOOLS

    def run(self, key):
        with _store_lock:
            value = _store.get(key, "")
        return (value,)


NODE_CLASS_MAPPINGS.update({"GetVariable": GetVariable})
NODE_DISPLAY_NAME_MAPPINGS.update({"GetVariable": "Get Variable"})
