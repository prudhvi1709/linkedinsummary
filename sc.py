import pandas as pd
import json
df = pd.read_excel('demos-full.xlsx')
json_data = df.to_json(orient='records')
with open('data.json', 'w') as json_file:
    json.dump(json.loads(json_data), json_file)