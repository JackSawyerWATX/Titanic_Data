# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# TODO: Set the seaborn default aesthetic parameters
# Choose the "whitegrid" figure style, the "coolwarm" color palette, and scale the font up
sns.set(style="whitegrid", palette="coolwarm", font="Serif", font_scale=1.2)

# TODO: Create a new figure with a specific size
plt.figure(figsize=(12, 6))

# TODO: Create a countplot that displays the number of passengers in each class
sns.countplot(x='pclass', data=titanic_df)

# TODO: Add a title and labels for the x and y axes
plt.title('Passenger Class Count')
plt.xlabel('Passenger Class')
plt.ylabel('Count')

# TODO: Rotate the x-axis labels by 30 degrees
plt.xticks(rotation=30)

# TODO: Display the plot
plt.show()