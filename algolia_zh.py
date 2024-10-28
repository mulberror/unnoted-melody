from algoliasearch.search_client import SearchClient
import json

client = SearchClient.create('MXP1WFVWGE', '2eb8acc230f7fde7375935e999726a22')
index = client.init_index('zh_index')

with open('./public/index.json', 'r') as f:
    data = json.load(f)

index.save_object(data)

print('index.json导入成功')