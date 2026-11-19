from .nodes import parameter

NODE_CLASS_MAPPINGS = {
    # parameter:
    "Parameter": parameter.Parameter,
    "BooleanParameter": parameter.BooleanParameter,
    "StringParameter": parameter.StringParameter,
    "NumberParameter": parameter.NumberParameter,
    "ParameterJoinerMini": parameter.ParameterJoinerMini,
    "ParameterJoiner": parameter.ParameterJoiner,
    "ParameterJoinerLarge": parameter.ParameterJoinerLarge,
}


NODE_DISPLAY_NAME_MAPPINGS = {
    # parameter:
    "Parameter": "Parameter",
    "BooleanParameter": "Boolean Parameter",
    "StringParameter": "String Parameter",
    "NumberParameter": "Number Parameter",
    "ParameterJoinerMini": "Parameter Joiner (Mini)",
    "ParameterJoiner": "Parameter Joiner",
    "ParameterJoinerLarge": "Parameter Joiner (Large)",
}


from .nodes.host import __registry__ as host

NODE_CLASS_MAPPINGS.update(host.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(host.NODE_DISPLAY_NAME_MAPPINGS)


from .nodes.model import __registry__ as model

NODE_CLASS_MAPPINGS.update(model.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(model.NODE_DISPLAY_NAME_MAPPINGS)


from .nodes.quantize import __registry__ as quantize

NODE_CLASS_MAPPINGS.update(quantize.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(quantize.NODE_DISPLAY_NAME_MAPPINGS)


from .nodes.sampler import __registry__ as sampler

NODE_CLASS_MAPPINGS.update(sampler.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(sampler.NODE_DISPLAY_NAME_MAPPINGS)


from .nodes.scheduler import __registry__ as scheduler

NODE_CLASS_MAPPINGS.update(scheduler.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(scheduler.NODE_DISPLAY_NAME_MAPPINGS)


from .nodes.tools import __registry__ as tools

NODE_CLASS_MAPPINGS.update(tools.NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(tools.NODE_DISPLAY_NAME_MAPPINGS)


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
