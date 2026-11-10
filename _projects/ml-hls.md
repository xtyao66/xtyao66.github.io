---
layout: page
title: Machine-learning-guided compiler optimization for FPGAs
description: Learning LLVM pass sequences for high-level synthesis
img: assets/img/publication_preview/rl-hls.svg
importance: 5
category: earlier
related_publications: true
---

High-level synthesis compiles C/C++ code into FPGA hardware, but LLVM's optimization pipeline is
tuned for CPUs and serves FPGA back ends poorly. With the [CAAD Lab](https://www.bu.edu/caadlab/) and [Red Hat](https://www.bu.edu/rhcollab/), I worked on letting a
learned agent choose the LLVM pass sequence instead, rewarded by the quality of the resulting
hardware, and compared supervised and reinforcement-learning approaches using RNN, Transformer, and
GNN models of the program.
[Paper (PDF)](https://www.bu.edu/caadlab/Shahzad22.pdf) ·
[Red Hat Collaboratory project (2022)](https://www.bu.edu/rhcollab/2022/04/14/red-hat-collaboratory-announces-2022-student-research-projects/) ·
[Red Hat Research project page](https://research.redhat.com/blog/research_project/practical-programming-of-fpgas-with-open-source-tools/)

{% include diagrams/rl-hls.svg %}

<div class="kpis">
  <div class="kpi"><div class="kpi-value">up to 3×</div><div class="kpi-label">speedup over <code>-O3</code></div></div>
  <div class="kpi"><div class="kpi-value">up to 23×</div><div class="kpi-label">faster learning</div></div>
</div>

<span hidden>{% cite shahzad2022rlhls %}</span>
