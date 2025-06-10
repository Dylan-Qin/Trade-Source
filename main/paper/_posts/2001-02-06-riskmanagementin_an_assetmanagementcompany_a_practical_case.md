---
layout: post
categories: paper
title: "RiskManagementin an AssetManagementCompany: A Practical Case"
author: "Dario Brandolini"
date: 2001-02-06
tags: ['Risk management', ' asset management', ' implementation', ' bootstrap', ' historical simulation']
---

The article concerns the differences between the meaning of risk management in a bank and in an asset management company, and then it illustrates the solution found to the challenge of building up a risk management system in an Italian medium size company. We describe the specific needs of an asset management company, in terms of proper financial modelling, time and resources constraints, given that an investment company: - manages "third party funds" (eventual losses are not its liabilities); - has a relatively long investment horizon, if compared to other market participants; - often monitors relative risk, rather than absolute risk. As models for estimating portfolio risk on medium-long horizons are crucial, and the related theoretical problems are absolutely not trivial, we briefly describe the model we use. It is based on bootstrapping, that allows us to calculate several risk measures for a large number of portfolios. It allows us to simulate medium-term to long-term financial scenarios, without imposing any particular probability function, taking into account heteroscedasticity, serial correlation, and any existing market views. We shortly describe the implementation, with  some details on the database and the calculation engine (both available on the market). This kind of system is more straightforward and cheaper to implement than traditional, bank-oriented risk systems: it  took less than one year to implement the whole tool, with limited costs (basically some cheap licences and the work of two quants). We hope that our experience could be of help to other asset management companies.

本文探讨了银行与资产管理公司在风险管理含义上的差异，并阐述了为一家意大利中型公司构建风险管理体系时所找到的解决方案。我们描述了资产管理公司在适当金融建模、时间和资源限制方面的特定需求，考虑到投资公司具有以下特点：管理"第三方资金"（潜在损失不构成其负债）；相较于其他市场参与者拥有相对较长的投资期限；通常监测相对风险而非绝对风险。鉴于中长期投资组合风险评估模型至关重要且相关理论问题绝非简单，我们简要介绍了所采用的基于自助法的模型。该模型能计算大量投资组合的多项风险指标，模拟中长期金融场景，无需设定特定概率函数，同时考虑异方差性、序列相关性及现有市场观点。我们简述了系统实施过程，包括数据库与计算引擎（均为市售产品）的若干细节。此类系统比传统银行导向的风险系统更易实施且成本更低：整套工具开发耗时不足一年，成本有限（主要为廉价许可证和两名量化分析师的投入）。希望我们的经验能为其他资产管理公司提供参考。

资源链接: [RiskManagementin an AssetManagementCompany: A Practical Case](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=252294)
