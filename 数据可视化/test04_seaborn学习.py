import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 画个散点图
sns.set(style="darkgrid")
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips)
plt.show()
