import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Page Configuration
st.set_page_config(page_title="Student Performance Prediction", layout="wide")

st.title("🎓 Student Performance Prediction System")

# Load Dataset
df = pd.read_csv("student_data.csv")

# Display Dataset
st.subheader("Student Dataset")
st.dataframe(df)

# Features and Target
X = df[["StudyHours", "Attendance", "Assignments", "PreviousMarks"]]
y = df["Result"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Sidebar
st.sidebar.header("Enter Student Details")

study_hours = st.sidebar.slider("Study Hours", 1, 10, 5)

attendance = st.sidebar.slider("Attendance (%)", 40, 100, 75)

assignments = st.sidebar.slider("Assignments Completed", 1, 10, 5)

previous_marks = st.sidebar.slider("Previous Marks", 30, 100, 60)

# Prediction
if st.sidebar.button("Predict Result"):

    student = [[study_hours, attendance, assignments, previous_marks]]

    prediction = model.predict(student)

    st.subheader("Prediction Result")

    if prediction[0] == "Pass":
        st.success("🎉 The student is likely to PASS.")
    else:
        st.error("❌ The student is likely to FAIL.")

# Accuracy
accuracy = model.score(X_test, y_test)

st.subheader("Model Accuracy")
st.write(f"Accuracy: **{accuracy * 100:.2f}%**")

# Charts
st.subheader("Student Performance Analysis")

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(df.groupby("Result").size())

with col2:
    st.bar_chart(df.groupby("Attendance")["PreviousMarks"].mean())

# Statistics
st.subheader("Dataset Statistics")
st.write(df.describe())