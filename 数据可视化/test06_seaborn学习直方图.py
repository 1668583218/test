import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 画个直方图
titanic = sns.load_dataset("titanic")
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
plt.show()