---
layout: about
title: About
permalink: /
subtitle: PhD Candidate, <a href="https://www.bu.edu/eng/academics/departments-and-divisions/electrical-and-computer-engineering/">Electrical and Computer Engineering</a>, <a href="https://www.bu.edu/">Boston University</a>

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false

selected_papers: true # papers marked selected={true} in _bibliography/papers.bib
social: false # icons are placed in the page body below instead, so they sit above the news

announcements:
  enabled: true
  scrollable: false
  limit: 6

latest_posts:
  enabled: false
---

I am a PhD candidate in Computer Engineering at Boston University, advised by
[Prof. Martin Herbordt](https://www.bu.edu/eng/profile/martin-herbordt/) in the [CAAD Lab](https://www.bu.edu/caadlab/) (Computer Architecture and Automated Design), expecting to graduate in May 2027.

My research is on **systems for large language models**: where computation, state, and coordination
should live in distributed LLM training and inference. I work across the stack, from
[programmable switches]({{ '/research/programmable-switches/' | relative_url }}) and
[SmartNIC datapaths]({{ '/research/smartnic-training/' | relative_url }}), through collective
communication and RDMA, to [GPU performance modeling]({{ '/research/ai-perf-engineering/' | relative_url }})
and LLM serving runtimes. I also build
[FPGA accelerators for secure machine learning]({{ '/research/secure-ml-mpc/' | relative_url }}),
and ask how to measure what really helps
[LLM agents that optimize code]({{ '/research/ai-perf-engineering/' | relative_url }}).

I have interned at **[Arm](https://www.arm.com/)** as an AI Research Scientist Intern, working on attention–FFN
disaggregated LLM inference, and at **[Amazon Web Services](https://aws.amazon.com/)** as an Applied Scientist Intern, where I
built [KernelSight-LM](https://arxiv.org/abs/2606.28565), a kernel-level LLM inference simulator.
More in [experience]({{ '/experience/' | relative_url }}) and the [CV]({{ '/cv/' | relative_url }}).

**Research interests:** LLM training and inference systems · SmartNIC/FPGA acceleration ·
programmable and stateful switches · collective communication · GPU performance modeling ·
AI for performance engineering · privacy-preserving computation.

<div class="social social-top">
  <div class="contact-icons">{% social_links %}</div>
  <div class="contact-note">{{ site.contact_note }}</div>
</div>
