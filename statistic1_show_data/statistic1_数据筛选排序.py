import pandas as pd
# 读取数据
df = pd.read_excel('data/1_table1.xlsx')
# 找出统计学成绩等于75的学生
df1 = df[df['统计学成绩'] == 75]
print(df1)

# 找出英语成绩最高的前三名学生
df2 = df.nlargest(3, columns='英语成绩')
# df2 = df.nsmallest(3, columns='英语成绩')  #英语成绩最低的前三名学生
print(df2)

# 找出四门课程成绩都大于70分的学生
df3 = df[(df['统计学成绩'] > 70) & (df['数学成绩'] > 70)
         & (df['英语成绩'] > 70) & (df['经济学成绩'] > 70)]
print(df3)

# 排序，升序ascending=False,降序ascending=True
df4 = df.sort_values(by='统计学成绩', ascending=False)
print(df4)




