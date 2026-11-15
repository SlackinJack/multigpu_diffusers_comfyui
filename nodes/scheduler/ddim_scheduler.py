from ..data_types import (
    NUM_TRAIN_TIMESTEPS,
    TRILEAN_DEFAULT,
    INT_MIN,
    INT_MAX,
    STEPS_OFFSET,
    PARAM,
    CATEGORY_SCHEDULER,
    trilean,
)


class DDIMScheduler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "num_train_timesteps": NUM_TRAIN_TIMESTEPS,
                "beta_start": (
                    "FLOAT",
                    {
                        "default": 0.00010,
                        "min": 0.00000,
                        "max": 1.00000,
                        "step": 0.00001,
                    },
                ),
                "beta_end": (
                    "FLOAT",
                    {
                        "default": 0.02000,
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
                    ],
                    {"default": "default"},
                ),
                # "trained_betas"
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
                "set_alpha_to_one": TRILEAN_DEFAULT,
                "steps_offset": STEPS_OFFSET,
                "prediction_type": (
                    ["default", "epsilon", "sample", "v_prediction"],
                    {"default": "default"},
                ),
                "thresholding": TRILEAN_DEFAULT,
                "dynamic_threasholding_ratio": (
                    "FLOAT",
                    {
                        "default": 0.99500,
                        "min": INT_MIN,
                        "max": INT_MAX,
                        "step": 0.00001,
                    },
                ),
                "sample_max_value": (
                    "FLOAT",
                    {
                        "default": 1.00000,
                        "min": INT_MIN,
                        "max": INT_MAX,
                        "step": 0.00001,
                    },
                ),
                "timestep_spacing": (
                    ["default", "leading", "linspace", "trailing"],
                    {"default": "default"},
                ),
                "rescale_betas_zero_snr": TRILEAN_DEFAULT,
            }
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_SCHEDULER

    def run(self, **kwargs):
        scheduler_config = {"scheduler": "DDIMScheduler"}
        for k, v in kwargs.items():
            if k in [
                "num_train_timesteps",
                "beta_start",
                "beta_end",
                "clip_sample_range",
                "steps_offset",
                "dynamic_threasholding_ratio",
                "sample_max_value",
            ]:
                scheduler_config[k] = v
            elif k in ["beta_schedule", "prediction_type", "timestep_spacing"]:
                if v != "default":
                    scheduler_config[k] = v
            elif trilean(v) is not None:
                scheduler_config[k] = trilean(v)
        return ({"scheduler": scheduler_config},)
