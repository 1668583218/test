import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 画个散点图
# sns.set(style="darkgrid")
# tips = sns.load_dataset("tips")
# sns.relplot(x="total_bill", y="tip", data=tips)
# plt.show()

# 画个折线图
# sns.set(style="darkgrid")
# np.random.seed(0)
# my_dpi = 96
# plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)
# values = np.cumsum(np.random.randn(1000, 1))
# plt.plot(values)
# plt.show()

# 画个直方图
sns.set(style="darkgrid")
titanic = sns.load_dataset("titanic")
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic);
plt.show()