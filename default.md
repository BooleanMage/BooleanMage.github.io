---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<ul>
  {% for category in site.categories %}
    <li><a href="/{{ category | first | slugify }}/">{{ category | first }}</a></li>
  {% endfor %}
</ul>