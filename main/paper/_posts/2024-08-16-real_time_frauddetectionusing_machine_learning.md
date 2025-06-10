---
layout: post
categories: paper
title: "Real-Time FraudDetectionUsing Machine Learning"
author: "Benjamin Borketey"
date: 2024-08-16
tags: ['Credit Card', ' Fraud Detection', ' Machine Learning', ' SHAP Values', ' Random Forest']
---

Credit card fraud remains a significant challenge, with financial losses and consumer protection at stake. This study addresses the need for practical, real-time fraud detection methodologies. Using a Kaggle credit card dataset, I tackle class imbalance using the Synthetic Minority Oversampling Technique (SMOTE) to enhance modeling efficiency. I compare several machine learning algorithms, including Logistic Regression, Linear Discriminant Analysis, K-nearest Neighbors, Classification and Regression Tree, Naive Bayes, Support Vector, Random Forest, XGBoost, and Light Gradient-Boosting Machine to classify transactions as fraud or genuine. Rigorous evaluation metrics, such as AUC, PRAUC, F1, KS, Recall, and Precision, identify the Random Forest as the best performer in detecting fraudulent activities. The Random Forest model successfully identifies approximately 92% of transactions scoring 90 and above as fraudulent, equating to a detection rate of over 70% for all fraudulent transactions in the test dataset. Moreover, the model captures more than half of the fraud in each bin of the test dataset. SHAP values provide model explainability, with the SHAP summary plot highlighting the global importance of individual features, such as "V12" and "V14". SHAP force plots offer local interpretability, revealing the impact of specific features on individual predictions. This study demonstrates the potential of machine learning, particularly the Random Forest model, for real-time credit card fraud detection, offering a promising approach to mitigate financial losses and protect consumers.

信用卡欺诈仍是一个重大挑战，涉及财务损失与消费者权益保护问题。本研究针对实时欺诈检测方法的实际需求展开。通过使用Kaggle信用卡数据集，我采用合成少数类过采样技术（SMOTE）解决类别不平衡问题以提升建模效率。我比较了多种机器学习算法，包括逻辑回归、线性判别分析、K近邻算法、分类回归树、朴素贝叶斯、支持向量机、随机森林、XGBoost和轻量梯度提升机，用于区分欺诈交易与正常交易。通过AUC、PRAUC、F1值、KS统计量、召回率与精确度等严格评估指标，确定随机森林在欺诈活动检测中表现最优。该模型成功识别出约92%评分90及以上的交易为欺诈交易，相当于对测试数据集中全部欺诈交易的检测率超过70%。此外，模型在每个数据分箱中捕获了超半数欺诈案例。SHAP值提供了模型可解释性，其摘要图凸显了"V12"和"V14"等特征的整体重要性，而作用力图则通过特定特征对个体预测的影响实现了局部解释。本研究证明了机器学习（尤其是随机森林模型）在实时信用卡欺诈检测中的潜力，为减少财务损失和保护消费者提供了一种有效方案。

资源链接: [Real-Time FraudDetectionUsing Machine Learning](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4895921)
