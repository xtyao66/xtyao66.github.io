---
layout: page
title: Research
permalink: /research/
description: Research projects, current and earlier. Each page lists its related papers.
nav: true
nav_order: 3
display_categories: [current, earlier]
horizontal: false
---

{% comment %}Cards are generated from the _projects collection, ordered by `importance`.{% endcomment %}
<div class="projects">
{% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
{% endfor %}
</div>
