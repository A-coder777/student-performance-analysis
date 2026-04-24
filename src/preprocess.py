import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("\n📌 First 5 Rows:\n", df.head())
    print("\n📌 Shape:", df.shape)
    print("\n📌 Columns:", df.columns)
    return df


def clean_data(df):
    print("\n🔧 Cleaning Data...")

    # Fill missing values
    df['Marks'].fillna(df['Marks'].mean(), inplace=True)
    df['StudyHours'].fillna(df['StudyHours'].median(), inplace=True)

    # Remove outliers
    df = df[(df['StudyHours'] <= 15) & (df['Marks'] <= 100)]

    return df


def feature_engineering(df):
    print("\n⚙️ Feature Engineering...")

    # Performance column
    def performance(marks):
        if marks >= 80:
            return "Excellent"
        elif marks >= 60:
            return "Good"
        else:
            return "Needs Improvement"

    df['Performance'] = df['Marks'].apply(performance)

    # EffortScore
    df['EffortScore'] = df['StudyHours'] * df['Attendance']

    return df