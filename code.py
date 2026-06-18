import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Arun", "Priya", "Ravi", "Divya", "Karthik"],
    "Maths": [85, 92, 70, 88, 65],
    "Science": [90, 88, 75, 91, 72],
    "English": [78, 95, 80, 89, 68]
}

df = pd.DataFrame(data)

df["Total"] = df["Maths"] + df["Science"] + df["English"]

print("Average Marks =", df["Total"].mean())

topper = df.loc[df["Total"].idxmax()]
print("Topper =", topper["Name"])

plt.bar(df["Name"], df["Total"])
plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.show()