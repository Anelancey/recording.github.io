import os
import json
import pandas as pd
from datetime import datetime

# 设置文件夹路径
folder_path = r'E:\Communication\data_twitter\data_twitter_json'

# 初始化列表，保存每个文件的最早最晚时间
records = []

# 遍历文件夹下所有 JSON 文件
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        created_at_list = []

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)  # 一行一行读
                    if 'created_at' in item:
                        created_at_str = item['created_at']
                        created_at_time = datetime.strptime(created_at_str, "%a %b %d %H:%M:%S %z %Y")
                        created_at_list.append(created_at_time)
                except Exception as e:
                    print(f"FILE {filename} ERROR: {e}")
        
        # 如果这个文件有找到created_at
        if created_at_list:
            min_time = min(created_at_list)
            max_time = max(created_at_list)
            records.append({
                'filename': filename,
                'min_created_at': min_time.strftime('%Y-%m-%d %H:%M:%S %z'),
                'max_created_at': max_time.strftime('%Y-%m-%d %H:%M:%S %z')
            })
        else:
            print(f"FILE {filename} NO created_at ！")

# 把所有记录保存成CSV
if records:
    df = pd.DataFrame(records)
    output_path = r'E:\Communication\data_twitter\data_twitter_json\Twitter_date.csv'
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"save {output_path}")
else:
    print("NO created_at，NO CSV")
