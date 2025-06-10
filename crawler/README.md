数据侧，先运行
```
python step1_data.py ## 结果存储在 outputs/ssrn_details.csv
```

论文侧，先运行
```
python step1_paper.py ## 结果存储在 outputs/ssrn_search_results.csv
python step2_paper.py ## 结果存储在 outputs/ssrn_details.csv
```

论文解释
```
python step3_interpretation.py --source ssrn ## 论文
python step3_interpretation.py --source sciencedb ## 数据
```

上述程序结束后，运行
```
python step4_convert.py --source ssrn ## 论文
python step4_convert.py --source sciencedb ## 数据
```

最终结果存储在outputs/markdown_files