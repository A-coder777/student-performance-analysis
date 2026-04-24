from src.preprocess import load_data, clean_data, feature_engineering
from src.analysis import basic_stats, top_students, low_performers, group_analysis, insights

def main():
    path = "data/student_dataset.csv"

    df = load_data(path)
    df = clean_data(df)
    df = feature_engineering(df)

    basic_stats(df)
    top_students(df)
    low_performers(df)
    group_analysis(df)
    insights()


if __name__ == "__main__":
    main()