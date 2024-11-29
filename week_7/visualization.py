import matplotlib.pyplot as plt
import seaborn as sns

def plot_line_chart(df, x_col, y_col):
    plt.figure(figsize=(10, 6))
    df.plot(x=x_col, y=y_col, kind='line', title=f"Line Chart: {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid()
    plt.show()

def plot_bar_chart(df, x_col, y_col):
    plt.figure(figsize=(10, 6))
    df.groupby(x_col)[y_col].mean().plot(kind='bar', title=f"Bar Chart: Avg {y_col} by {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(f"Average {y_col}")
    plt.xticks(rotation=45)
    plt.show()

def plot_histogram(df, column):
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=20, edgecolor='k', alpha=0.7)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()

def plot_scatter(df, x_col, y_col, hue_col=None):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col)
    plt.title(f"Scatter Plot: {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend(title=hue_col)
    plt.show()
