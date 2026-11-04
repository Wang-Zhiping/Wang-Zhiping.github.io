---
layout: default
title: Research Experience
description: Research and project experience of Zhiping Wang.
---


<div class="project" id="phd">
<h3>Computational Phase Imaging for Monitoring Light-Based Additive Manufacturing</h3>
<p class="meta">PhD research, Laboratory of Applied Photonics Devices (LAPD), EPFL &middot; Supervisor: Prof. Christophe Moser &middot; Aug 2026 – present &middot; Lausanne, Switzerland</p>
<ul>
<li>Developing computational and quantitative phase imaging for in-situ monitoring, with the long-term goal of monitoring TVAM, SHVAM, and holographic fabrication.</li>
<li>Building a programmable Fourier ptychographic microscopy (FPM) / differential phase contrast (DPC) microscope with sparse multi-angle LED illumination, external camera triggering, and synchronized illumination and acquisition.</li>
<li>Developing illumination-angle, pupil, aberration, and defocus calibration; investigating vignetting, model mismatch, and few-frame imaging for dynamic processes.</li>
<li>Validating with USAF resolution targets, glass microspheres, and quantitative phase targets.</li>
<li><a href="publications/Wang_2026_poster_phase_imaging_SHVAM.pdf">Poster: Towards Computational Phase Imaging for Monitoring Light-Based Fabrication (PDF)</a></li>
</ul>
</div>

<div class="project" id="thesis">
<h3>3D Multi-View Tracking and Behavioral Analysis of <em>Drosophila</em></h3>
<p class="meta">Master's thesis, Biozentrum, University of Basel &middot; Advisors: Prof. Anissa Kempf and Dr. Alexandra Medeiros &middot; Oct 2025 – Jun 2026 &middot; Basel, Switzerland</p>
<ul>
<li>Built a mirror-based multi-view arena and trained DeepLabCut keypoint models; reconstructed metric 3D trajectories using calibration, triangulation, and outlier filtering, with MuJoCo/PyTorch STAC inverse kinematics for joint-angle analysis.</li>
<li>Developed locomotion, grooming, immobility, and sleep classifiers; applied hBehaveMAE to unsupervised repertoire discovery and an SVM to proboscis extension (&gt; 90% accuracy).</li>
<li>Thesis defended on Jun 8, 2026.</li>
</ul>
</div>

<div class="project" id="tvam">
<h3>3D Reconstruction for TVAM 3D-Printed Samples</h3>
<p class="meta">EPFL Excellence in Engineering (E3) summer project &middot; Advisors: Felix Wechsler, Dr. Jonathan Dong, and Prof. Christophe Moser, LAPD, EPFL &middot; Jun 2025 – Sep 2025 &middot; Lausanne, Switzerland</p>
<ul>
<li>Developed a multi-slice forward model for 3D FPM using angular-spectrum propagation and implicit neural representation (INR)-based inverse reconstruction in PyTorch; compared INR and voxel representations, improving fidelity and reducing artifacts in simulations.</li>
<li>Independently assembled an FPM setup with programmable LED illumination, optical alignment, acquisition, and reconstruction software; validated super-resolution using experimental data.</li>
</ul>
</div>

<div class="project" id="cryoet">
<h3>Optimal Filtered Back-Projection for Cryo-electron Tomography</h3>
<p class="meta">Master's project, Biozentrum &amp; Department of Mathematics and Computer Science, University of Basel &middot; Advisors: Dr. Ricardo Righetto and Dr. Valentin Debarnot &middot; Nov 2024 – Feb 2025 &middot; Basel, Switzerland</p>
<ul>
<li>Implemented ODL filtered back-projection and PyTorch filter learning with total-variation regularization; improved structural recovery on experimental <em>Chlamydomonas</em> data (EMPIAR-11830) compared with conventional filtered back-projection.</li>
<li><a href="publications/Zhiping_Report_cryo_opfbp.pdf">Project report (PDF)</a></li>
</ul>
</div>

