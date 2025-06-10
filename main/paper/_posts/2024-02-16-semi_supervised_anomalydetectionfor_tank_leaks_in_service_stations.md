---
layout: post
categories: paper
title: "Semi-Supervised AnomalyDetectionfor Tank Leaks in Service Stations"
author: "Li Chik"
date: 2024-02-16
tags: ['Fuel loss detection', ' Tank leak detection', ' Semi-supervised anomaly detection', ' Autoencoder']
---

Service station poses a significant risk to the surrounding environment and community due to the possibility of a fuel leak. Current practice for fuel loss detection in the underground storage system relies on traditional statistical regression models to analyse the daily data. However, these models are typically sensitive to the quality of the collected data, and it is also difficult to pinpoint the source of the problem as they could be in any part of the storage system. This study extends semi-supervised anomaly detection methods for tank leak detection by analysing the idle state of the storage system instead of all different possible states (to reduce unnecessary complexity) as in the daily data. The idle state dataset is able achieve a similar level of true positive rate compared to the daily data under settings in practise, while reducing the false positive rates (37% to 23%) and time to detection (50 to 30 days). Furthermore, both statistically based and deep learning based semi-supervised anomaly detection models are compared with the traditional statistical regression model for tank leak detection under various leak simulation scenarios. Under the optimal setting, both semi-supervised anomaly detection models can consistently achieve a higher true positive rate at lower false positive rates (≤23%) compared to the model used in the industry. Finally, the study also discusses the practical aspects that must be considered in selecting the datasets and models for real-world applications, such as cost, data quality and model interpretability.

加油站因可能发生燃油泄漏而对周边环境和社区构成重大风险。目前地下储油系统的燃油泄漏检测主要依赖传统统计回归模型分析日常数据。然而这些模型通常对数据质量敏感，且难以精确定位问题源头——泄漏可能发生在储油系统的任何部位。本研究通过分析储油系统闲置状态（而非日常数据中所有可能状态，以降低不必要的复杂性），将半监督异常检测方法扩展应用于油罐泄漏检测。实践表明，闲置状态数据集在保持相近真实阳性率的同时，能将误报率从37%降至23%，并将检测时间从50天缩短至30天。此外，研究对比了基于统计和深度学习的半监督异常检测模型与传统统计回归模型在不同泄漏模拟场景下的表现。在最优设置下，两种半监督模型的真实阳性率均优于行业现行模型，且误报率始终低于23%。最后，研究还探讨了实际应用中数据集和模型选择需考虑的成本、数据质量及模型可解释性等现实因素。

资源链接: [Semi-Supervised AnomalyDetectionfor Tank Leaks in Service Stations](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4729311)
