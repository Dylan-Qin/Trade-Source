---
layout: post
categories: data
title: "The Open Data Challenge: An Analysis of 124,000 Data Availability Statements and an Ironic Lesson about Data Management Plans"
author: "Chris Graf, Dave Flanagan, Lisa Wylie , Deirdre Silver"
date: 2020-10-17
tags: ['paper', ' figures', ' data availability statements', ' submissions', ' LDA', ' pyLDAvis', ' topics', ' topic distribution', ' document/topic matrix', ' word/topic matrix', ' interactive plots', ' DOI']
---

Six figures of this paper. Figure 1 shows cumulative data availability statements (left) and approximate cumulative number of submissions (right) from August 2012 to October 2019. The number of data availability statements increased dramatically in the first half of 2019. Figure 2 is visualization of the topics estimated by the LDA using pyLDAvis. Interactive plots available at DOI: 10.22541/au.157253515.58528497. Figure 3 shows topic distribution by percentage. Interactive plots available at DOI: 10.22541/au.157253515.58528497. Figure 4 shows document/topic matrix for the first 50 documents in the data set. Topic weighting ranges from low (blue) to high (red). Interactive plots available at DOI: 10.22541/au.157253515.58528497. Figure 5 presents word/topic matrix for the 20 most popular overall words in the data set. Topic weighting ranges from low (blue) to high (red). Interactive plots available at DOI: 10.22541/au.157253515.58528497. Figure 6 shows growth of individual topics over time. Interactive plots available at DOI: 10.22541/au.157253515.58528497.

本文的六幅图示。图1展示了2012年8月至2019年10月期间累积数据可用性声明（左）与近似累计投稿数量（右）的变化趋势。2019年上半年数据可用性声明的数量急剧增长。图2为通过pyLDAvis实现的LDA主题估计可视化结果，交互式图表详见DOI: 10.22541/au.157253515.58528497。图3显示各主题占比分布，交互式图表详见同一DOI。图4呈现数据集中前50篇文献的主题分布矩阵，主题权重由低（蓝色）至高（红色）渐变，交互式图表详见该DOI。图5展示数据集中20个最常用词汇的主题关联矩阵，权重颜色梯度同前，交互式图表详见该DOI。图6反映各主题随时间演变的增长趋势，交互式图表详见该DOI。

### **论文解读：The Open Data Challenge**  

#### **1. 研究目的**  
本研究旨在分析124,000篇学术论文的**数据可用性声明（Data Availability Statements, DAS）**，探讨开放数据实践的发展趋势、主题分布及其管理问题，并揭示**数据管理计划（Data Management Plans, DMPs）**在实际执行中的局限性。  

#### **2. 研究方法**  
- **数据来源**：收集2012年8月至2019年10月期间124,000篇论文的DAS。  
- **趋势分析**（图1）：对比DAS数量与投稿量的增长趋势，观察开放数据政策的采纳情况。  
- **主题建模**（LDA模型，图2-6）：  
  - 使用**pyLDAvis**可视化主题结构（图2）。  
  - 分析各主题占比（图3）、文献-主题分布（图4）、词汇-主题关联（图5）及主题时间演变（图6）。  
- **交互式图表**：通过DOI链接提供动态分析工具，增强结果可探索性。  

#### **3. 核心观点**  
- **DAS的快速增长**（图1）：2019年上半年DAS数量激增，反映期刊开放数据政策的强化。  
- **主题分布特征**（图3-5）：  
  - 高频主题可能涉及数据存储、共享方式（如“repository”“supplementary materials”）或限制因素（如“restricted access”）。  
  - 词汇-主题关联揭示不同领域的数据管理偏好。  
- **时间演变**（图6）：部分主题（如开放存储）随时间增长显著，而受限数据主题可能稳定或下降。  
- **DMP的“讽刺性”问题**：尽管DMP被广泛提倡，但实际数据管理仍存在执行差距（如数据未真正开放或管理不规范）。  

#### **4. 创新点**  
- **大规模DAS分析**：首次对超12万篇论文的DAS进行系统性主题建模，揭示开放数据的实践模式。  
- **动态可视化工具**：通过交互式图表（图2-6）支持用户自主探索主题结构。  
- **批判性发现**：指出DMP的理论价值与实际效果的不匹配，推动对数据管理政策的反思。  

#### **5. 潜在影响**  
- **政策优化**：为期刊、资助机构改进数据共享政策提供实证依据。  
- **学术实践**：提示研究者重视数据管理的实质性执行，而非仅满足形式要求。  
- **技术工具**：LDA模型与可视化方法可为后续开放数据研究提供方法论参考。  

### **总结**  
该研究通过量化分析与主题建模，揭示了开放数据实践的进展与矛盾，尤其强调DMP的落实问题，对推动科学数据共享的规范化具有重要启示。

资源链接: [The Open Data Challenge: An Analysis of 124,000 Data Availability Statements and an Ironic Lesson about Data Management Plans](https://doi.org/10.11922/sciencedb.j00104.00064)
