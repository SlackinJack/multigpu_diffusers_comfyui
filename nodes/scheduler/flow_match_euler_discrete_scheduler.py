from ..data_types import (
    NUM_TRAIN_TIMESTEPS,
    INT_MAX,
    TRILEAN_DEFAULT,
    TIMESTEPS,
    SIGMAS,
    PARAM,
    CATEGORY_SCHEDULER,
    trilean,
)


class FlowMatchEulerDiscreteScheduler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "num_train_timesteps": NUM_TRAIN_TIMESTEPS,
                "shift": (
                    "FLOAT",
                    {"default": 1.00000, "min": 0.00000, "step": 0.00001},
                ),
                "use_dynamic_shifting": TRILEAN_DEFAULT,
                "base_shift": (
                    "FLOAT",
                    {"default": 0.50000, "min": 0.00000, "step": 0.00001},
                ),
                "max_shift": (
                    "FLOAT",
                    {"default": 1.15000, "min": 0.00000, "step": 0.00001},
                ),
                "base_image_seq_len": (
                    "INT",
                    {"default": 256, "min": 0, "max": INT_MAX},
                ),
                "max_image_seq_len": (
                    "INT",
                    {"default": 4096, "min": 0, "max": INT_MAX},
                ),
                "invert_sigmas": TRILEAN_DEFAULT,
                "shift_terminal": (
                    "FLOAT",
                    {"default": 0.00000, "min": 0.00000, "step": 0.00001},
                ),
                "use_karras_sigmas": TRILEAN_DEFAULT,
                "use_exponential_sigmas": TRILEAN_DEFAULT,
                "use_beta_sigmas": TRILEAN_DEFAULT,
                "time_shift_type": (
                    ["linear", "exponential", "default"],
                    {"default": "default"},
                ),
                "stochastic_sampling": TRILEAN_DEFAULT,
            },
            "optional": {
                "timesteps": TIMESTEPS,
                "sigmas": SIGMAS,
                # "mu":                     MU,
            },
        }

    RETURN_TYPES = PARAM
    FUNCTION = "run"
    CATEGORY = CATEGORY_SCHEDULER

    def run(self, **kwargs):
        scheduler_config = {"scheduler": "FlowMatchEulerDiscreteScheduler"}
        for k, v in kwargs.items():
            if k in [
                "num_train_timesteps",
                "shift",
                "base_shift",
                "max_shift",
                "base_image_seq_len",
                "max_image_seq_len",
                "shift_terminal",
                "timesteps",
                "sigmas",
            ]:
                scheduler_config[k] = v
            elif k in ["time_shift_type"]:
                if v != "default":
                    scheduler_config[k] = v
            elif trilean(v) is not None:
                scheduler_config[k] = trilean(v)
        return ({"scheduler": scheduler_config},)
