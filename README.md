```bash
hugo serve --disableFastRender -e production --buildDrafts
```

## 工作流
```bash
hugo serve --disableFastRender -e production
# 上传 index.json 文件到 algolia
python3 algolia.py
# 更新本人主题配置
cd ./themes/FixIt/
git add .
git commit -m "fix: update config of theme"
git push -u origin main
cd ../..
# 上传网站文件

```