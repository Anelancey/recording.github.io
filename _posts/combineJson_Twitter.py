import os
import json
import pandas as pd

# 输入文件夹路径
folder_path = r"E:\Communication\data_twitter\data_twitter_json"

# 存放所有数据的列表
all_data = []

# 遍历文件夹下所有 JSON 文件
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    all_data.extend(data)
                elif isinstance(data, dict):
                    all_data.append(data)
            except json.JSONDecodeError:
                print(f"❌ Failed to parse: {filename}")

# === 保存为 CSV 表格 ===
df = pd.json_normalize(all_data)
output_csv = os.path.join(folder_path, "merged_all_json.csv")
df.to_csv(output_csv, index=False, encoding="utf-8-sig")
print(f"✅ CSV 保存成功: {output_csv}")

# === 保存为新的合并 JSON 文件 ===
output_json = os.path.join(folder_path, "data_twitter_merge.json")
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)
print(f"✅ JSON 合并成功: {output_json}")
