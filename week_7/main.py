import matplotlib.pyplot as plt
from data_loading import load_dataset, clean_dataset
from data_analysis import explore_data, analyze_by_group
from visualization import plot_line_chart, plot_bar_chart, plot_histogram, plot_scatter

def main():
    # Task 1: Load and Explore the Dataset
    print("Loading dataset...")
    df, metadata, variables = load_dataset()

    print("\nDataset Columns:")
    print(df.columns)  # Ensure correct column names

    print("\nFirst few rows of the dataset:")
    print(df.head())  # This will show a preview of the dataset

    print("\nDataset Metadata:")
    print(metadata)
    print("\nVariable Information:")
    print(variables)

    print("\nCleaning dataset...")
    df = clean_dataset(df)

    print("\nExploring dataset...")
    explore_data(df)

    # Task 2: Basic Data Analysis
    print("\nAnalyzing dataset...")
    analyze_by_group(df, group_column="class", target_column="sepal length")

    # Task 3: Data Visualization
    print("\nVisualizing dataset...")
    
    # Histogram
    plot_histogram(df, "sepal length")
    plt.show()  # Show histogram

    # Scatter Plot
    plot_scatter(df, "sepal length", "petal length", "class")
    plt.show()  # Show scatter plot

    # Bar Chart
    plot_bar_chart(df, "class", "sepal length")
    plt.show()  # Show bar chart

    # Line Chart
    plot_line_chart(df, x_col="sepal width", y_col="sepal length")
    plt.show()  # Show line chart

if __name__ == "__main__":
    main()
