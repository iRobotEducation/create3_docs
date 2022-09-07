# iRobot® Create® 3 Printable Compute Board Parts
{% set repo = 'rudislabs' %}
{% set branch = 'jinja-ninja' %}
{% set data = listfiles("docs/hw/data/models/Compute") %}
{% set render_size_limit = "5000" %}

{% for key0, val0 in data|dictsort %}
## {{ key0|replace("NVIDIA", "NVIDIA®")|replace("Jetson", "Jetson™")|replace("Pi", "Pi®") }}
  {% for keys, file in val0|dictsort %}
### {{ keys }}
{% if file.size_raw_kb|float() < render_size_limit|float() %}
<details>
  <summary>3D-Rendering</summary>

  <script src="https://embed.github.com/view/3d/{{ repo }}/create3_docs/{{ branch }}/docs/{{ file.path }}/{{ file.name }}"></script>

</details>
{% else %}
<details>
  <summary>Ortho-Image</summary>

  <img src="../../{{ file.path}}/{{ file.name|replace(file.extension, "png") }}"></img>

</details>
{% endif %}



* [STL ({{ file.size_str }})](../{{ file.path }}/{{ file.name }})

{% endfor %}
{% endfor %}

[^1]: All trademarks mentioned are the property of their respective owners.