import pandas as pd

# 1. 读取CSV文件
# 假设CSV文件名为'example.csv'，并且它位于当前工作目录中
df = pd.read_csv('./csv/intro_job_1.csv',encoding="GB2312")
print(df.head())