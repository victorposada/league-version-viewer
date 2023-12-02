from jinja2 import Template



input_string = "13.23.1"
split_parts = input_string.split('.')
result = '-'.join(split_parts[:2])
print(result)
