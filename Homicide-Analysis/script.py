import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("homicide_report.csv")

# average age of perpetrator
# Convert the 'Perpetrator Age' column to numeric, coercing errors to NaN for non-numeric values
df['Perpetrator Age'] = pd.to_numeric(df['Perpetrator Age'], errors='coerce')

# Calculate the average perpetrator's age, excluding NaN values
average_age = int(df['Perpetrator Age'].mean())

print("Average Perpetrator's Age:", average_age)

# states with most and least homicides
# Group the DataFrame by the 'State' column and sum up the victim counts for each state
victim_counts_per_state = df.groupby('State')['Victim Count'].sum()

# Get the state with the most murders (highest victim count)
state_with_most_murders = victim_counts_per_state.idxmax()
most_murders_count = victim_counts_per_state.max()

# Get the state with the least murders (lowest victim count)
state_with_least_murders = victim_counts_per_state.idxmin()
least_murders_count = victim_counts_per_state.min()

print("State with the most murders (by victim count):", state_with_most_murders)
print("Total victims in that state:", most_murders_count)

print("\nState with the least murders (by victim count):", state_with_least_murders)
print("Total victims in that state:", least_murders_count)

# solved per state
solved_per_state = df.groupby('State')['Crime Solved'].apply(lambda x: (x == 'Yes').sum()).reset_index()
print(solved_per_state)

#solved v unsolved
# Count the occurrences of solved and unsolved crimes
solved_vs_unsolved = df['Crime Solved'].value_counts()

# Get the count of solved and unsolved crimes
solved_count = (solved_vs_unsolved['Yes']/ df.shape[0]).round(2) * 100
unsolved_count = (solved_vs_unsolved['No']/ df.shape[0]).round(2) * 100

print("Percent of solved crimes:", solved_count)
print("Percent of unsolved crimes:", unsolved_count)

# difference in total deaths from 1980 and 2014
# Filter the DataFrame to include data from 1980 to 2014
filtered_df = df[(df['Year'] >= 1980) & (df['Year'] <= 2014)]

# Group the filtered DataFrame by the 'Year' column and count the number of murders per year
murders_per_year = filtered_df['Year'].value_counts().sort_index()

# Calculate the murder rates for each year
murder_rates = murders_per_year.diff().fillna(murders_per_year.iloc[0]) / murders_per_year.iloc[0] * 100

# Calculate the percentage change in murder rates from 1980 to 2014
decline_percentage = murder_rates.iloc[-1] - murder_rates.iloc[0]

print("Murder rates have declined by approximately {:.2f}% from 1980 to 2014.".format(decline_percentage))

# which gender is more likely to commit a crime?
# Count the number of crimes committed by perpetrators of each sex
crimes_by_sex = df['Perpetrator Sex'].value_counts()

# Determine which sex is more likely to commit murder
more_likely_sex = crimes_by_sex.idxmax()

print("Number of crimes committed by perpetrators of each sex:")
print(crimes_by_sex)

print("\n{} is more likely to commit murder.".format(more_likely_sex))
