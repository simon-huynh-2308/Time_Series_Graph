#Histogram using Python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = np.random.multivariate_normal([0,0], [[5,2], [2,2]], size=2500)
data = pd.DataFrame(data, columns=["x", "y"])
plt.hist(data["x"], alpha=0.5)
plt.hist(data["y"], alpha=0.5)
plt.show()

#Density plots using Python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = np.random.multivariate_normal([0,0], [[5,2], [2,2]], size=2500)
data = pd.DataFrame(data, columns=["x","y"])
sns.kdeplot(data["x"], shade=True, fill=True)
sns.kdeplot(data["y"], shade=True, fill=True)
plt.show()

#Both histogram and density plots at once

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = np.random.multivariate_normal([0,0], [[5,2], [2,2]], size=2500)
data = pd.DataFrame(data, columns=["x","y"])
sns.distplot(data["x"])
sns.distplot(data["y"])
plt.show()
