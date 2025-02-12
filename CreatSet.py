
import pandas as pd

# 读取 TSV 文件
df = pd.read_csv("Lexique383.tsv", delimiter="\t", encoding="utf-8")

# 提取单词列并转换为 set
french_words = set(df["ortho"])

