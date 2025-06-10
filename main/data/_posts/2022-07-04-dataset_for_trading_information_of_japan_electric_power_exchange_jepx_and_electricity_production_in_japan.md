---
layout: post
categories: data
title: "Dataset for trading information of Japan Electric Power Exchange (JEPX) and electricity production in Japan"
author: "Teng Ma, Yimeng Du, Tao Xu, Wang Chen"
date: 2022-07-04
tags: ['Spot Market Data', ' JEPX', ' transaction volume', ' spot prices', ' Yen/kWh', ' hourly price data', ' Power Generation Data', ' electric power companies', ' nuclear', ' thermal', ' hydroelectric', ' geothermal', ' biomass', ' solar', ' wind', ' hydroelectric power', ' power transmission', ' Utilization and Forecast Data', ' utilization rate', ' power generation facilities', ' electricity demand forecast', ' Organization for Cross-regional Coordination of Transmission Operator']
---

Spot Market Data:The spot price data of nine regions in Japan were obtained from the homepage of the JEPX. The dataset includes (i) transaction volume (100 GWh) and (ii) spot prices (Yen/kWh) in each area. Hourly price data were calculated as the hourly spot price by the mean of each two-time interval value in 1 hour, according to the 48 products traded in each 30-minute time interval within a day.Power Generation Data:The energy generation data in the electricity sector were acquired from nine traditional electric power companies (Hokkaido EPCO, Tohoku EPCO, Tokyo EPCO, Chubu EPCO, Hokuriku EPCO, Kansai EPCO, Chugoku EPCO, Shikoku EPCO, and Kyushu EPCO).The dataset contains various electricity power sources, such as nuclear, thermal, inflow-type hydroelectric, geothermal, biomass, solar, wind, pump-storage-type hydroelectric power, and regional power transmission by cross-regional interconnected lines. All the generation data were organized as hour-level data for each day.Utilization and Forecast Data:The utilization rate of the respective power generation facilities and the electricity demand forecast datasets were obtained from the Organization for Cross-regional Coordination of Transmission Operator, Japan.

现货市场数据：日本九个地区的现货价格数据取自JEPX官网。该数据集包含（i）交易量（100吉瓦时）和（ii）各区域现货价格（日元/千瓦时）。根据每日48个30分钟时段交易产品，每小时价格数据通过取两个30分钟间隔值的平均值计算得出。发电数据：电力行业发电数据来自九家传统电力公司（北海道电力、东北电力、东京电力、中部电力、北陆电力、关西电力、中国电力、四国电力、九州电力）。数据集涵盖核电、火电、径流式水电、地热、生物质、太阳能、风电、抽水蓄能式水电及跨区域互联线路输送电力等多种电源类型。所有发电数据均按日整理为小时级数据。利用率与预测数据：各发电设施利用率及电力需求预测数据集取自日本跨地区输电运营商协调组织。

### 研究目的  
该论文旨在构建一个涵盖日本电力交易市场（JEPX）现货价格、发电量及利用率预测的综合数据集，为分析电力市场动态（如价格波动、供需关系）及可再生能源整合影响提供数据支持。

### 研究方法  
1. **数据来源**：  
   - **现货市场数据**：从JEPX官网获取九大区域的每小时现货价格（日元/千瓦时）和交易量（100吉瓦时），基于每日48个30分钟时段数据的平均值计算。  
   - **发电数据**：整合九家传统电力公司的每小时发电量，覆盖核电、火电、可再生能源（水电、地热、生物质、太阳能、风电）及跨区域输电数据。  
   - **利用率与预测数据**：采用日本跨地区输电运营商协调组织提供的设施利用率及需求预测数据。  

2. **数据处理**：  
   - 统一时间粒度至小时级，确保数据一致性。  
   - 多源数据关联，如价格与发电类型、区域间电力流动的匹配。

### 核心观点  
1. **数据全面性**：数据集首次系统整合了日本电力市场的交易价格、多能源发电量及供需预测，覆盖地域和电源类型的多样性。  
2. **市场分析价值**：通过小时级数据可揭示价格与发电结构（如可再生能源占比）的关联性，或区域间电力输送对价格的影响。  

### 创新点  
1. **多维度整合**：将交易市场数据与发电技术细节、需求预测结合，弥补了单一数据源的局限性。  
2. **时间分辨率优化**：小时级数据比传统日级数据更能捕捉电力市场的短期波动特征。  

### 潜在影响  
1. **学术研究**：支持电力市场建模、可再生能源经济性分析或政策效果模拟。  
2. **行业应用**：助力发电企业优化投标策略，或电网运营商平衡跨区域供需。  
3. **政策制定**：为日本电力市场改革（如碳定价、可再生能源激励）提供实证依据。  

（注：解读基于论文描述的数据集构建方法，未涉及具体实证结论。）

资源链接: [Dataset for trading information of Japan Electric Power Exchange (JEPX) and electricity production in Japan](https://doi.org/10.57760/sciencedb.01925)
