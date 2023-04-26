from PyPDF2 import PdfReader
import os
import pathlib

count=0
folder_path=r"C:\Users\aida\Desktop\EFL(LMO)\PDF\KNAスペイン\EFL-Spanish-KNA_CDt"

p = pathlib.Path(folder_path)

for path in p.glob("*.pdf"):
# PDFを読み込むNotImplementedErro
        reader = PdfReader(path)
# ページ数を取得する
        count=len(reader.pages)+count

print(count)