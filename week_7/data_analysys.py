def explore_data(df):
    """
    Prints dataset structure, first few rows, and statistics.
    """
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    print("\nData types and non-null counts:")
    print(df.info())

    print("\nBasic statistics:")
    print(df.describe())

def analyze_by_group(df, group_column, target_column):
    """
    Groups data by a categorical column and calculates the mean of a numerical column.
    """
    grouped = df.groupby(group_column)[target_column].mean()
    print(f"\nMean of {target_column} grouped by {group_column}:")
    print(grouped)
    return grouped
