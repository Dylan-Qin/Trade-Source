---
layout: post
categories: paper
title: "A Gradient Descent-Ascent Method for Continuous-TimeRisk-Averse OptimalControl"
author: "Gabriel Velho"
date: 2023-09-30
tags: ['Gradient descent-ascent', ' Coherent risk measures', ' Stochastic optimal control', ' Non-linear Control', ' Risk-averse control']
---

In this paper, we consider continuous-time stochastic optimal control problems where the cost is evaluated through a coherent risk measure. We provide an explicit gradient descent-ascent algorithm which applies to problems subject to non-linear stochastic differential equations. More specifically, we leverage duality properties of coherent risk measures to relax the problem via a smooth min-max reformulation which induces artificial strong concavity in the max subproblem. We then formulate necessary conditions of optimality for this relaxed problem which we leverage to prove convergence of the gradient descent-ascent algorithm to candidate solutions of the original problem. Finally, we showcase the efficiency of our algorithm through numerical simulations involving trajectory tracking problems and highlight the benefit of favoring risk measures over classical expectation.

本文研究了连续时间随机最优控制问题，其成本通过一致性风险度量进行评估。我们提出了一种显式的梯度下降-上升算法，适用于受非线性随机微分方程约束的问题。具体而言，我们利用一致性风险度量的对偶特性，通过平滑的极小-极大重构来松弛原问题，从而在极大子问题中引入人工强凹性。随后，我们为该松弛问题建立了最优性必要条件，并借此证明梯度下降-上升算法能收敛至原问题的候选解。最后，我们通过轨迹跟踪问题的数值模拟验证了算法的有效性，并突显了采用风险度量相较于传统期望准则的优势。

资源链接: [A Gradient Descent-Ascent Method for Continuous-TimeRisk-Averse OptimalControl](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4588364)
