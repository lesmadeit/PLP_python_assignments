from data_loading import load_dataset, clean_dataset
from data_analysis import explore_data, analyze_by_group
from visualization import plot_line_chart, plot_bar_chart, plot_histogram, plot_scatter

def main():
    # Task 1: Load and Explore the Dataset
    print("Loading dataset...")
    df, metadata, variables = load_dataset()
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
    plot_histogram(df, "sepal length")
    plot_scatter(df, "sepal length", "petal length", "class")
    plot_bar_chart(df, "class", "sepal length")
    plot_line_chart(df, x_col="sepal width", y_col="sepal length")  # Example with a different column

if __name__ == "__main__":
    main()
