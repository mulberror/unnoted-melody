import os
import argparse
import shutil

# python3 blog createPost <name> [-e]
# 创建一篇文章
def newpost(en_name, zh_name, enable_en=False):
    post_name = en_name
    os.system(f"hugo new posts/{post_name}/{post_name}.md")
    os.rename(f"./content/posts/{post_name}/{post_name}.md", f"./content/posts/{post_name}/index.md")

    if enable_en:
        shutil.copy(f"./content/posts/{post_name}/index.md", f"./content/posts/{post_name}/index.en.md")

    # 替换标题
    with open(f"./content/posts/{post_name}/index.md", 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines[1] = f"""title: "{zh_name}"\n"""
    with open(f"./content/posts/{post_name}/index.md", 'w', encoding='utf-8') as file:
        file.writelines(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("en_name")
    parser.add_argument("zh_name")
    parser.add_argument("-e", "--enable_english", help="create post in English", action="store_true")
    args = parser.parse_args()
    newpost(args.en_name, args.zh_name, args.enable_english)