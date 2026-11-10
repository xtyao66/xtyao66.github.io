---
layout: page
title: Programmable switches for distributed LLM systems
description: Fusing computation and placing state inside the network fabric
img: assets/img/publication_preview/smartfuse-llm.svg
importance: 1
category: current
related_publications: true
---

Distributed LLM training and inference push data through the network at every layer. This project
asks which work can move into the switch that the data already passes through, and when doing so
removes more critical-path time than it adds.

## SmartFuse-LLM: fusing computation into collectives

With tensor and sequence parallelism, every layer boundary does a reduce-scatter, a small residual
add and RMSNorm on each GPU, and then an all-gather. SmartFuse-LLM moves the add and RMSNorm into an
FPGA switch datapath, so the switch returns normalized activations directly and one of the two
network round trips disappears.
[Paper (ACM DL)](https://doi.org/10.1145/3814576.3814596)

{% include diagrams/smartfuse-llm.svg %}

<div class="kpis">
  <div class="kpi"><div class="kpi-value">50.5%</div><div class="kpi-label">projected lower latency per layer boundary</div></div>
  <div class="kpi"><div class="kpi-value">1</div><div class="kpi-label">network round trip instead of 2</div></div>
</div>

## PoolStateLens: evaluating an on-switch memory pool for training state

Fully sharded training spreads parameters and optimizer state across GPUs, so memory capacity grows
only by adding GPUs. A switch-attached memory pool, proposed in prior work, can hold that state instead: the switch multicasts
parameters to GPUs, reduces gradients back, and an optimizer beside the pool applies the update.
PoolStateLens is a measurement-grounded model, built on [GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/) measurements and [ASTRA-sim](https://github.com/astra-sim/astra-sim) checks, that asks how
fast such a pool must be to keep up with FSDP.
[PDF](https://ieee-hpec.org/wp-content/uploads/2026/09/327.pdf)

{% include diagrams/poolstatelens.svg %}

<div class="kpis">
  <div class="kpi"><div class="kpi-value">~7.9 TB/s</div><div class="kpi-label">aggregate raw state bandwidth to match FSDP (modeled, controlled 7B, 32-GPU case)</div></div>
  <div class="kpi"><div class="kpi-value">GB200</div><div class="kpi-label">NVL72 measurements ground the model</div></div>
</div>

## Next: stateful programmable switches

Ongoing work implements FPGA forward and backward datapaths and designs intermediate-state placement
and workload-aware offload policies for LLM training and inference. This line of work, the core of
my dissertation, builds on my
[SmartNIC offload for training]({{ '/research/smartnic-training/' | relative_url }}) work.

<span hidden>{% cite yao2026smartfusellm yao2026poolstatelens %}</span>
