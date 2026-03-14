import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("Instructor Effectiveness Analysis Dashboard")

# Load dataset
file_path = "instructor_effectiveness_dataset_2000_rows_-_Google_Sheets_1bdf6c39.csv"

df = pd.read_csv(file_path)

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Feature Engineering
df["engagement_score"] = (
    df["avg_watch_time"] +
    df["assignment_submission_rate"] +
    df["forum_activity_rate"]
) / 3

df["learning_score"] = (
    df["avg_score_improvement"] +
    df["avg_quiz_score"]
) / 2

df["feedback_quality"] = (
    df["avg_feedback_score"] *
    df["feedback_response_rate"]
)

df["effectiveness_score"] = (
    0.30 * df["completion_rate"] +
    0.20 * df["learning_score"] +
    0.20 * df["engagement_score"] +
    0.20 * df["feedback_quality"] -
    0.10 * df["dropout_rate"]
)

# Instructor aggregation
instructor_df = df.groupby("instructor_id").mean(numeric_only=True).reset_index()

# Create tiers
instructor_df["tier"] = pd.qcut(
    instructor_df["effectiveness_score"],
    q=3,
    labels=["Low","Medium","High"]
)

st.subheader("Instructor Tier Distribution")
st.write(instructor_df["tier"].value_counts())

# Visualization
fig, ax = plt.subplots()

sns.boxplot(
    x="tier",
    y="effectiveness_score",
    data=instructor_df,
    ax=ax
)

st.pyplot(fig)

# Machine Learning
X = instructor_df.drop(["tier","instructor_id"], axis=1)
y = instructor_df["tier"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()

model.fit(X_train,y_train)

accuracy = model.score(X_test,y_test)

st.subheader("Model Accuracy")
st.write(accuracy)

# Feature Importance
importance = model.feature_importances_

feat = pd.Series(importance,index=X.columns)

st.subheader("Feature Importance")

fig2, ax2 = plt.subplots()

feat.sort_values().plot(kind="barh",ax=ax2)

st.pyplot(fig2)