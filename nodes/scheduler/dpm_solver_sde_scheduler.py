from ..data_types import (
    NUM_TRAIN_TIMESTEPS,
    TRILEAN_DEFAULT,
    STEPS_OFFSET,
    PARAM,
    CATEGORY_SCHEDULER,
    trilean,
)


class DPMSolverSDEScheduler:
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
                "use_karras_sigmas": TRILEAN_DEFAULT,
                "use_exponential_sigmas": TRILEAN_DEFAULT,
                "use_beta_sigmas": TRILEAN_DEFAULT,
                # "noise_sampler_seed"
                "timestep_spacing": (
                    ["default", "leading", "linspace", "trailing"],
                    {"default": "default"},
                ),
                "steps_offset": STEPS_OFFSET,
            }
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_SCHEDULER

    def run(self, **kwargs):
        scheduler_config = {"scheduler": "DPMSolverSDEScheduler"}
        for k, v in kwargs.items():
            if k in [
                "num_train_timesteps",
                "beta_start",
                "beta_end",
                "steps_offset",
            ]:
                scheduler_config[k] = v
            elif k in ["beta_schedule", "prediction_type", "timestep_spacing"]:
                if v != "default":
                    scheduler_config[k] = v
            elif trilean(v) is not None:
                scheduler_config[k] = trilean(v)
        return ({"scheduler": scheduler_config},)
