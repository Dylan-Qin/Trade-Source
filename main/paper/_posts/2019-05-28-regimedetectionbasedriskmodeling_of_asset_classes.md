---
layout: post
categories: paper
title: "RegimeDetectionBasedRiskModeling of Asset Classes"
author: "Gaurav Chakravorty"
date: 2019-05-28
tags: ['Risk Targeting', ' Tactical Asset Allocation', ' Regime Detection', ' Risk Prediction', ' Portfolio Construction']
---

In this work, we have found a risk model that improves the performance of Risk Targeting. Risk Targeting in portfolio construction is implemented to improve capital utilization in growing markets and systematically step away from risk scenarios. However, the performance of risk targeting varies with different implementations of risk estimation. Risk Targeting using recent backward volatility estimates is the most popular risk targeting mechanism but it could not have anticipated a deep crisis like 2008 and it would hurt in range bound situations like the February 2018 drop and bounce back or the December 2018 drop and January 2019 bounce back. The drawbacks of recent volatility are that in such a risk model, short-term volatility is being used to detect a long-term risk event with and short term mean reversion effects are ignored .In this work, we will try to separate risk estimation into two risk models, a long-term risk model that predicts extreme risk scenarios based on macroeconomic data and a short-term risk model that adjusts risk based on short-term mean reversion effects. We then combine the output of the two risk models into a risk measure that enables a risk targeted allocation strategy to outperform static allocation in both crisis periods like 2008 and mean-reverting periods like 2018.Note that risk for a real-money investor is not an expectation of volatility but a measure of the probability  of losing money if one is allocated to that asset class. Hence, we try to forecast a risk value which, if interpreted as a probability of loss, outperforms a baseline estimate of risk.

在这项工作中，我们发现了一种能提升风险目标策略表现的风险模型。投资组合构建中的风险目标策略旨在提高增长市场中的资本利用率，并系统性规避风险情景。然而，不同风险估算方法会导致风险目标策略的表现存在差异。采用近期历史波动率估算的风险目标策略是最常见的机制，但它无法预见如2008年的深度危机，且在震荡行情中表现不佳——例如2018年2月暴跌反弹或2018年12月暴跌2019年1月反弹的情形。近期波动率模型的缺陷在于：此类模型使用短期波动率来检测长期风险事件，同时忽略了短期均值回归效应。本研究尝试将风险估算拆分为两个模型：基于宏观经济数据预测极端风险情景的长期风险模型，以及根据短期均值回归效应调整风险的短期风险模型。随后我们将两个模型的输出结果整合为统一风险指标，使得风险目标配置策略在2008年等危机时期和2018年等均值回归时期均能超越静态配置策略。需注意的是，对于实际资金投资者而言，风险并非波动率预期，而是配置该资产类别时发生亏损的概率度量。因此我们尝试预测的风险值若被解读为亏损概率，其表现需优于基线风险估计。

资源链接: [RegimeDetectionBasedRiskModeling of Asset Classes](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3376816)
