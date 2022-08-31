# iRobot® Create® 3 Mounts, Cases, and Adapters
{% set repo = 'rudislabs' %}
{% set repo = 'jinja-ninja' %}
{% set data = listfiles("docs/hw/data/models") %}
{% for key0, val0 in data.items() %}
## {{ key0 }}
  {% for key1, val1 in val0.items() %}
### {{ key1 }}
    {% for keys, file in val1.items() %}
#### {{ keys }}
<details>
  <summary>3D-Rendering</summary>

  <script src="https://embed.github.com/view/3d/{{ repo }}/create3_docs/{{ branch }}/{{ file.path }}"></script>

</details>


* [STL ({{ file.size }})]({{ file.path }})
{% endfor %}
{% endfor %}
{% endfor %}

[^1]: All trademarks mentioned are the property of their respective owners.