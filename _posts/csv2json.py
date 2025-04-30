import os
import csv
import json

input_root = r"E:\Communication\concat_congressmeta"
output_root = r"E:\Communication\concat_congressmeta"

for root, dirs, files in os.walk(input_root):
    for file in files:
        if file.endswith(".csv"):
            csv_path = os.path.join(root, file)

            relative_path = os.path.relpath(root, input_root)
            output_dir = os.path.join(output_root, relative_path)
            os.makedirs(output_dir, exist_ok=True)

            # 获取去掉扩展名的文件名
            filename_without_ext = os.path.splitext(file)[0]

            # 如果文件名以 "csv_" 开头，就替换成 "json_"
            if filename_without_ext.startswith("csv_"):
                new_filename = filename_without_ext.replace("csv_", "json_", 1) + ".json"
            else:
                new_filename = filename_without_ext + ".json"  # 不以csv_开头的，正常保存

            json_path = os.path.join(output_dir, new_filename)

            # 读取 CSV 转成 JSON
            with open(csv_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)

            with open(json_path, mode='w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"✔ Converted: {csv_path} → {json_path}")
