from .nodes import parameter, nodes_general

from .nodes.host import (
    environvar,
    host,
    host_asyncdiff,
    host_parallel,
    host_single,
)
from .nodes.model import lora, model
from .nodes.quantize import bitsandbytes, modelopt, quantize, quanto, sdnq
from .nodes.sampler import sampler, sdup_sampler
from .nodes.scheduler import (
    ddim_scheduler,
    ddpm_scheduler,
    deis_multistep_scheduler,
    dpmsolver_multistep_scheduler,
    dpmsolver_singlestep_scheduler,
    euler_ancestral_discrete_scheduler,
    euler_discrete_scheduler,
    flow_match_euler_discrete_scheduler,
    flow_match_heun_discrete_scheduler,
    heun_discrete_scheduler,
    kdpm2_ancestral_discrete_scheduler,
    kdpm2_discrete_scheduler,
    lms_discrete_scheduler,
    pndm_scheduler,
    tcd_scheduler,
    unipc_multistep_scheduler,
    scheduler_utils,
)
from .nodes.tools import convert

NODE_CLASS_MAPPINGS = {
    # model.model:
    "CheckpointSelector": model.CheckpointSelector,
    "ModelSelector": model.ModelSelector,
    "UnsafeModelSelector": model.UnsafeModelSelector,
    # model.lora:
    "LoraSelector": lora.LoraSelector,
    "MultiLoraJoiner": lora.MultiLoraJoiner,
    "MultiLoraJoinerMini": lora.MultiLoraJoinerMini,
    "MultiLoraJoinerLarge": lora.MultiLoraJoinerLarge,
    # scheduler:
    "CustomTimesteps": scheduler_utils.CustomTimesteps,
    "CustomSigmas": scheduler_utils.CustomSigmas,
    "DDIMScheduler": ddim_scheduler.DDIMScheduler,
    "DDPMScheduler": ddpm_scheduler.DDPMScheduler,
    "DEISMultistepScheduler": deis_multistep_scheduler.DEISMultistepScheduler,
    "DPMSolverMultistepScheduler": dpmsolver_multistep_scheduler.DPMSolverMultistepScheduler,
    "DPMSolverSinglestepScheduler": dpmsolver_singlestep_scheduler.DPMSolverSinglestepScheduler,
    "EulerAncestralDiscreteScheduler": euler_ancestral_discrete_scheduler.EulerAncestralDiscreteScheduler,
    "EulerDiscreteScheduler": euler_discrete_scheduler.EulerDiscreteScheduler,
    "FlowMatchEulerDiscreteScheduler": flow_match_euler_discrete_scheduler.FlowMatchEulerDiscreteScheduler,
    "FlowMatchHeunDiscreteScheduler": flow_match_heun_discrete_scheduler.FlowMatchHeunDiscreteScheduler,
    "HeunDiscreteScheduler": heun_discrete_scheduler.HeunDiscreteScheduler,
    "KDPM2AncestralDiscreteScheduler": kdpm2_ancestral_discrete_scheduler.KDPM2AncestralDiscreteScheduler,
    "KDPM2DiscreteScheduler": kdpm2_discrete_scheduler.KDPM2DiscreteScheduler,
    "LMSDiscreteScheduler": lms_discrete_scheduler.LMSDiscreteScheduler,
    "PNDMScheduler": pndm_scheduler.PNDMScheduler,
    "TCDScheduler": tcd_scheduler.TCDScheduler,
    "UniPCMultistepScheduler": unipc_multistep_scheduler.UniPCMultistepScheduler,
    # quantize:
    "QuantizationConfig": quantize.QuantizationConfig,
    "BitsAndBytesQuantizationConfig": bitsandbytes.BitsAndBytesQuantizationConfig,
    "QuantoQuantizationConfig": quanto.QuantoQuantizationConfig,
    "SDNQQuantizationConfig": sdnq.SDNQQuantizationConfig,
    "ModelOptQuantizationConfig": modelopt.ModelOptQuantizationConfig,
    # general:
    "TorchConfig": nodes_general.TorchConfig,
    "CompileConfig": nodes_general.CompileConfig,
    "GroupOffloadConfig": nodes_general.GroupOffloadConfig,
    "OffloadConfig": nodes_general.OffloadConfig,
    "AttentionBackendConfig": nodes_general.AttentionBackendConfig,
    "DeepCacheConfig": nodes_general.DeepCacheConfig,
    "CacheDiTConfig": nodes_general.CacheDiTConfig,
    # host:
    "EnvironVar": environvar.EnvironVar,
    "EnvironVarJoinerMini": environvar.EnvironVarJoinerMini,
    "EnvironVarJoiner": environvar.EnvironVarJoiner,
    "EnvironVarJoinerLarge": environvar.EnvironVarJoinerLarge,
    "AsyncDiffConfig": host_asyncdiff.AsyncDiffConfig,
    "ParallelConfig": host_parallel.ParallelConfig,
    "SingleConfig": host_single.SingleConfig,
    "CreateHost": host.CreateHost,
    "CloseHost": host.CloseHost,
    "ApplyPipeline": host.ApplyPipeline,
    "SleepHost": host.SleepHost,
    "OffloadPipeline": host.OffloadPipeline,
    # sampler:
    "SDUpscaleSampler": sdup_sampler.SDUpscaleSampler,
    "DiffusersSampler": sampler.DiffusersSampler,
    "DiffusersSamplerVideo": sampler.DiffusersSamplerVideo,
    # parameter:
    "Parameter": parameter.Parameter,
    "BooleanParameter": parameter.BooleanParameter,
    "StringParameter": parameter.StringParameter,
    "NumberParameter": parameter.NumberParameter,
    "ParameterJoinerMini": parameter.ParameterJoinerMini,
    "ParameterJoiner": parameter.ParameterJoiner,
    "ParameterJoinerLarge": parameter.ParameterJoinerLarge,
    # tools.convert:
    "StringToListString": convert.StringToListString,
    "StringToListNumber": convert.StringToListNumber,
    "StringToDict": convert.StringToDict,
}


