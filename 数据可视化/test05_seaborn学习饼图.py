import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 画个折线图
fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", hue="event", kind="line", data=fmri)
plt.show()

