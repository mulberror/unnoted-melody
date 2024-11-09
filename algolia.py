from algoliasearch.search_client import SearchClient
import json
import config.config as config

client = SearchClient.create(config.appid, config.adminid)

# 上传 zh-search.json
zh_index = client.init_index('zh_index')

with open("./public/search.json", encoding='utf-8') as f:
    zh_batch = json.load(f)

zh_index.save_objects(zh_batch, {'autoGenerateObjectIDIfNotExist': True})

print('zh/search.json 上传成功')

# 上传 en-search.json
en_index = client.init_index('en_index')
with open("./public/en/search.json", encoding='utf-8') as f:
    en_batch = json.load(f)
en_index.save_objects(en_batch, {'autoGenerateObjectIDIfNotExist': True})

print('en/search.json 上传成功')
