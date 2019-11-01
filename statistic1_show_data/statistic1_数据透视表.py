import pandas as pd
df = pd.read_excel('data/1_table2.xlsx')
# print(df)
# 数据透视表
# df1 = df.pivot_table(index=['性别', '买衣服首选因素'], columns='家庭所在地区', values='平均月生活费(元)')
df1 = df.pivot_table(index='性别', columns='家庭所在地区', values='平均月生活费(元)')
print(df1)