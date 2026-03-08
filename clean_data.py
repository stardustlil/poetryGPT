import json
import re

def clean_text(content):
    # 1️⃣ 去换行 → 改成句子换行（更利于模型学习节奏）
    content = content.replace("\n", "")

    # 2️⃣ 去注释
    content = re.sub(r'[\[\(].*?[\]\)]', '', content)

    # 3️⃣ 统一标点（避免全角半角混乱）
    content = content.replace(",", "，")
    content = content.replace(".", "。")
    content = content.replace("?", "？")
    content = content.replace("!", "！")
    content = content.replace(":", "：")
    content = content.replace(";", "；")

    # 4️⃣ 按句号断句（帮助模型学习节奏）
    content = re.sub(r'([。！？])', r'\1\n', content)

    # 5️⃣ 去多余空行
    content = re.sub(r'\n+', '\n', content)

    return content.strip()


def clean_title(title):
    # 去掉词牌中的副标题（如 渡江云三犯·渡江云）
    title = title.split("·")[-1]
    return title.strip()


def build_sample(title, content):

    content = clean_text(content)
    title = clean_title(title)

    # 过滤异常数据
    if len(content) < 20:
        return None
    if len(content) > 600:
        return None

    return f"<START>\n词牌: {title}\n{content}\n<END>"


def clean_poetry_data(input_path, output_path):

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cleaned_entries = []

    for item in data:

        title = item.get("title", "").strip()
        content = item.get("content", "").strip()

        if not title or not content:
            continue

        sample = build_sample(title, content)

        if sample:
            cleaned_entries.append(sample)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(cleaned_entries))

    print(f"清洗完成！共处理 {len(cleaned_entries)} 首诗词。")


# 执行
clean_poetry_data('ci.song.json', 'input.txt')