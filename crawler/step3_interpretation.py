import os
import json
import argparse
import pandas as pd
from llm import ChatTranslateLLM
from tqdm import tqdm

translator = ChatTranslateLLM(temperature=0.3)

def convert_to_jsonl(source_type):
    # 路径设置
    if source_type == "sciencedb":
        input_path = "outputs/sciencedb_details.csv"
        output_path = "outputs/sciencedb_explanation.jsonl"
    elif source_type == "ssrn":
        input_path = "outputs/ssrn_details.csv"
        output_path = "outputs/ssrn_explanation.jsonl"
    else:
        raise ValueError("source_type must be either 'sciencedb' or 'ssrn'.")

    # 加载原始数据
    data = pd.read_csv(input_path)

    # 已处理条目集合（使用 title 和 ch_abstract 作为唯一标识）
    processed_ids = set()
    if os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    item = json.loads(line)
                    processed_ids.add((item['title'], item['ch_abstract']))
                except Exception:
                    continue  # 忽略损坏行

    # 打开文件用于追加写入
    output_file = open(output_path, 'a', encoding='utf-8')
    pbar = tqdm(data.iterrows(), total=len(data))

    for idx, row in pbar:
        row_key = (row['title'], row['ch_abstract'])
        if row_key in processed_ids:
            continue

        try:
            interpretation = translator.interpretation(row['title'], row['ch_abstract'])
        except Exception as e:
            interpretation = f"Error: {e}"

        # 构造输出字典
        new_row = row.to_dict()
        new_row['interpretation'] = interpretation

        # 写入 JSON 行并刷新
        json_line = json.dumps(new_row, ensure_ascii=False)
        output_file.write(json_line + '\n')
        output_file.flush()
        os.fsync(output_file.fileno())

        processed_ids.add(row_key)

    output_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert paper explanations to JSONL.")
    parser.add_argument("--source", choices=["sciencedb", "ssrn"], default='sciencedb',
                        help="Specify the source type: 'sciencedb' or 'ssrn'")
    args = parser.parse_args()

    convert_to_jsonl(args.source)