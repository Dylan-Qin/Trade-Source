---
layout: post
categories: data
title: "Algorithmic Trading in A-share and Stock Price Informativeness before Earnings Announcements"
author: "张小日, 孙芳芳, 叶强"
date: 2024-11-15
tags: ['dataset', ' algorithmic trading indicators', ' public companies', ' Shenzhen Stock Exchange', ' ChiNext', ' Shanghai Stock Exchange', ' STAR Market', ' 2017 to 2021', ' Cancel-to-Trade Ratio', ' CTR', ' Trade-to-Order Ratio', ' TOR', ' Average Trade Size', ' ATS', ' RESSET', ' high-frequency', ' intraday data']
---

The dataset includes the daily algorithmic trading indicators for public companies on the Shenzhen Stock Exchange's ChiNext and the Shanghai Stock Exchange's STAR Market from 2017 to 2021. These indicators are: Cancel-to-Trade Ratio (CTR), or the ratio of the daily number of cancellations to the total number of trades; Trade-to-Order Ratio (TOR), or the ratio of daily trading volume to total order volume; Average Trade Size (ATS), or the ratio of total trading volume to the total number of trades. Our date source comes from RESSET high-frequency intraday (minute-level) data.

该数据集包含2017年至2021年深圳证券交易所创业板和上海证券交易所科创板上市公司的每日算法交易指标。这些指标分别为：撤单成交比（CTR），即每日撤单笔数与总成交笔数之比；成交委托比（TOR），即每日成交量与总委托量之比；平均每笔成交股数（ATS），即总成交量与总成交笔数之比。我们的数据来源为锐思（RESSET）高频日内（分钟级）数据。

### 研究目的  
该论文旨在探究A股市场中算法交易对上市公司盈余公告前股价信息含量（price informativeness）的影响，揭示算法交易行为如何改变市场信息效率。研究聚焦于创业板和科创板，分析算法交易指标（如撤单成交比、成交委托比等）与股价信息含量之间的关联，为理解算法交易的市场效应提供实证依据。

### 研究方法  
1. **数据来源**：  
   - 使用2017—2021年深交所创业板和上交所科创板的分钟级高频数据（来自RESSET数据库）。  
   - 核心算法交易指标：  
     - **撤单成交比（CTR）**：反映撤单活跃度（撤单笔数/总成交笔数）。  
     - **成交委托比（TOR）**：衡量委托单的执行效率（成交量/总委托量）。  
     - **平均每笔成交股数（ATS）**：指示大额交易倾向（总成交量/总成交笔数）。  

2. **分析框架**：  
   - 采用面板回归模型，控制公司特征、市场波动等变量，检验算法交易指标与盈余公告前股价信息含量的关系。  
   - 可能辅以事件研究法，分析公告窗口期的异常收益或信息不对称程度变化。  

### 核心观点  
1. **算法交易与信息效率**：  
   - 高CTR可能预示算法交易者通过频繁撤单试探市场深度，加剧短期噪音，降低股价信息含量。  
   - 高TOR或表明委托单执行效率高，可能提升信息传递速度，增强股价对基本面信息的反映。  
   - ATS的上升可能反映机构大额交易主导，若伴随信息优势，或提高股价信息含量。  

2. **板块差异**：  
   - 创业板与科创板因投资者结构、涨跌幅限制不同，算法交易的影响可能存在异质性。  

### 创新点  
1. **指标选择**：  
   - 结合CTR、TOR、ATS多维度刻画算法交易行为，超越传统单一指标（如订单流）的分析。  
2. **研究场景**：  
   - 聚焦盈余公告前的关键窗口期，揭示算法交易对信息提前融入股价的动态影响。  
3. **市场背景**：  
   - 针对中国新兴的创业板和科创板，补充新兴市场算法交易研究的空白。  

### 潜在影响  
1. **学术价值**：  
   - 为市场微观结构理论提供新兴市场证据，丰富算法交易与信息效率关系的文献。  
2. **实践意义**：  
   - 对监管机构：提示高频撤单可能干扰信息效率，需优化订单管理规则（如撤单费用）。  
   - 对投资者：量化算法交易指标可作为信息环境变化的信号，辅助交易策略调整。  

### 总结  
该论文通过高频数据实证分析算法交易行为对A股信息效率的影响，核心贡献在于细分指标构建和新兴市场场景应用，结论可为监管与投资决策提供参考。

资源链接: [Algorithmic Trading in A-share and Stock Price Informativeness before Earnings Announcements](https://doi.org/10.57760/sciencedb.j00214.00069)
