from .__registry__ import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

from ..data_types import (
    NUM_TRAIN_TIMESTEPS,
    INT_MIN,
    INT_MAX,
    TRILEAN_DEFAULT,
    STEPS_OFFSET,
    TIMESTEPS,
    PARAM,
    CATEGORY_SCHEDULER,
    trilean,
)


class HeunDiscreteScheduler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "num_train_timesteps": NUM_TRAIN_TIMESTEPS,
                "beta_start": (
                    "FLOAT",
                    {
                        "default": 0.00085,
                        "min": 0.00000,
                        "max": 1.00000,
                        "step": 0.00001,
                    },
                ),
                "beta_end": (
                    "FLOAT",
                    {
                        "default": 0.01200,
                        "min": 0.00000,
                        "max": 1.00000,
                        "step": 0.00001,
                    },
                ),
                "beta_schedule": (
                    [
                        "default",
                        "linear",
                        "scaled_linear",
                        "squaredcos_cap_v2",
                        "exp",
                    ],
                    {"default": "default"},
                ),
                # "trained_betas"
                "prediction_type": (
                    ["default", "epsilon", "sample", "v_prediction"],
                    {"default": "default"},
                ),
                "clip_sample": TRILEAN_DEFAULT,
                "clip_sample_range": (
                    "FLOAT",
                    {
                        "default": 1.00000,
                        "min": INT_MIN,
                        "max": INT_MAX,
                        "step": 0.00001,
                    },
                ),
                "use_karras_sigmas": TRILEAN_DEFAULT,
                "use_exponential_sigmas": TRILEAN_DEFAULT,
                "use_beta_sigmas": TRILEAN_DEFAULT,
                "timestep_spacing": (
                    ["default", "leading", "linspace", "trailing"],
                    {"default": "default"},
                ),
                "steps_offset": STEPS_OFFSET,
            },
            "optional": {
                "timesteps": TIMESTEPS,
            },
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_SCHEDULER

    def run(self, **kwargs):
        scheduler_config = {"scheduler": "HeunDiscreteScheduler"}
        for k, v in kwargs.items():
            if k in [
                "num_train_timesteps",
                "beta_start",
                "beta_end",
                "clip_sample_range",
                "steps_offset",
                "timesteps",
            ]:
                scheduler_config[k] = v
            elif k in ["beta_schedule", "prediction_type", "timestep_spacing"]:
                if v != "default":
                    scheduler_config[k] = v
            elif trilean(v) is not None:
                scheduler_config[k] = trilean(v)
        return ({"scheduler": scheduler_config},)


NODE_CLASS_MAPPINGS.update({"HeunDiscreteScheduler": HeunDiscreteScheduler})
NODE_DISPLAY_NAME_MAPPINGS.update(
    {"HeunDiscreteScheduler": "HeunDiscreteScheduler"}
)
