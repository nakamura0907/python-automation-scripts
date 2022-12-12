import argparse
import img2pdf
import os
from PIL import Image

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    allowed_extensions = ["jpg", "jpeg", "png", "gif"]
    
    # コマンドライン引数
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input", "-i", help="画像の入力先ディレクトリ（デフォルト: image-to-pdf/assets/）", default=path + "/../assets/")
    parser.add_argument("--output", "-o", help="PDFの出力先ディレクトリ（デフォルト: image-to-pdf/dist/）", default=path + "/../dist/")
    parser.add_argument("--filename", "-f", help="PDFのファイル名（デフォルト: output）", default="output")

    args = parser.parse_args()

    # PDFの出力
    with open(args.output + args.filename + ".pdf" , "wb") as f:
        images = [Image.open(args.input + img).filename for img in os.listdir(args.input) if img.endswith(tuple(allowed_extensions))]
        
        if len(images) == 0:
            print("画像が見つかりませんでした")
            exit(1)
            
        images.sort()
        pdf = img2pdf.convert(images)
        f.write(pdf)