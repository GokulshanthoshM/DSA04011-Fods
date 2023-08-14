import pandas as pd
import matplotlib.pyplot as plt

# Read the data from CSV into a pandas DataFrame
df = pd.read_csv("sample1.csv")

# Find the top 5 players with the highest number of goals
top_goal_scorers = df.nlargest(5, "Goals")

# Find the top 5 players with the highest salaries
top_salary_players = df.nlargest(5, "Salary")

# Calculate the average age of players
average_age = df["Age"].mean()

# Find players above the average age
above_average_age_players = df[df["Age"] > average_age]

# Visualize the distribution of players based on their positions
position_counts = df["Position"].value_counts()
position_counts.plot(kind="bar")
plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()

# Display the results
print("Top 5 players with the highest number of goals:")
print(top_goal_scorers[["Name", "Goals"]])

print("\nTop 5 players with the highest salaries:")
print(top_salary_players[["Name", "Salary"]])

print(f"\nAverage age of players: {average_age:.2f}")

print("\nPlayers above the average age:")
print(above_average_age_players[["Name", "Age"]])
