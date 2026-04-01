import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\lab\Desktop\IMDB Top 250 Movies.csv")
df_numeric = df.select_dtypes(include=[np.number])
if df_numeric.shape[0] < 30:
    print("Dataset must have at least 30 rows")
else:
    df_sample = df_numeric.sample(n=30, random_state=1)
    if df_sample.shape[1] > 30:
        df_sample = df_sample.sample(n=30, axis=1, random_state=1)
    cols = df_sample.columns[:2]
    x = df_sample[cols[0]]
    y = df_sample[cols[1]]
    midpoint = len(x) // 2
    x1, y1 = x[:midpoint], y[:midpoint] * 0.8
    x2, y2 = x[midpoint:], y[midpoint:] * 1.2
    x_out = np.append(pd.concat([x1, x2]), max(x) * 1.1)
    y_out = np.append(pd.concat([y1, y2]), max(y) * 3)
    plt.figure(figsize=(10, 6))
    plt.scatter(x1, y1, color='blue', label='Cluster 1')
    plt.scatter(x2, y2, color='green', label='Cluster 2')
    plt.scatter(x_out[-1], y_out[-1], color='red', label='Outlier')
    plt.xlabel(cols[0])
    plt.ylabel(cols[1])
    plt.title('Scatter Plot (30x30 Sample with Clusters, Correlation, Outlier)')
    plt.legend()

    plt.show()