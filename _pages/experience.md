---
layout: page
permalink: /experience/
title: Experience
description: Industry internships, research, teaching, and service.
nav: true
nav_order: 4
---

<div class="xp">

  <div class="xp-item">
    <div class="xp-when">May 2026 – Aug 2026</div>
    <div class="xp-role">AI Research Scientist Intern</div>
    <div class="xp-org"><a href="https://www.arm.com/">Arm</a> <span class="xp-where">· Seattle, WA</span></div>
    <ul>
      <li>Built a runtime for <strong>attention–FFN disaggregation (AFD)</strong> in LLM inference, running attention and feed-forward layers as separate serving stages.</li>
      <li>Implemented context-length-aware request routing and expert routing to handle workload and mixture-of-experts imbalance.</li>
    </ul>
    <div class="xp-tags"><span class="xp-tag">LLM inference</span><span class="xp-tag">disaggregated serving</span><span class="xp-tag">MoE</span><span class="xp-tag">vLLM</span></div>
  </div>

  <div class="xp-item">
    <div class="xp-when">Aug 2025 – Dec 2025</div>
    <div class="xp-role">Applied Scientist Intern</div>
    <div class="xp-org"><a href="https://aws.amazon.com/">Amazon Web Services</a> <span class="xp-where">· Santa Clara, CA</span></div>
    <ul>
      <li>Quantified LLM serving optimizations (prefill/decode disaggregation, continuous batching, prefix caching) and tuned <a href="https://github.com/vllm-project/vllm">vLLM</a> runtime parameters for deployments.</li>
      <li>Built <strong>KernelSight-LM</strong>, a kernel-level LLM inference simulator that combines kernel-latency, communication, and host-overhead models in a discrete-event scheduler; 2.7% median throughput-prediction error (target-measured tier) across six model families. It extends the open-source <a href="https://github.com/microsoft/vidur">Vidur</a> serving simulator.</li>
    </ul>
    <div class="xp-tags"><span class="xp-tag">GPU performance modeling</span><span class="xp-tag">simulation</span><span class="xp-tag">vLLM</span></div>
    <div class="xp-links"><a href="https://arxiv.org/abs/2606.28565">Paper (arXiv)</a><a href="{{ '/research/ai-perf-engineering/' | relative_url }}">Research page</a></div>
  </div>

  <div class="xp-item">
    <div class="xp-when">Sep 2023 – present</div>
    <div class="xp-role">PhD Researcher</div>
    <div class="xp-org"><a href="https://www.bu.edu/caadlab/">CAAD Lab</a>, Boston University <span class="xp-where">· Boston, MA</span></div>
    <ul>
      <li>Systems for large language models with <a href="https://www.bu.edu/eng/profile/martin-herbordt/">Prof. Martin Herbordt</a>: programmable switches and SmartNICs for distributed training and inference, FPGA-accelerated secure ML, and AI for performance engineering.</li>
      <li>Papers at ACM ICS, HEART, and IEEE HPEC, including the HPEC 2025 Outstanding Student Paper Award.</li>
    </ul>
    <div class="xp-tags"><span class="xp-tag">FPGA</span><span class="xp-tag">SmartNIC</span><span class="xp-tag">RDMA</span><span class="xp-tag">collectives</span><span class="xp-tag">ASTRA-sim</span></div>
    <div class="xp-links"><a href="{{ '/research/' | relative_url }}">Research</a><a href="{{ '/publications/' | relative_url }}">Publications</a></div>
  </div>

  <div class="xp-item">
    <div class="xp-when">Apr 2022 – Aug 2023</div>
    <div class="xp-role">Undergraduate Researcher</div>
    <div class="xp-org"><a href="https://www.bu.edu/caadlab/">CAAD Lab</a>, Boston University, with Red Hat <span class="xp-where">· Boston, MA</span></div>
    <ul>
      <li>Machine-learning-guided LLVM optimization for FPGA high-level synthesis, funded by the <a href="https://www.bu.edu/rhcollab/">Red Hat Collaboratory</a>; published at LLVM-HPC 2022.</li>
    </ul>
    <div class="xp-links"><a href="{{ '/research/ml-hls/' | relative_url }}">Research page</a><a href="https://www.bu.edu/caadlab/Shahzad22.pdf">Paper (PDF)</a><a href="https://www.bu.edu/rhcollab/2022/04/14/red-hat-collaboratory-announces-2022-student-research-projects/">Red Hat Collaboratory project</a></div>
  </div>

</div>

## Teaching

Teaching assistant, [Department of Electrical and Computer Engineering](https://www.bu.edu/eng/academics/departments-and-divisions/electrical-and-computer-engineering/), Boston University, 2019–2026:
ten semesters in total.

| Course | Title | Semesters |
| --- | --- | --- |
| [EC311](https://www.bu.edu/academics/eng/courses/eng-ec-311/) | Digital Logic Design | 2 |
| [EC413](https://www.bu.edu/academics/eng/courses/eng-ec-413/) | Computer Organization | 4 |
| [EC440](https://www.bu.edu/academics/eng/courses/eng-ec-440/) | Operating Systems | 1 |
| [EC528](https://www.bu.edu/academics/eng/courses/eng-ec-528/) | Cloud Computing | 1 |
| [EK103](https://www.bu.edu/academics/eng/courses/eng-ek-103/) | Linear Algebra | 1 |
| [EK307](https://www.bu.edu/academics/eng/courses/eng-ek-307/) | Electrical Circuits | 1 |

## Service

**Journal reviewer:** [IEEE Transactions on Parallel and Distributed Systems (TPDS)](https://www.computer.org/csdl/journal/td) ·
[Future Generation Computer Systems (FGCS)](https://www.sciencedirect.com/journal/future-generation-computer-systems) ·
[ACM Transactions on Reconfigurable Technology and Systems (TRETS)](https://dl.acm.org/journal/trets)

**Conference and workshop reviewer:** [IEEE FCCM](https://www.fccm.org/) · [FPT](https://fpt2025.shanghaitech.edu.cn/) ·
[H2RC](https://h2rc.cse.sc.edu/) · [IEEE HPEC](https://ieee-hpec.org/) · [HEART](https://heart2026.github.io/) ·
[MIT URTC](https://urtc.mit.edu/)
