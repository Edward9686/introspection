import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None

    # Определяем другие интересные свойства
    other_properties = {}
    if hasattr(obj, "__doc__"):
        other_properties["doc"] = obj.__doc__

    if hasattr(obj, "__dict__"):
        other_properties["dict"] = obj.__dict__

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'other_properties': other_properties
    }


class SampleClass:
    """Это пример класса для демонстрации."""

    def __init__(self, value):
        self.value = value

    def increase(self):
        return self.value + 1

    def decrease(self):
        return self.value - 1


sample_obj = SampleClass(10)
info = introspection_info(sample_obj)
print(info)
