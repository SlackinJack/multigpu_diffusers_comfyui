from ..data_types import (
    NUM_TRAIN_TIMESTEPS,
    TRILEAN_DEFAULT,
    STEPS_OFFSET,
    TIMESTEPS,
    SIGMAS,
    PARAM,
    CATEGORY_SCHEDULER,
    trilean,
)


class EulerDiscreteScheduler:
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
                "prediction_type": (
                    ["default", "epsilon", "sample", "v_prediction"],
                    {"default": "default"},
                ),
                "interpolation_type": (
                    ["default", "linear", "log_linear"],
                    {"default": "default"},
                ),
                "use_karras_sigmas": TRILEAN_DEFAULT,
                "use_exponential_sigmas": TRILEAN_DEFAULT,
                "use_beta_sigmas": TRILEAN_DEFAULT,
                # "sigma_min"
                # "sigma_max"
                "timestep_spacing": (
                    ["default", "leading", "linspace", "trailing"],
                    {"default": "default"},
                ),
                "timestep_type": (
                    ["default", "discrete", "continuous"],
                    {"default": "default"},
                ),
                "steps_offset": STEPS_OFFSET,
                "rescale_betas_zero_snr": TRILEAN_DEFAULT,
                "final_sigma_type": (
                    ["default", "zero", "sigma_min"],
                    {"default": "default"},
                ),
            },
            "optional": {
                "timesteps": TIMESTEPS,
                "sigmas": SIGMAS,
            },
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_SCHEDULER

    def run(self, **kwargs):
        scheduler_config = {"scheduler": "EulerDiscreteScheduler"}
        for k, v in kwargs.items():
            if k in [
                "num_train_timesteps",
                "beta_start",
                "beta_end",
                "steps_offset",
                "timesteps",
                "sigmas",
            ]:
                scheduler_config[k] = v
            elif k in [
                "beta_schedule",
                "prediction_type",
                "interpolation_type",
                "timestep_spacing",
                "timestep_type",
                "final_sigma_type",
            ]:
                if v != "default":
                    scheduler_config[k] = v
            elif trilean(v) is not None:
                scheduler_config[k] = trilean(v)
        return ({"scheduler": scheduler_config},)
