import argparse

if __name__ == '__main__':
    # コマンドライン引数
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", help="画像の入力先ディレクトリ", default="./../assets")
    parser.add_argument("--output", help="PDFの出力先ディレクトリ", default="./../dist")

    args = parser.parse_args()

    # PDFの出力

    print(args)
    print(args.output)
