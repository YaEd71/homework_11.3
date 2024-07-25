def introspection_info(obj):
    info = {}

    # Тип объекта
    info['type'] = type(obj).__name__

    # Атрибуты и методы объекта
    attributes = []
    methods = []

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)

    info['attributes'] = attributes
    info['methods'] = methods

    # Модуль, к которому объект принадлежит
    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    else:
        info['module'] = None

    # Дополнительные интересные свойства объекта
    if isinstance(obj, (int, float, complex)):
        info['properties'] = {
            'is_integer': isinstance(obj, int),
            'is_float': isinstance(obj, float),
            'is_complex': isinstance(obj, complex)
        }
    elif isinstance(obj, str):
        info['properties'] = {
            'length': len(obj),
            'is_alpha': obj.isalpha(),
            'is_digit': obj.isdigit()
        }
    elif isinstance(obj, list):
        info['properties'] = {
            'length': len(obj),
            'contains': [type(item).__name__ for item in obj]
        }
    else:
        info['properties'] = 'No additional properties available'

    return info


# Пример работы
number_info = introspection_info(42)
print(number_info)


# Создание пользовательского класса и объекта
class CustomClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def greet(self):
        return f"Hello, {self.name}!"

    def add_value(self, addend):
        self.value += addend
        return self.value


custom_obj = CustomClass("Alice", 10)
custom_obj_info = introspection_info(custom_obj)
print(custom_obj_info)