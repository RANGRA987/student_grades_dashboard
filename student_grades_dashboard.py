import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
    "Student": ["Aryan", "Aryan", "Aryan", "Somnath", "Somnath", "Somnath", "Rohit", "Rohit", "Rohit", 
                "Sushant", "Sushant", "Sushant", "Paras", "Paras", "Paras"],
    "Subject": ["Math", "Science", "English", "Math", "Science", "English", "Math", "Science", "English", 
                "Math", "Science", "English", "Math", "Science", "English"],
    "Grade": [80, 85, 90, 92, 75, 83, 84, 72, 95, 77, 79, 82, 99, 90, 97]
})

# 1. Bar Plot for Average Grades by Subject

plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='Subject', y='Grade', estimator='mean', ci=None, palette='viridis')
plt.title('Average Grade by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Grade')
plt.show()

# 2. Pie Chart for Grade Distribution by Student

plt.figure(figsize=(8, 8))
grades_by_student = data.groupby('Student')['Grade'].mean().reset_index()
plt.pie(grades_by_student['Grade'], labels=grades_by_student['Student'], autopct='%1.1f%%', startangle=140)
plt.title('Average Grade Distribution by Student')
plt.axis('equal')
plt.show()

# 3. Scatter Plot for Grades by Subject

plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Subject', y='Grade', hue='Student', style='Student', s=100, palette='tab10')
plt.title('Scatter Plot of Grades by Subject')
plt.xlabel('Subject')
plt.ylabel('Grade')
plt.ylim(0, 100)
plt.show()

# 4. Line Plot to Show Progress of Each Student Across Subjects

plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Subject', y='Grade', hue='Student', marker='o', palette='tab10')
plt.title('Student Performance Across Subjects')
plt.xlabel('Subject')
plt.ylabel('Grade')
plt.ylim(0, 100)
plt.show()
