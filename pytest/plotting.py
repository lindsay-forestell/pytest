import matplotlib.pyplot as plt


def plot_hist(df, col):
    vals = df[col].values
    plt.hist(vals)
    plt.show()
