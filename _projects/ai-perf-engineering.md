---
layout: page
title: LLM performance modeling and AI for performance engineering
description: Predicting LLM inference performance, and measuring what helps code-optimizing agents
img: assets/img/publication_preview/kernelsight-lm.svg
importance: 3
category: current
related_publications: true
---

Two questions run through this work: can we predict how an LLM deployment will perform before
running it, and when an LLM agent or a learned search optimizes code, what actually helps it?

## KernelSight-LM: predicting LLM inference performance

Built during my [AWS internship]({{ '/experience/' | relative_url }}). KernelSight-LM extends the
[Vidur](https://github.com/microsoft/vidur) serving simulator and combines
models of GPU kernel latency, communication, and host overhead in a discrete-event scheduler that
replays batching and KV-cache behavior, predicting end-to-end latency and throughput for
hardware/software co-design and design-space exploration.
[Paper (arXiv)](https://arxiv.org/abs/2606.28565)

{% include diagrams/kernelsight-lm.svg %}

<div class="kpis">
  <div class="kpi"><div class="kpi-value">2.7%</div><div class="kpi-label">median throughput error, target-measured tier</div></div>
  <div class="kpi"><div class="kpi-value">6</div><div class="kpi-label">model families evaluated</div></div>
</div>

## ACBench: what helps LLM agents optimize code

ACBench turns merged performance pull requests from six production Go codebases into 14 tasks. An
agent proposes patches over several rounds; each patch is applied, tested, and benchmarked against
the human fix. Because a retry gives the model both new information and another chance, ACBench
compares error-guided and generic retry at an equal proposal budget to separate the two.
[PDF](https://ieee-hpec.org/wp-content/uploads/2026/09/266.pdf) ·
[Code](https://github.com/xtyao66/acbench)

{% include diagrams/acbench.svg %}

## RL-guided GPU compiler optimization on NVIDIA Blackwell

A runtime reward tells a reinforcement-learning search whether a GPU kernel got faster, but not why.
This work studies RL-guided optimization of [Triton](https://triton-lang.org/) kernels on
[NVIDIA Blackwell](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), looking at how changes carry through the compiler
to the final machine code, to understand when and why an optimization helps.
[PDF](https://ieee-hpec.org/wp-content/uploads/2026/09/267.pdf)

{% include diagrams/rl-gpu-compiler.svg %}

<span hidden>{% cite yao2026kernelsight yao2026acbench yao2026rlgpucompiler %}</span>
