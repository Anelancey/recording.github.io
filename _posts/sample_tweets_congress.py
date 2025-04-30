import pandas as pd
import os
import csv
import json


# Path to the folder containing JSON files
politician_data_path = r'E:\Communication\congresstweets-master\data'
'''
# List all files (not just .json) in the folder
politician_all_files = [os.path.join(politician_data_path, f) 
                        for f in os.listdir(politician_data_path) 
                        if os.path.isfile(os.path.join(politician_data_path, f))]

# Read and combine all JSON files safely
politician_df_list = []
for file in politician_all_files:
    try:
        df = pd.read_json(file)
        politician_df_list.append(df)
    except Exception as e:
        print(f"Skipping {file}: {e}")

# Combine into one DataFrame
politician_df = pd.concat(politician_df_list, ignore_index=True)

#save to csv
politician_df.to_csv(r'E:\Communication\concat_congressmeta\all_politician_df.csv', index=False)
print('save file succes')

'''
'''
politician_metadata_flat10=pd.read_csv(r'E:\Communication\concat_congressmeta\all_politician_df.csv')
print("\n所有列名:")
print(politician_metadata_flat.columns.tolist())
print(politician_metadata_flat10.head(10))

#save to csv
#politician_metadata_flat10.head(10).to_csv(r'E:\Communication\concat_congressmeta\all_politician_df-10.csv', index=False)
#print('save file succes-10')
'''

# import politicians' metadata
politician_metadata = pd.read_json(
    r'E:\Communication\historical-users-filtered-formatted.json'
)

politician_metadata_flat = pd.concat([politician_metadata.explode('accounts').reset_index(drop=True).drop(columns='accounts'), 
                     pd.json_normalize(politician_metadata.explode('accounts')['accounts'].reset_index(drop=True))], axis=1)


#print("\n所有列名:")
#print(politician_metadata_flat.columns.tolist())
#print(politician_metadata_flat.head(10))

# 保存为CSV文件
output_dir = r'E:\Communication\concat_congressmeta'
csv_path = os.path.join(output_dir, 'historical-users_csv.csv')
politician_metadata_flat.to_csv(csv_path, index=False)

# 保存为JSON文件
json_path = os.path.join(output_dir, 'historical-users_json.json')
politician_metadata_flat.to_json(json_path, orient='records', indent=4)

print(f"已将平铺数据保存为CSV文件: {csv_path}")
print(f"已将平铺数据保存为JSON文件: {json_path}")