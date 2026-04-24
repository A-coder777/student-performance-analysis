def basic_stats(df):
    print("\n📊 Basic Statistics:\n", df.describe())


def top_students(df):
    print("\n🏆 Top 5 Students:\n", df.sort_values(by='Marks', ascending=False).head(5))


def low_performers(df):
    print("\n⚠️ Students with Marks < 50:\n", df[df['Marks'] < 50])


def group_analysis(df):
    print("\n📈 Avg Marks by Attendance:\n", df.groupby('Attendance')['Marks'].mean())

    # Study category
    def category(hours):
        if hours < 3:
            return "Low"
        elif hours < 6:
            return "Medium"
        else:
            return "High"

    df['StudyCategory'] = df['StudyHours'].apply(category)

    print("\n📊 Avg Marks by Study Category:\n", df.groupby('StudyCategory')['Marks'].mean())


def insights():
    print("\n🧠 Key Insights:")
    print("1. Higher study hours generally improve marks.")
    print("2. Students with high attendance perform better.")
    print("3. Low attendance leads to poor performance.")
    print("4. EffortScore helps identify consistent students.")
    print("5. Study hours alone are not enough without attendance.")