from comfy.utils import ProgressBar
from torchvision.transforms import ToPILImage, ToTensor


from .data_types import *
from .nodes_general import *
from ..modules.host_manager import *
from ..multigpu_diffusion.modules.utils import *


SINGLE_CONFIGS = {
}


SINGLE_CONFIGS_OPTIONAL = {
    "cache_dit_config": CACHE_DIT_CONFIG,
    "deepcache_config": DEEPCACHE_CONFIG,
}


class SingleConfig:
    @classmethod
    def INPUT_TYPES(s): return { "required": SINGLE_CONFIGS, "optional": SINGLE_CONFIGS_OPTIONAL, }
    RETURN_TYPES, FUNCTION, CATEGORY = BACKEND_CONFIG, "get_config", ROOT_CATEGORY_CONFIG
    def get_config(self, **kwargs): return (kwargs,)
