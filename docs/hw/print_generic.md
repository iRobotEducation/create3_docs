# iRobot® Create® 3 Printable Generic Parts
{% set repo = 'rudislabs' %}
{% set branch = 'jinja-ninja' %}
{% set data = listfiles("docs/hw/data/models/Generic") %}
{% set render_size_limit = "5000" %}

{% for keys, file in data|dictsort %}
## {{ keys }}
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

[^1]: All trademarks mentioned are the property of their respective owners.