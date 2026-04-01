import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\lab\Desktop\IMDB Top 250 Movies.csv")
df_numeric = df.select_dtypes(include=[np.number])
if df_numeric.shape[0] < 30:
    print("Dataset must have at least 30 rows")
else:
    df_sample = df_numeric.sample(n=30, random_state=1)
    plt.figure(figsize=(12, 6))
    plt.boxplot(df_sample.values)
    plt.xticks(range(1, len(df_sample.columns) + 1), df_sample.columns, rotation=45)

    plt.title('Boxplot of All Numeric Columns (30 Random Rows)')
    plt.xlabel('Columns')
    plt.ylabel('Values')

    plt.tight_layout()
    plt.show()