NODE_DISPLAY_NAME_MAPPINGS = {
    # model.model:
    "CheckpointSelector": "Checkpoint",
    "ModelSelector": "Model",
    "UnsafeModelSelector": "Model (Unsafe)",
    # model.lora:
    "LoraSelector": "Lora",
    "MultiLoraJoiner": "Lora Joiner",
    "MultiLoraJoinerMini": "Lora Joiner (Mini)",
    "MultiLoraJoinerLarge": "Lora Joiner (Large)",
    # scheduler:
    "CustomTimesteps": "Timesteps",
    "CustomSigmas": "Sigmas",
    "DDIMScheduler": "DDIMScheduler",
    "DDPMScheduler": "DDPMScheduler",
    "DEISMultistepScheduler": "DEISMultistepScheduler",
    "DPMSolverMultistepScheduler": "DPMSolverMultistepScheduler",
    "DPMSolverSinglestepScheduler": "DPMSolverSinglestepScheduler",
    "EulerAncestralDiscreteScheduler": "EulerAncestralDiscreteScheduler",
    "EulerDiscreteScheduler": "EulerDiscreteScheduler",
    "FlowMatchEulerDiscreteScheduler": "FlowMatchEulerDiscreteScheduler",
    "FlowMatchHeunDiscreteScheduler": "FlowMatchHeunDiscreteScheduler",
    "HeunDiscreteScheduler": "HeunDiscreteScheduler",
    "KDPM2AncestralDiscreteScheduler": "KDPM2AncestralDiscreteScheduler",
    "KDPM2DiscreteScheduler": "KDPM2DiscreteScheduler",
    "LMSDiscreteScheduler": "LMSDiscreteScheduler",
    "PNDMScheduler": "PNDMScheduler",
    "TCDScheduler": "TCDScheduler",
    "UniPCMultistepScheduler": "UniPCMultistepScheduler",
    # quantize:
    "QuantizationConfig": "Quantize",
    "BitsAndBytesQuantizationConfig": "BitsAndBytes Quantize",
    "QuantoQuantizationConfig": "Quanto Quantize",
    "SDNQQuantizationConfig": "SDNQ Quantize",
    "ModelOptQuantizationConfig": "ModelOpt Quantize",
    # general:
    "TorchConfig": "Torch Settings",
    "CompileConfig": "Compile Settings",
    "GroupOffloadConfig": "Group Offload Settings",
    "OffloadConfig": "Module Offload Settings",
    "AttentionBackendConfig": "Attention Backend",
    "DeepCacheConfig": "DeepCache",
    "CacheDiTConfig": "CacheDiT",
    # host:
    "EnvironVar": "Environment Variable",
    "EnvironVarJoinerMini": "Env Var Joiner (Mini)",
    "EnvironVarJoiner": "Env Var Joiner",
    "EnvironVarJoinerLarge": "Env Var Joiner (Large)",
    "AsyncDiffConfig": "AsyncDiff Backend",
    "ParallelConfig": "Parallel Backend",
    "SingleConfig": "Single Backend",
    "CreateHost": "Create Host",
    "CloseHost": "Close Host",
    "ApplyPipeline": "Apply Pipeline",
    "SleepHost": "Sleep Host",
    "OffloadPipeline": "Offload Pipeline",
    # sampler:
    "SDUpscaleSampler": "Sampler (Diffusers SDUpscale)",
    "DiffusersSampler": "Sampler (Diffusers)",
    "DiffusersSamplerVideo": "Video Sampler (Diffusers)",
    # parameter:
    "Parameter": "Parameter",
    "BooleanParameter": "Boolean Parameter",
    "StringParameter": "String Parameter",
    "NumberParameter": "Number Parameter",
    "ParameterJoinerMini": "Parameter Joiner (Mini)",
    "ParameterJoiner": "Parameter Joiner",
    "ParameterJoinerLarge": "Parameter Joiner (Large)",
    # tools.convert:
    "StringToListString": "String to List<String>",
    "StringToListNumber": "String to List<Number>",
    "StringToDict": "String to Dict",
}


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
