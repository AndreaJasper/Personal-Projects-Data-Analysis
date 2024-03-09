import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
from scipy.stats import pearsonr, chi2_contingency

books = pd.read_csv('2023-Reading-Analysis\Books_2023.csv')

# Converts appropriate clumns to strings
books['Book Type'] = books['Book Type'].astype(str)
books['Book Name'] = books['Book Name'].astype(str)
books['Reading Status'] = books['Reading Status'].astype(str)
books['Author'] = books['Author'].astype(str)
books['Genre'] = books['Genre'].astype(str)
books['Author'] = books['Author'].astype(str)
books['Gender'] = books['Gender'].astype(str)

# Convert start and end date to dates
books['Start Date'] = pd.to_datetime(books['Start Date'])
books['End Date'] = pd.to_datetime(books['End Date'])

# Converts all column names to lowercase for consitency and replaces spaces with underscores
books.columns = books.columns.str.lower().str.replace(' ', '_')
print(books.head(2))

# What is the distribution of book types (e.g., fiction, non-fiction)?
plt.hist(books.genre)
plt.title('Distribution of Book Genres')
plt.show()

# What is the average rating given to books?
avg_rating = books.rating.mean()
print(avg_rating)

# Is there a correlation between book length and rating?
pages_rating_corr = books['pages'].corr(books['rating'])
print(pages_rating_corr)

plt.scatter(books['pages'], books['rating'], alpha=0.5)
plt.title('Book Length vs. Rating')
plt.xlabel('Book Length (Pages)')
plt.ylabel('Rating')
plt.show()

corr_length_rating, p = pearsonr(books.pages, books.rating)
print(corr_length_rating)

# Average time to complete a book?
avg_completion_time = books.duration.mean()
print(avg_completion_time)

# Are there certain periods of the year when more books are read?
books['month'] = books['start_date'].dt.month
# books['year'] = books['start_date'].dt.year
books_read_by_month = books.groupby('month').size()
# books_read_by_year = books.groupby('year').size()

plt.bar(books_read_by_month.index, books_read_by_month)
plt.title('Books Read by Month')
plt.xlabel('Month')
plt.ylabel('Number of Books Read')
plt.show()

# Are there differences in ratings based on author gender?
average_rating_by_gender = books.groupby('gender')['rating'].mean()
print(average_rating_by_gender)

# What is the average time taken to finish books of different genres?
# calculates the duration to finish each book in days
books['duration_to_finish_in_days'] = (books['end_date'] - books['start_date']).dt.days

# calculate the average duracton to finish books for each genre
avg_duration_by_genre = books.groupby('genre')['duration_to_finish_in_days'].mean()

plt.bar(avg_duration_by_genre.index, avg_duration_by_genre)
plt.title('Average Time Taken to Finish Books by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Duration to Finish (Days)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
