# Import seaborn
import seaborn as sns

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Print the shape of the DataFrame
print('Shape of the DataFrame:')
print(titanic_df.shape)

# Print the fifty five entries of the DataFrame
print('First fifty entries of the DataFrame:')
print(titanic_df.head(50))

# Print the last fifty entries of the DataFrame
print('Last fifty entries of the DataFrame:')
print(titanic_df.tail(50))

# Print the count of male and female passengers
print('\nSex distribution:')
print(titanic_df['sex'].value_counts())

# Print the unique and count of unique 'embarked' entries
print('\nUnique entries and count of unique entries in the "embarked" column:')
print('Count:', titanic_df['embarked'].nunique())
print('Entries:', titanic_df['embarked'].unique())

# Print a concise summary of the DataFrame
print('\nConcise summary of the DataFrame:')
titanic_df.info()

# Print the descriptive statistics of the DataFrame
print('\nDescriptive statistics of the DataFrame:')
print(titanic_df.describe())