<div class="project" id="fpm">
<h3>High-Efficiency Fourier Ptychographic Microscopy</h3>
<p class="meta">Research internship, Pioneering Interdiscipline Center, Chinese Academy of Sciences &middot; Supervisor: Dr. An Pan &middot; Aug 2023 – Jul 2024 &middot; China</p>
<ul>
<li>Investigated acquisition efficiency and wide-field quantitative phase imaging; identified block-stitching artifacts and expanded the reconstructed field of view from approximately 0.2 to 3.3 mm through simulation, calibration, and programmable LED illumination.</li>
<li>Developed nonlinear multi-exposure fusion (MEIF) for low-SNR dark-field data and contributed to feature-domain reconstruction; first-author <em>Advanced Photonics Nexus</em> and co-first-author <em>Optics &amp; Laser Technology</em> publications.</li>
<li>Notes: <a href="ResearchSummary%26Reporting/FPM/single-fast.html">single-shot algorithm</a>, <a href="ResearchSummary%26Reporting/FPM/fusion.html">phase fusion</a></li>
</ul>
</div>

<details class="earlier">
<summary>Earlier undergraduate projects (2020 – 2023)</summary>

<div class="project">
<h3>Improving the Efficiency of Photoacoustic Conversion in Photoacoustic Imaging</h3>
<p class="meta">Online research project, HISLab, School of Information Science and Technology, ShanghaiTech University &middot; Advisor: Prof. Fei Gao &middot; May 2023 – Sep 2023</p>
</div>

<div class="project">
<h3>Performance of Coherent Ising Machines in Weighted NP-Hard Problems</h3>
<p class="meta">Independent study &middot; Advisor: Jie Zhu, School of ECE, Purdue University (online) &middot; Dec 2022 – Aug 2023</p>
<ul>
<li>Code and details on <a href="https://github.com/Wang-Zhiping/Exploring-the-Performance-of-Coherent-Ising-Machine-in-weighted-NP-Hard-Problems">GitHub</a>.</li>
<li>Replicated prior research on an optical-parametric-oscillator (OPO)-based coherent Ising machine with numerical simulations in Python, solving the governing differential equations with the Runge–Kutta method.</li>
<li>Applied the coherent Ising machine to number partitioning and MAX-CUT on unweighted graphs; for MAX-CUT the Ising-machine approach had a higher success probability.</li>
<li>Extended MAX-CUT to weighted graphs and found similar trends, suggesting that the success probability may depend on the weights.</li>
</ul>
</div>

<div class="project">
<h3>Reproduction of Inverse Design of Nano-Optical Structures by Neural Networks</h3>
<p class="meta">Research assistant &middot; Advisor: Dr. Hao Jia, Lanzhou University &amp; KAUST &middot; Apr 2022 – Mar 2023</p>
<ul>
<li>Carried out literature research on inverse design methods for optoelectronic devices and their applications.</li>
<li>Built an optical system model with a tandem architecture combining forward modeling and inverse design, based on the work of Zongfu Yu's group.</li>
<li>Implemented it in Python with TensorFlow and reproduced the trends reported in the paper on a small dataset.</li>
</ul>
</div>

<div class="project">
<h3>Palm Print Identification</h3>
<p class="meta">Advisor: Dr. Jizhao Liu, School of Information Science and Engineering, Lanzhou University &middot; Nov 2021 – Mar 2022</p>
<ul>
<li>Code and details on <a href="https://github.com/Wang-Zhiping/palmprint-recognition">GitHub</a> and <a href="https://colab.research.google.com/drive/1UXjqFMbqhZZp2DVSjXcWU_WVvdc7rTjc?usp=sharing">Colab</a>.</li>
<li>Learned common operations in machine learning and digital image processing, especially biometrics.</li>
<li>Used various filters for feature extraction, followed by PCA for dimensionality reduction.</li>
<li>Achieved a high recognition rate on the Hong Kong Polytechnic University open-source database and on part of a student dataset.</li>
</ul>
</div>

<div class="project">
<h3>Nature and Causes of Candle Flame Oscillation</h3>
<p class="meta">Advisor: Dr. Ning Huang, School of Physical Science and Technology, Lanzhou University &middot; Oct 2020 – Sep 2021</p>
<ul>
<li>Reviewed the literature on the conditions and root causes of coupled flame oscillations when several candles burn close to each other.</li>
<li>Captured images and temperatures of the coupled oscillations and processed them with OpenCV to obtain experimental data.</li>
<li>Modeled and interpreted the phenomenon with thermodynamics and fluid dynamics.</li>
<li>Presented as a tournament topic at the China Undergraduate Physics Tournament (Northwest Region) and won the First Prize in Jun 2021.</li>
</ul>
</div>

</details>
