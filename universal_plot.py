# import pandas
# import matplotlib.pyplot as plt
# data = 'iris.csv'
# names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
# dataset = pandas.read_csv(data, names=names)
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# plt.show()
# dataset.hist()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt

# data = 'GAGAN PANDEY RESUME DS.csv'

# names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# dataset = pd.read_csv(data, names=names, header=None)

# dataset.plot(
#     kind='box',
#     subplots=True,
#     layout=(2, 2),
#     sharex=False,
#     sharey=False
# )

# plt.show()

# dataset.hist()
# plt.show()






# import os

# folder = r"C:\python1\pandas file system"

# print("Files available in the folder:")

# for file in os.listdir(folder):
#     print(file)

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
dataset = pd.read_csv("iris.csv")

# Display first five rows
print(dataset.head())

# Display column names
print(dataset.columns)

# Select numerical columns
numerical_data = dataset.select_dtypes(include="number")

# Create box plots
numerical_data.plot(
    kind="box",
    subplots=True,
    layout=(2, 2),
    sharex=False,
    sharey=False,
    figsize=(10, 8)
)

plt.tight_layout()
plt.show()

# Create histograms
numerical_data.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()