import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_json("deviation.json")
n = len(df)
# print(df.to_string())
df_4 = df[df['rb_corners'] == 4]
df_6 = df[df['rb_corners'] == 6]
df_8 = df[df['rb_corners'] == 8]

rmse = np.sqrt(df['mean'].transform(np.square).sum() / n)
mae = df['mean'].sum() / n
print('RMSE: ' + str(rmse))
print('MAE: ' + str(mae))

# boxplot by corner count
grouped = df.groupby('rb_corners')['mean']
plt.boxplot([grouped.get_group(4), grouped.get_group(6), grouped.get_group(8)])
plt.xticks([1, 2, 3], ["4 corners", "6 corners", "8 corners"])
plt.show()

# df['mean'].hist(by=df['rb_corners'], bins=40)
# plt.show()
#
# df['max'].hist(by=df['rb_corners'], bins=40)
# plt.show()

columns = ["floor_mean", "ceiling_mean"]
ax = df.boxplot(column=columns)
ax.set_ylim(0, 50)
plt.show()

plt.hist(df['mean'], bins=40)
plt.title('Mean errors')
plt.show()
# ax = df.hist(column='mean', bins=50)
# ax.title('Mean errors')
# plt.show()
#
# df.hist(column='max', bins=50)
# df.hist(column='floor_max', bins=50)
# df.hist(column='ceiling_max', bins=50)
# df.boxplot('mean')
# df.boxplot('floor_mean')
# df.boxplot('ceiling_mean')

#plt.show()

