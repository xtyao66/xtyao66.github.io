---
layout: page
title: FPGA-accelerated secure machine learning
description: Multi-party computation on FPGA SmartNICs with RDMA
img: assets/img/publication_preview/mpc-fpga.svg
importance: 4
category: current
related_publications: true
---

Multi-party computation (MPC) lets several parties train or evaluate a model jointly without
revealing their inputs, but every multiplication needs a round of communication between parties.
This project runs the MPC engine on FPGA SmartNICs and connects them with the [Coyote](https://github.com/fpgasystems/Coyote) RDMA stack, so
secret-shared data moves between parties without touching the host CPU and communication overlaps
with computation.
[Paper (IEEE Xplore)](https://doi.org/10.1109/HPEC67600.2025.11196126)

{% include diagrams/mpc-fpga.svg %}

<div class="kpis">
  <div class="kpi"><div class="kpi-value">2.1×</div><div class="kpi-label">faster convolution layers than existing MPC frameworks</div></div>
  <div class="kpi"><div class="kpi-value">HPEC 2025</div><div class="kpi-label"><a href="{{ '/awards/' | relative_url }}">Outstanding Student Paper Award</a></div></div>
</div>

Current work extends this to GPU–FPGA acceleration with GPUDirect RDMA, aiming to cut host-memory
copies from the secure-training data path.

<span hidden>{% cite yao2025mpc %}</span>
