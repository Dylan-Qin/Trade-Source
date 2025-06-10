---
layout: post
categories: data
title: "Network pharmacology data"
author: "Xu Yi"
date: 2025-04-03
tags: ['DBW', ' TCMSP', ' 口服生物利用度', ' OB', ' 药物相似度', ' DL', ' PubChem', ' Swiss Target Prediction', ' Genecards', ' OMIM', ' Ulcerative colitis', ' Uniprot', ' Venn', ' String', ' 蛋白质-蛋白质相互作用', ' PPI', ' Cytoscape', ' Metascape', ' 基因本体论', ' GO', ' 京都基因与基因组百科全书', ' KEGG']
---

DBW 主要活性化合物的数据来自 TCMSP 数据库 （https://old.tcmsp-e.com/tcmsp.php），成分筛选标准为口服生物利用度 （OB） ≥30% 和药物相似度 （DL） ≥0.18。通过将 DBW 的经典 SMILES 从 PubChem 数据库 （https://pubchem.ncbi.nlm.nih.gov/） 导入 Swiss Target Prediction 数据库 （http://swisstargetprediction.ch/） 来鉴定 DBW 的主要活性化合物，以寻找潜在靶标。接下来，我们从 Genecards 数据库 （https://www.genecards.org/） 和 OMIM 数据库 （https://www.omim.org/） 收集了关键词为 “Ulcerative colitis” 的结肠炎相关蛋白，然后使用 Uniprot 数据库 （https://www.uniprot.org/） 将所有靶标翻译成基因符号。我们整合了化合物和 UC 疾病的潜在靶点，并使用 Venn 工具 （htt ps://bioinfogp.cnb.csic.es/tools/venny/） 分析了常见靶点。随后，我们使用 String 数据库 （https://cn.string-db.org/） 构建了一个蛋白质\u2012蛋白质相互作用 （PPI） 网络，仅限于“智人”，并使用 Cytoscape 软件 （3.9.1） 可视化了该网络。最后，对 Metascape 数据库 （https://metascape.org/gp/index.html） 中的关键靶点进行基因本体论 （GO） 和京都基因与基因组百科全书 （KEGG） 分析，并将结果绘制在可视化平台 （http://www.bioinformatics.com.cn/） 上。

DBW主要活性化合物的数据来自TCMSP数据库（https://old.tcmsp-e.com/tcmsp.php），成分筛选标准为口服生物利用度（OB）≥30%和药物相似度（DL）≥0.18。通过将DBW的经典SMILES从PubChem数据库（https://pubchem.ncbi.nlm.nih.gov/）导入Swiss Target Prediction数据库（http://swisstargetprediction.ch/）来鉴定DBW的主要活性化合物，以寻找潜在靶标。接下来，我们从Genecards数据库（https://www.genecards.org/）和OMIM数据库（https://www.omim.org/）收集了关键词为“Ulcerative colitis”的结肠炎相关蛋白，然后使用Uniprot数据库（https://www.uniprot.org/）将所有靶标翻译成基因符号。我们整合了化合物和UC疾病的潜在靶点，并使用Venn工具（https://bioinfogp.cnb.csic.es/tools/venny/）分析了常见靶点。随后，我们使用String数据库（https://cn.string-db.org/）构建了一个蛋白质-蛋白质相互作用（PPI）网络，仅限于“智人”，并使用Cytoscape软件（3.9.1）可视化了该网络。最后，对Metascape数据库（https://metascape.org/gp/index.html）中的关键靶点进行基因本体论（GO）和京都基因与基因组百科全书（KEGG）分析，并将结果绘制在可视化平台（http://www.bioinformatics.com.cn/）上。

资源链接: [Network pharmacology data](https://doi.org/10.57760/sciencedb.22955)
