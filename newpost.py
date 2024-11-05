import os
import argparse
import shutil

# python3 blog createPost <name> [-e]
# 创建一篇文章
def newpost(en_name, year, season):
    post_name = en_name
    path = f"posts/{year}/{season}/{post_name}"
    os.system(f"hugo new {path}/{post_name}.md")
    os.rename(f"./content/{path}/{post_name}.md", f"./content/{path}/index.zh-cn.md")

    shutil.copy(f"./content/{path}/index.zh-cn.md", f"./content/{path}/index.en.md")
    os.makedirs(f"./content/{path}/img/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("en_name")
    parser.add_argument("year")
    parser.add_argument("season")

    args = parser.parse_args()
    newpost(args.en_name, args.year, args.season)
