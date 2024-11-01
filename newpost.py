import os
import argparse
import shutil

# python3 blog createPost <name> [-e]
# 创建一篇文章
def newpost(en_name, enable_en=False):
    post_name = en_name
    os.system(f"hugo new posts/{post_name}/{post_name}.md")
    os.rename(f"./content/posts/{post_name}/{post_name}.md", f"./content/posts/{post_name}/index.zh-cn.md")

    if enable_en:
        shutil.copy(f"./content/posts/{post_name}/index.zh-cn.md", f"./content/posts/{post_name}/index.en.md")

    os.makedirs(f"./content/posts/{post_name}/img/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("en_name")
    parser.add_argument("-e", "--enable_english", help="create post in English", action="store_true")
    args = parser.parse_args()
    newpost(args.en_name, args.enable_english)
