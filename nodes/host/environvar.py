from ..data_types import ENVIRON_VAR, CATEGORY_HOST


class EnvironVar:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "key": (
                    "STRING",
                    {
                        "default": "key",
                        "multiline": False,
                    },
                ),
                "value": (
                    "STRING",
                    {
                        "default": "value",
                        "multiline": False,
                    },
                ),
            }
        }

    RETURN_TYPES = ENVIRON_VAR
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, key, value):
        return ({key: value},)


class EnvironVarJoinerMini:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"env{i}": ENVIRON_VAR for i in range(4)}}

    RETURN_TYPES = ENVIRON_VAR
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        return (
            {k: v for mapping in kwargs.values() for k, v in mapping.items()},
        )


class EnvironVarJoiner:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"env{i}": ENVIRON_VAR for i in range(16)}}

    RETURN_TYPES = ENVIRON_VAR
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        return (
            {k: v for mapping in kwargs.values() for k, v in mapping.items()},
        )


class EnvironVarJoinerLarge:
    @classmethod
    def INPUT_TYPES(s):
        return {"optional": {f"env{i}": ENVIRON_VAR for i in range(32)}}

    RETURN_TYPES = ENVIRON_VAR
    FUNCTION = "run"
    CATEGORY = CATEGORY_HOST

    def run(self, **kwargs):
        return (
            {k: v for mapping in kwargs.values() for k, v in mapping.items()},
        )
