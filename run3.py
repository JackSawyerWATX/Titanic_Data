import seaborn as sns

# Load the dataset
titanic = sns.load_dataset('titanic')

# show the first few rows of data
print()
print(titanic.head())

# Generate descriptive statistics
titanic_stats = titanic.describe()
print('\ntitanic_stats')

# The describe() function generates descriptive 
# statistics that summarize a dataset's 
# distribution's central tendency, dispersion, 
# and shape, excluding NaN values. describe() 
# only includes columns with numerical data.

# Generate descriptive statistics
titanic_stats = titanic.describe(include='all')
print(titanic_stats)

# Variability, also known as dispersion, is 
# the extent to which data points differ from 
# the center. Two commonly used measures are 
# the range and interquartile range (IQR). 
# The range is the difference between a 
# dataset's maximum and minimum values. 
# However, it's sensitive to outliers; 
# extremely high or low values can skew 
# the range. Here's how you calculate the 
# range for the age column of the Titanic dataset:

# Calculate the numerical data range
age_range = titanic['age'].max() - titanic['age'].min()
print('\nAge Range:', age_range) 

# The IQR measures statistical dispersion, or 
# how far apart the data points are. It's the 
# range within which the middle 50% of your 
# data falls. It's a better measure of dispersion 
# than the range because outliers don't affect 
# it. Here's how you can calculate it:

# Calculate the IQR
Q1 = titanic['age'].quantile(0.25)
Q3 = titanic['age'].quantile(0.75)
IQR = Q3 - Q1
print('\nAge IQR:', IQR) # Age IQR: 17.875

# Central tendency measures help you find
# the center of your dataset. Mean and median 
# are the most common measures of central tendency. 
# The mean or average is the most common measure 
# of central tendency. It's the sum of all data 
# points divided by the number of data points.

# Calculate the mean
mean_age = titanic['age'].mean()
print('\nMean Age:', mean_age) # Mean Age: 29.69911764705882

# The median is the middle score. The scores must 
# be arranged in numerical order to identify the median 
# correctly.

# Calculate the median
median_age = titanic['age'].median()
print('\nMedian Age:', median_age) # Median Age: 28.0

# Calculate and print the mode of the 'age' column.
mode_age = titanic['age'].mode()
print('\nMode Age:', mode_age)