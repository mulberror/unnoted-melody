from PIL import Image
import argparse
import os

def trans(name):
    path = f"./static/img/posts/{name}"
    for filename in os.listdir(path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(path, filename)
            img = Image.open(img_path)
            output_path = os.path.join(path, f"{os.path.splitext(filename)[0]}.webp")
            img.save(output_path, 'webp')
            print(f"已转换: {filename} -> {output_path}")
            os.remove(img_path)
    
    print("所有图片已转换并删除原文件。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    trans(args.name)
