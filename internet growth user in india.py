import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("D:/india data.csv")

# Convert Year column to integer
df["Year"] = df["Year"].astype(int)

# Ensure correct data type for 'No. of Internet Users'
df["No. of Internet Users"] = pd.to_numeric(df["No. of Internet Users"], errors="coerce")

# Set up the figure
plt.figure(figsize=(8, 6), dpi=80)  # Lower DPI for smaller file size

# Gradient colors based on value progression
# Generate unique colors for each bar using a color map
colors = plt.cm.plasma(np.linspace(0.2, 1, len(df)))

# Apply unique colors to bars
bars = plt.bar(df["Year"], df["No. of Internet Users"], color=colors)
# Add labels to bars
for bar, value in zip(bars, df["No. of Internet Users"]):
    text_color = "black" if value > 1000000 else "black"
    offset = 5000000 if value < 50000000 else value * 0.02
    rotation_angle = 360 if value >= 600000000 else 90

    plt.text(bar.get_x() + bar.get_width() / 2, 
             bar.get_height() + offset, 
             f"{int(value):,}", 
             ha='center', va='bottom',
             rotation=rotation_angle, fontsize=9, 
             color=text_color, fontweight="bold")

# Add milestone annotations
milestones = {
    2020: "COVID Surge"
}

for year, note in milestones.items():
    if year in df["Year"].values:
        value = df.loc[df["Year"] == year, "No. of Internet Users"].values[0]
        plt.annotate(note,
                     xy=(year, value),  # Pointing location
                     xytext=(year -3, value - 3000000),  # Shift right
                     ha='right', va='center',fontsize=12,
                     color='black', fontweight="normal",
                     arrowprops=dict(arrowstyle='->',facecolor='black', ))
milestones2 = {
    2016: "Jio Launch"
   
}

for year, note in milestones2.items():
    if year in df["Year"].values:
        value = df.loc[df["Year"] == year, "No. of Internet Users"].values[0]
        plt.annotate(note,
                     xy=(year, value),  # Pointing location
                     xytext=(year + 2, value * 1.05),  # Shift right
                     ha='left', va='center', fontsize=12,
                     color='black', fontweight="normal",
                     arrowprops=dict(arrowstyle='->',))
        


# Customize chart
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Number of Internet Users", fontsize=12, fontweight='bold')
plt.title(" Growth of Internet Users in India Over the Years", fontsize=16, fontweight='bold')
plt.xticks(rotation=45, color ='black')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.box(False)


# Show the plot
plt.show()
