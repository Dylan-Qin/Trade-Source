---
layout: post
categories: data
title: "FAIR Data Reuse – the Path through Data Citation"
author: "Paul Groth, Helena Cousijn, Tim Clark, Carole Goble"
date: 2020-10-17
tags: ['FAIR guiding principles', ' data reuse', ' machine readable metadata', ' data providers', ' provenance metadata', ' shared vocabularies', ' existing data sets', ' data citation', ' persistent identifiers', ' unique identifiers', ' metadata', ' FAIR data reuse', ' DataCite metadata']
---

Two figures of this paper. One of the key goals of the FAIR guiding principles is defined by its final principle – to optimize data sets for reuse by both humans and machines. To do so, data providers need to implement and support consistent machine readable metadata to describe their data sets. This can seem like a daunting task for data providers, whether it is determining what level of detail should be provided in the provenance metadata or figuring out what common shared vocabularies should be used. Additionally, for existing data sets it is often unclear what steps should be taken to enable maximal, appropriate reuse. Data citation already plays an important role in making data findable and accessible, providing persistent and unique identifiers plus metadata on over 16 million data sets. In this paper, we discuss how data citation and its underlying infrastructures, in particular associated metadata, provide an important pathway for enabling FAIR data reuse. Figure 1 shows an example data citation. Figure 2 shows an example DataCite metadata.

本文的两张图。FAIR指导原则的一个关键目标由其最终原则定义——优化数据集以供人类和机器重复使用。为此，数据提供者需要实施并支持一致的机器可读元数据来描述其数据集。这对数据提供者来说可能是一项艰巨的任务，无论是确定来源元数据应提供的详细程度，还是弄清楚应使用哪些通用共享词汇表。此外，对于现有数据集，通常不清楚应采取哪些步骤来实现最大限度的适当重用。数据引用在使数据可查找和可访问方面已经发挥了重要作用，为超过1600万个数据集提供了持久且唯一的标识符以及元数据。在本文中，我们讨论了数据引用及其底层基础设施（特别是相关元数据）如何为实现FAIR数据重用提供重要途径。图1展示了一个数据引用示例。图2展示了一个DataCite元数据示例。

### 研究目的  
本文旨在探讨数据引用（Data Citation）及其底层元数据基础设施如何支持FAIR（可查找、可访问、可互操作、可重用）原则的实现，尤其是优化数据集的重复使用。重点解决数据提供者在实施机器可读元数据时面临的挑战，并提出通过数据引用促进数据重用的具体路径。

### 研究方法  
1. **理论分析**：基于FAIR原则框架，分析数据重用的关键障碍（如元数据标准化不足、共享词汇表缺失）。  
2. **案例研究**：通过数据引用实例（图1）和DataCite元数据示例（图2），展示现有基础设施如何提供持久标识符和结构化元数据。  
3. **功能映射**：将数据引用的核心组件（如唯一标识符、元数据字段）与FAIR原则的具体要求进行匹配，论证其支持数据重用的机制。  

### 核心观点  
1. **数据引用是FAIR实现的关键路径**：通过提供持久标识符和标准化元数据，数据引用直接满足FAIR中“可查找”和“可访问”要求，并为“可互操作”和“可重用”奠定基础。  
2. **元数据标准化挑战**：数据提供者需平衡元数据详细度与实用性，采用通用词汇表（如DataCite Schema）可降低实施难度。  
3. **基础设施的杠杆作用**：现有数据引用系统（如DataCite）已覆盖1600万数据集，证明其规模化支持FAIR的潜力。  

### 创新点  
1. **实践导向的FAIR路径**：将抽象原则转化为具体操作方案，强调数据引用作为现成工具的可行性。  
2. **元数据与重用关联性**：揭示数据引用元数据（如作者、许可信息）如何直接影响重用决策，填补FAIR落地研究的空白。  

### 潜在影响  
1. **推动数据共享文化**：为数据提供者提供明确的技术路线，降低FAIR合规成本。  
2. **促进跨领域协作**：标准化引用机制可增强学科间数据互操作性，加速科学发现。  
3. **激励长期数据管理**：通过引用提升数据可见性和学术影响力，形成数据共享的正向循环。  

### 图表补充说明  
- **图1（数据引用示例）**：展示典型引用格式，包括DOI、创作者、出版时间等核心元数据，体现机器可读性。  
- **图2（DataCite元数据示例）**：呈现结构化字段（如标题、描述、许可协议），验证其与FAIR元数据要求的兼容性。  

（注：因原文未提供图表细节，解读基于描述性内容归纳。）

资源链接: [FAIR Data Reuse – the Path through Data Citation](https://doi.org/10.11922/sciencedb.j00104.00069)
