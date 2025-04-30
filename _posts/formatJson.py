import json
import os

# 设置输入和输出路径
input_path = r'E:\Communication\congresstweets-master\data\2017-06-21.json'
output_folder = r'E:\Communication'
output_file = os.path.join(output_folder, '2017-06-21-formatted.json')

# 读入原 JSON
with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 写出新的 JSON，缩进4格
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"已经导出格式化的JSON到 {output_file}")
