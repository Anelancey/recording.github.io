import pandas as pd
import os


politician_metadata = pd.read_json(
    r'E:\Communication\historical-users-filtered-formatted.json'
)

politician_metadata_flat = pd.concat([politician_metadata.explode('accounts').reset_index(drop=True).drop(columns='accounts'), 
                     pd.json_normalize(politician_metadata.explode('accounts')['accounts'].reset_index(drop=True))], axis=1)


#save path and name
output_folder = r'E:\Communication\concat_congressmeta'
os.makedirs(output_folder, exist_ok=True)

csv_path = os.path.join(output_folder, 'politician_metadata_flat.csv')

# save as csv and json
politician_metadata_flat.to_csv(csv_path, index=False)

#json_path = os.path.join(output_folder, 'politician_metadata_flat.json')
#politician_metadata_flat.to_json(json_path, orient='records', lines=True)

#print(f"文件已保存到 {csv_path} 和 {json_path}")