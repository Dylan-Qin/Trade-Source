---
layout: post
categories: paper
title: "OutlierDetectionin TARGET2RiskIndicators"
author: "Ronald Heijmans"
date: 2019-02-12
tags: ['risk indicator', ' TARGET2', ' financial market infrastructure', ' extrem value theory (EVT)', ' local outlier factor (LOF)', ' anomaly']
---

This paper studies the detection of outliers in risk indicators based on large value payment system transaction data. The ten risk indicators are daily time series measuring various risks in the large value payment system, such as operational risk, concentration risk and liquidity flows related to other financial market infrastructures. We use extreme value theory and local outlier factor methods to identify anomalous data points (outliers). In a univariate setup, the extreme value analysis quantifies the unusualness of each outlier. In a multivariate setup, the local outlier factor method identifies outliers by measuring the local deviation of a given data point with respect to its neighbours. We find that most detected outliers are at the beginning and near end of the calendar month when turnover is significantly larger than at other days. Our method can be used e.g. by overseers and financial stability experts who wish to look at many (risk) indicators in relation to each other.

本文研究基于大额支付系统交易数据的风险指标异常值检测。这十个风险指标是衡量大额支付系统中各类风险的日度时间序列，包括操作风险、集中度风险以及与其他金融市场基础设施相关的流动性流动等。我们运用极值理论和局部离群因子方法来识别异常数据点（离群值）。在单变量分析框架下，极值分析量化了每个离群值的异常程度；在多变量分析框架下，局部离群因子方法通过测量给定数据点相对于其邻近点的局部偏差来识别离群值。研究发现，大多数被检测到的离群值出现在日历月初和临近月末时点，这些时点的交易量显著高于其他日期。本方法可供监管者和金融稳定专家使用，尤其适用于需要关联分析多个（风险）指标的场景。

资源链接: [OutlierDetectionin TARGET2RiskIndicators](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3332441)
