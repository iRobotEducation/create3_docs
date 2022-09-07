# iRobot® Create® 3 Printable Sensor Mount Parts
{% set data = listfiles("docs/hw/data/models/Sensors") %}

{% for key0, val0 in data|dictsort %}
## {{ key0|replace("IntelRealSense", "Intel® RealSense™")|replace("SLAMTEC", "SLAMTEC®")|replace("Luxonis", "Luxonis®") }}
  {% for keys, file in val0|dictsort %}
### {{ keys|replace("Oak-D", "Oak-D®") }}
{% if file.size_raw_kb|float() < render_size_limit|float() %}
<details>
  <summary>3D-Rendering</summary>

  <script src="https://embed.github.com/view/3d/{{ repo }}/create3_docs/{{ org }}/docs/{{ file.path }}/{{ file.name }}"></script>

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