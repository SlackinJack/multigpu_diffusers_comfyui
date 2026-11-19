from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    TIMESTEPS,
    SIGMAS,
    CATEGORY_SCHEDULER,
)


class CustomTimesteps:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "timesteps_csv": (
                    "STRING",
                    {"default": "999, 499, 0", "multiline": True},
                )
            }
        }

    RETURN_TYPES = TIMESTEPS
    FUNCTION = "run"
    CATEGORY = CATEGORY_SCHEDULER

    def run(self, timesteps_csv):
        t = timesteps_csv.replace("\n", "").replace(" ", "").split(",")
        t = [float(x) for x in t]
        t = [int(x) for x in t]
        return (t,)


NODE_CLASS_MAPPINGS.update({"CustomTimesteps": CustomTimesteps})
NODE_DISPLAY_NAME_MAPPINGS.update({"CustomTimesteps": "CustomTimesteps"})


class CustomSigmas:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "sigmas_csv": (
                    "STRING",
                    {"default": "14.20, 7.10, 3.55", "multiline": True},
                )
            }
        }

    RETURN_TYPES = SIGMAS
    FUNCTION = "run"
    CATEGORY = CATEGORY_SCHEDULER

    def run(self, sigmas_csv):
        s = sigmas_csv.replace("\n", "").replace(" ", "").split(",")
        s = [float(x) for x in s]
        return (s,)


NODE_CLASS_MAPPINGS.update({"CustomSigmas": CustomSigmas})
NODE_DISPLAY_NAME_MAPPINGS.update({"CustomSigmas": "CustomSigmas"})
