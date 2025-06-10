---
layout: post
categories: paper
title: "COPOD: Copula-Based OutlierDetection"
author: "Zheng Li"
date: 2021-03-22
tags: ['Outlier Detection', ' Anomaly Detection', ' Fraud Detection', ' Copula', ' Risk Management']
---

Outlier detection refers to the identification of rare items that are deviant from the general data distribution. Existing approaches suffer from high computational complexity, low predictive capability, and limited interpretability. As a remedy, we present a novel outlier detection algorithm called COPOD, which is inspired by copulas for modeling multivariate data distribution. COPOD first constructs an empirical copula, and then uses it to predict tail probabilities of each given data point to determine its level of "extremeness". Intuitively, we think of this as calculating an anomalous p-value. This makes COPOD both parameter-free, highly interpretable, and computationally efficient. In this work, we make three key contributions, 1) propose a novel, parameter-free outlier detection algorithm with both great performance and interpretability, 2) perform extensive experiments on 30 benchmark datasets to show that COPOD outperforms in most cases and is also one of the fastest algorithms, and 3) release an easy-to-use Python implementation for reproducibility.

异常值检测指的是识别偏离一般数据分布的罕见项。现有方法存在计算复杂度高、预测能力弱及可解释性有限的问题。为此，我们提出一种名为COPOD的新型异常检测算法，其灵感源自用于建模多元数据分布的copula理论。COPOD首先构建经验copula，随后利用其预测每个给定数据点的尾部概率以确定其"极端程度"。直观而言，这类似于计算异常p值。该方法使COPOD兼具无需参数设定、强可解释性和高效计算的特点。本研究作出三项关键贡献：1）提出兼具优异性能与可解释性的新型无参数异常检测算法；2）在30个基准数据集上开展大量实验，表明COPOD在多数情况下性能优越且属于最快算法之一；3）发布易于使用的Python实现以确保可复现性。

资源链接: [COPOD: Copula-Based OutlierDetection](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3801322)
