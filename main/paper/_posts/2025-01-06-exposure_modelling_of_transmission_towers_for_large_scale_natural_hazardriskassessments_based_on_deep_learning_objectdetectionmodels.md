---
layout: post
categories: paper
title: "Exposure Modelling of Transmission Towers for Large-Scale Natural HazardRiskAssessments Based on Deep-Learning ObjectDetectionModels"
author: "Luigi Cesarini"
date: 2025-01-06
tags: ['Exposure modelling', ' Object-detection', ' Transmission tower', ' OpenStreetMap', ' Street-level Imagery']
---

Exposure modelling plays a crucial role in disaster risk assessments by providing geospatial information about assets at risk and their characteristics. Detailed exposure data enhances the spatial representation of a rapidly changing environment, enabling decision-makers to develop effective policies for reducing disaster risk. This work proposes and demonstrates a methodology linking volunteered geographic information from OpenStreetMap (OSM), street-level imagery from Google Street View (GSV), and deep learning object detection models into the automated creation of exposure datasets for power grid transmission towers, assets particularly vulnerable to strong wind and other perils. Specifically, the methodology is implemented through a start-to-end pipeline that starts from the locations of transmission towers derived from OSM data to obtain GSV images capturing the towers in a given region, based on which their relevant features for risk assessment purposes are determined using two families of object detection models, i.e., single-stage and two-stage detectors. Both models adopted herein, You Only Look Once version 5 (YOLOv5) and Detectron2, achieved high values of mean average precision (mAP) for the identification and the classification tasks when applied to a pilot study area in northern Portugal comprising approximately 5.800 towers, highlighting the potential of the approach for large-scale exposure modelling of transmission towers. By investigating the skill of the models in detecting towers of various sizes in the images, Detectron2 was found to outperform YOLOv5 in most metrics. The Detectron2 two-stage detector also exhibited higher confidence in its detection on a larger part of the study area.

暴露建模通过提供有关风险资产及其特征的地理空间信息，在灾害风险评估中发挥着关键作用。详细的暴露数据增强了快速变化环境的空间表征能力，使决策者能够制定有效的减灾政策。本研究提出并演示了一种方法，将OpenStreetMap（OSM）的志愿地理信息、Google街景（GSV）的街道级图像与深度学习目标检测模型相结合，自动创建针对输电铁塔（这种极易受强风等灾害影响的资产）的暴露数据集。具体而言，该方法通过端到端流程实现：从OSM数据获取的输电铁塔位置出发，采集目标区域内包含铁塔的GSV图像，随后使用两类目标检测模型（单阶段检测器与两阶段检测器）确定其风险评估相关特征。在葡萄牙北部约5,800座铁塔的试点研究中，采用的YOLOv5和Detectron2模型在识别分类任务中均取得较高的平均精度均值（mAP），证明了该方法在大规模输电铁塔暴露建模中的潜力。通过评估模型检测不同尺寸铁塔的表现，发现Detectron2在多数指标上优于YOLOv5。两阶段检测器Detectron2还在研究区更大范围内表现出更高的检测置信度。

资源链接: [Exposure Modelling of Transmission Towers for Large-Scale Natural HazardRiskAssessments Based on Deep-Learning ObjectDetectionModels](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5084497)
