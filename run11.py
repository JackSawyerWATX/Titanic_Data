# Importing required libraries
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# TODO: Create a boxplot to illustrate the relationship between the fare and passenger class, categorized by their survival status.
sns.boxplot(
    x='pclass', 
    y='fare',
    hue='survived',
    data=titanic_df,
    palette='Set3', 
    linewidth=1.5,
    order=[3,1,2], 
    hue_order=[1,0],
    color='skyblue', 
    saturation=0.7,
    dodge=True, 
    fliersize=5
)

# TODO: Set a fitting title for the plot
plt.title('Fares vs Passenger Classes Differentiated by Survival')

# TODO: Finally, display the plot
plt.show()