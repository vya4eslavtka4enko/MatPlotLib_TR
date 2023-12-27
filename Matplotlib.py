import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv')
# df.rolling(window=6).mean()
pd.to_datetime(df.m)
# print(date_df)
plt.plot(df.m,df['Unnamed: 2'])
plt.xlabel('Date',fontsize = 14)
plt.ylabel("Numbers of Posts",fontsize = 12)
plt.figure(figsize=(14,10))
plt.xticks(fontsize = '10')
plt.yticks(fontsize = '10')
plt.ylim(0,35000)
for column in df.columns:
    plt.plot(df.m, df['Unnamed: 2'],
    linewidth = 3, label = df[column].name)
    plt.legend(fontsize=16)

plt.show()