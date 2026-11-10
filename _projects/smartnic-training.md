---
layout: page
title: SmartNIC offload for large-model training
description: Overlapping ZeRO communication with GPU and CPU computation
img: assets/img/publication_preview/sgc.svg
importance: 2
category: current
related_publications: true
---

ZeRO-style training repeatedly gathers parameters from other GPUs and offloads state to host memory,
so the GPU often waits on data movement. This work puts a SmartNIC in that data path: it prefetches
and buffers parameters from the network and host memory and schedules their delivery to the GPU,
overlapping communication with GPU and CPU computation and reducing duplicate parameter gathers.
[Paper (ACM DL)](https://doi.org/10.1145/3721145.3729514)

{% include diagrams/sgc.svg %}

<div class="kpis">
  <div class="kpi"><div class="kpi-value">&gt;1.6×</div><div class="kpi-label">projected training throughput, 100B-parameter model</div></div>
  <div class="kpi"><div class="kpi-value">ICS 2025</div><div class="kpi-label">ACM International Conference on Supercomputing</div></div>
</div>

<span hidden>{% cite guo2025sgc %}</span>
