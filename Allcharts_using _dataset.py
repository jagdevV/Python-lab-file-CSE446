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
    fig, axs = plt.subplots(3, 2, figsize=(14, 12))
    fig.suptitle('Multiple Plots from 30x30 Sample Data')
    axs[0, 0].plot(df_sample.iloc[:, 0], label=df_sample.columns[0])
    axs[0, 0].set_title('Line Plot')
    axs[0, 0].legend()
    if df_sample.shape[1] >= 2:
        axs[0, 1].scatter(df_sample.iloc[:, 0], df_sample.iloc[:, 1])
        axs[0, 1].set_title('Scatter Plot')
        axs[0, 1].set_xlabel(df_sample.columns[0])
        axs[0, 1].set_ylabel(df_sample.columns[1])
    axs[1, 0].bar(range(len(df_sample.iloc[:, 0])), df_sample.iloc[:, 0])
    axs[1, 0].set_title('Bar Chart')
    pie_data = df_sample.iloc[:5, 0]
    axs[1, 1].pie(pie_data, labels=[f'Item {i}' for i in range(1, 6)], autopct='%1.1f%%')
    axs[1, 1].set_title('Pie Chart')
    axs[2, 0].step(range(len(df_sample.iloc[:, 0])), df_sample.iloc[:, 0], where='mid')
    axs[2, 0].set_title('Stair Plot')
    if df_sample.shape[1] >= 2:
        axs[2, 1].plot(df_sample.iloc[:, 1], color='green')
        axs[2, 1].set_title('Line Plot (2nd Column)')
    else:
        axs[2, 1].axis('off')

    plt.tight_layout()
    plt.show()