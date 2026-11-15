from ..data_types import (
    NUM_TRAIN_TIMESTEPS,
    PARAM,
    CATEGORY_SCHEDULER,
)


class FlowMatchHeunDiscreteScheduler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "num_train_timesteps": NUM_TRAIN_TIMESTEPS,
                "shift": (
                    "FLOAT",
                    {"default": 1.00000, "min": 0.00001, "step": 0.00001},
                ),
            },
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_SCHEDULER

    def run(self, **kwargs):
        scheduler_config = {"scheduler": "FlowMatchHeunDiscreteScheduler"}
        for k, v in kwargs.items():
            if k in ["num_train_timesteps", "shift"]:
                scheduler_config[k] = v
            # elif k in [""]:
            #     if v != "default": scheduler_config[k] = v
            # elif trilean(v) != None:
            #     scheduler_config[k] = trilean(v)
        return ({"scheduler": scheduler_config},)
