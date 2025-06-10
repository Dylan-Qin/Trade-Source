---
layout: post
categories: paper
title: "DecouplingRiskDetectionand Captioning Via Dual-Branch Multi-Scale Spatial-Temporal Fusion for Autonomous Driving"
author: "Zeyu Pan"
date: 2025-01-17
tags: ['Video captioning', ' risk detection', ' spatial-temporal fusion', ' Autonomous driving']
---

Risk detection aims to identify the objects that threaten the driver, while the captioning task focuses on generating a caption to describe the scene and provide driving suggestions. Previous methods train the model coupling risk detection and captioning task with a single low-resolution input. However, they face two primary challenges: 1) they only handle the video captioning task while failing to handle the other closely relevant downstream task such as question answering, and visual grounding; 2) they fail to well detect small objects in complex scenes. To address these challenges, we propose a Dual-branch Multi-scale Spatial-temporal Fusion (DMSF) method to decouple the two tasks, i.e., risk detection and captioning. In particular, it unleashes the potential of the vision-language model for more relevant downstream tasks, e.g., multi-modal question answering. Specifically, our method incorporates a High-Low Resolution Spatial-Temporal Fusion module that integrates multi-scale visual features from the high-resolution frames and spatial-temporal features from low-resolution frames. This helps the model to capture the small objects. Meanwhile, our method utilizes a Dual-Branch Abstractor to decouple the risk detection and captioning tasks, while consider the visual token cues by an abstractor. Experiments on the benchmark dataset demonstrate the effectiveness of our approach in both risk detection and captioning tasks. For example, it achieves a SPICE (Semantic Propositional Image Caption Evaluation) score of 66.2 for captioning and improves detection performance by a gain of 5% in terms of mIoU (mean Intersection over Union).

风险检测旨在识别威胁驾驶员的物体，而描述任务则侧重于生成场景描述并提供驾驶建议。现有方法通常采用单一低分辨率输入耦合训练风险检测与描述任务模型，但面临两大核心挑战：1)仅能处理视频描述任务，无法应对问答、视觉定位等其他紧密相关的下游任务；2)难以有效检测复杂场景中的小物体。为此，我们提出双分支多尺度时空融合（DMSF）方法，将风险检测与描述任务解耦。该方法释放了视觉语言模型在多模态问答等下游任务中的潜力，具体通过高低分辨率时空融合模块整合高分辨率帧的多尺度视觉特征与低分辨率帧的时空特征，显著提升小物体检测能力；同时采用双分支抽象器解耦两项任务，并通过抽象器融合视觉标记线索。基准数据集实验表明，本方法在描述任务中取得66.2的SPICE分数，检测任务mIoU指标提升5%。

资源链接: [DecouplingRiskDetectionand Captioning Via Dual-Branch Multi-Scale Spatial-Temporal Fusion for Autonomous Driving](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5101150)
