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


class TCDScheduler:
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
                    ],
                    {"default": "default"},
                ),
                # "trained_betas"
                "original_inference_steps": (
                    "INT",
                    {"default": 50, "min": 0, "max": INT_MAX},
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
                "set_alpha_to_one": TRILEAN_DEFAULT,
                "steps_offset": STEPS_OFFSET,
                "prediction_type": (
                    ["default", "epsilon", "sample", "v_prediction"],
                    {"default": "default"},
                ),
                "thresholding": TRILEAN_DEFAULT,
                "dynamic_thresholding_ratio": (
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
                "timestep_scaling": (
                    "FLOAT",
                    {
                        "default": 10.00000,
                        "min": INT_MIN,
                        "max": INT_MAX,
                        "step": 0.00001,
                    },
                ),
                "rescale_betas_zero_snr": TRILEAN_DEFAULT,
            },
            "optional": {
                "timesteps": TIMESTEPS,
            },
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_SCHEDULER

    def run(self, **kwargs):
        scheduler_config = {"scheduler": "TCDScheduler"}
        for k, v in kwargs.items():
            if k in [
                "num_train_timesteps",
                "beta_start",
                "beta_end",
                "original_inference_steps",
                "clip_sample_range",
                "dynamic_thresholding_ratio",
                "sample_max_value",
                "timestep_scaling",
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
