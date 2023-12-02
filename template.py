from jinja2 import Environment, FileSystemLoader

with open('current_version', 'r') as file:
    current_version = file.read()

split_parts = current_version.split('.')
link_version = '-'.join(split_parts[:2])

def render_template(template_path, context):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    output = template.render(context)
    return output

# Define the path to your HTML template
template_path = 'index.html.j2'  # Replace with the actual filename

# Define the context data you want to pass to the template
context_data = {
    'version': current_version,
    'link_version': link_version,
}

result = render_template(template_path, context_data)

output_file_path = 'index.html'

# Guarda el resultado en el archivo de salida
with open(output_file_path, 'w') as output_file:
    output_file.write(result)
