---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 7
description: Curriculum vitae (PDF).
---

{% comment %}To update the CV, replace assets/pdf/cv.pdf with the new PDF (keep the file name).{% endcomment %}

<div class="cv-pdf-actions">
  <a class="btn-cv" href="{{ '/assets/pdf/cv.pdf' | relative_url }}" target="_blank" rel="noopener">Open PDF</a>
  <a class="btn-cv" href="{{ '/assets/pdf/cv.pdf' | relative_url }}" download="Xiteng_Yao_CV.pdf">Download</a>
</div>

<object class="cv-pdf" title="CV (PDF)" data="{{ '/assets/pdf/cv.pdf' | relative_url }}#view=FitH&navpanes=0" type="application/pdf">
  <p>Your browser can't show the PDF here.
  <a href="{{ '/assets/pdf/cv.pdf' | relative_url }}">Open the CV</a> instead.</p>
</object>
