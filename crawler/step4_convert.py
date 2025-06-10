import os
import json
import re
import argparse
from datetime import datetime
import pandas as pd
import string

import re
def contains_non_english(title: str) -> bool:
    """
    检查论文标题中是否包含非英文字符（不包括常见标点、数字、空格等）。
    
    参数:
        title (str): 论文标题
    
    返回:
        bool: 如果包含非英文字符，返回 True；否则返回 False
    """
    # 允许的字符：A-Z a-z 0-9 空格和常见标点符号
    allowed_chars = string.ascii_letters + string.digits + string.punctuation + " "
    
    for char in title:
        if char not in allowed_chars:
            return True  # 非英文字符（如汉字、韩文、俄文等）
    return False


def escape_special_chars(s: str) -> str:
    # 需要转义的字符映射表
    escape_map = {
        '\t': '\\t',
        '\r': '\\r',
        '\\': '\\\\',
        '\"': '\\\"',
        '&': '\\&',
    }

    # 构建转义函数
    def escape_char(c):
        return escape_map.get(c, c)

    # 替换每个字符
    return ''.join(escape_char(c) for c in s)


def slugify(text):
    """将标题转为下划线连接的小写文件名"""
    return re.sub(r'\W+', '_', text.strip()).lower().strip('_')

def format_date(raw_date):
    """统一提取 yyyy-mm-dd 格式"""
    try:
        return raw_date[:10]
    except:
        return "unknown-date"

def generate_markdown(entry, category):
    """生成 markdown 内容"""
    title = entry.get("title", "")
    link = entry.get("link", "")
    abstract_en = entry.get("abstract", "")
    abstract_zh = entry.get("ch_abstract", "")
    tags = entry.get("tags", "")
    author = entry.get("authors", "")
    affiliation = entry.get("affiliation", "")
    interpretation = entry.get("interpretation", "")

    date = format_date(entry.get("publish_date", "unknown-date"))

    md = f"""---
layout: post
categories: {category}
title: "{title}"
author: "{author}"
date: {date}
tags: {tags}
---

{abstract_en}

{abstract_zh}

{interpretation}

资源链接: [{title}]({link})
"""
    return md, date

def convert_to_markdown(source_type):
    if source_type == "sciencedb":
        input_path = "outputs/sciencedb_explanation.jsonl"
        output_dir = "outputs/markdown_files/data/_posts"
        category = "data"
    elif source_type == "ssrn":
        input_path = "outputs/ssrn_explanation.jsonl"
        output_dir = "outputs/markdown_files/paper/_posts"
        category = "paper"
    else:
        raise ValueError("source_type must be either 'sciencedb' or 'ssrn'.")

    os.makedirs(output_dir, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        origin_data = [json.loads(i) for i in f.readlines()]

    df = pd.DataFrame(origin_data)
    df = df.sort_values(['publish_date'], ascending=[False]).drop_duplicates('title')
    
    df = df[df['title'].apply(len)<args.limit_char_length]
    df = df[~df['title'].apply(contains_non_english)]
    for col in df.columns:
        df = df[df[col].apply(lambda x: type(x) == type(''))]
        if col in ['title', 'author']:
            df[col] = df[col].apply(lambda x: x.replace('"', "'"))
        if col == 'tags':
            df[col] = df[col].apply(lambda x: x.split(','))
            # df[col] = df[col].apply(lambda x: x.replace(':', ''))

    if args.source == "sciencedb":
        df = df[df['term'].apply(lambda x: 'trade' in x and 'data' in x)]
        df = df[df.apply(lambda x: len(re.findall(r'trade', x['abstract'])) > 0 or len(re.findall(r'数据管理|商业|贸易', x['interpretation'])) > 0, axis=1)]
    else:
        df = df[df['term'].apply(lambda x: 'trade' in x)]
        df = df[df['abstract'].apply(lambda x: 'trade' in x)]

    data = df.to_dict(orient='records')

    for entry in data:
        md_content, date = generate_markdown(entry, category)
        filename = f"{date}-{slugify(entry['title'])}.md"
        filepath = os.path.join(output_dir, filename)
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md_content)
            print(f"✅ Saved: {filename}")
        except Exception as e:
            print(f"❌ Failed: {filename}")

    print(f"✅✅✅✅✅✅ Saved: {len(data)} Files")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON papers to Markdown.")
    parser.add_argument("--source", choices=["sciencedb", "ssrn"], default='ssrn', help="Specify the source type: 'sciencedb' or 'ssrn'")
    parser.add_argument("--limit_char_length", default=80, type=int)
    args = parser.parse_args()

    convert_to_markdown(args.source)