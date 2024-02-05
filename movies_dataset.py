# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:23:19 2024

@author: ADMIN
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")

print(df)

print(df.info())
'''
# #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
    '''
        
print(df.describe())

# Rename columns by removing spaces
df.columns = df.columns.str.replace(" ", "_")

# Fill missing values for numeric columns with mean
x = df["Revenue_(Millions)"].mean()
y = df["Metascore"].mean()

df["Revenue_(Millions)"].fillna(x, inplace = True) 
df["Metascore"].fillna(y, inplace = True)

max_rating = df["Rating"].max()

print("Highest movie rate:", max_rating)
#Question1
# Find the highest-rated movie 
highest_rated_movie = df.sort_values(by="Rating", ascending=False).iloc[0]

# Display the details of the highest-rated movie
print(highest_rated_movie[["Title", "Rating"]])

#Question2

av_rev = df["Revenue_(Millions)"].mean()  

# Display the average revenue
print("Average Revenue of All Movies:", av_rev)

#Question3

# Filter movies released between 2015 and 2017
df["Year"] = pd.to_datetime(df["Year"], format="%Y")

filtered_df = df[(df["Year"].dt.year >= 2015) & (df["Year"].dt.year <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_to_2017 = filtered_df["Revenue_(Millions)"].mean()

# Display the average revenue for movies from 2015 to 2017
print("Average Revenue of Movies from 2015 to 2017:", average_revenue_2015_to_2017)


#Question4
# Filter movies released in the year 2016
movies_2016 = df[df["Year"].dt.year == 2016]

# Get the count of movies released in 2016
num_movies_2016 = len(movies_2016)

# Display the result
print("Number of Movies Released in 2016:", num_movies_2016)

#Queston5
# Filter movies directed by Christopher Nolan
nolan_movies = df[df["Director"] == "Christopher Nolan"]

# Get the count of movies directed by Christopher Nolan
num_nolan_movies = len(nolan_movies)

# Display the result
print("Number of Movies Directed by Christopher Nolan:", num_nolan_movies)

#Question6
# Filter movies with a rating of at least 8.0
high_rated_movies = df[df["Rating"] >= 8.0]

# Get the count of movies with a rating of at least 8.0
num_high_rated_movies = len(high_rated_movies)

# Display the result
print("Number of Movies with a Rating of at least 8.0:", num_high_rated_movies)

#Question7
# Filter movies directed by Christopher Nolan
nolan_movies = df[df["Director"] == "Christopher Nolan"]

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies["Rating"].median()

# Display the result
print("Median Rating of Movies Directed by Christopher Nolan:", median_rating_nolan_movies)

#Question8
# Group the DataFrame by release year and calculate the average rating for each year
average_rating_by_year = df.groupby("Year")["Rating"].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year[average_rating_by_year == average_rating_by_year.max()].index[0]

# Display the result
print("Year with the Highest Average Rating:", year_highest_average_rating)

#Question9
# Extract the counts for 2006 and 2016
movies_2006 = df[df["Year"].dt.year == 2006]
movies_2016 = df[df["Year"].dt.year == 2016]

num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)
# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
# Display the result
print(f"Percentage Increase in Number of Movies from 2006 to 2016: {percentage_increase:.2f}%")

#Question10
from collections import Counter

# Split the comma-separated strings in the 'Actors' column into lists
df["Actors"] = df["Actors"].str.split(', ')

# Flatten the lists in the 'Actors' column
all_actors = [actor for sublist in df["Actors"].dropna() for actor in sublist]

# Use Counter to count the occurrences of each actor
actor_counts = Counter(all_actors)

# Find the most common actor
most_common_actor = actor_counts.most_common(1)[0][0]

# Display the result
print("Most Common Actor in All Movies:", most_common_actor)

#Question11
# Split the comma-separated strings in the 'Genre' column into lists
df["Genre"] = df["Genre"].str.split(', ')

# Flatten the lists in the 'Genre' column
all_genres = [genre for sublist in df["Genre"].dropna() for genre in sublist]

# Get the count of unique genres
num_unique_genres = len(set(all_genres))

# Display the result
print("Number of Unique Genres in the Dataset:", num_unique_genres)

#Question12
# Drop non-numeric columns before calculating the correlation matrix
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix of numerical features
correlation_matrix = numeric_df.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Deduce insights
'''
Title  ... Revenue (Millions) Metascore
0       1  Guardians of the Galaxy  ...             333.13      76.0
1       2               Prometheus  ...             126.46      65.0
2       3                    Split  ...             138.12      62.0
3       4                     Sing  ...             270.32      59.0
4       5            Suicide Squad  ...             325.02      40.0
..    ...                      ...  ...                ...       ...
995   996     Secret in Their Eyes  ...                NaN      45.0
996   997          Hostel: Part II  ...              17.54      46.0
997   998   Step Up 2: The Streets  ...              58.01      50.0
998   999             Search Party  ...                NaN      22.0
999  1000               Nine Lives  ...              19.64      11.0

[1000 rows x 12 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None
              Rank         Year  ...  Revenue (Millions)   Metascore
count  1000.000000  1000.000000  ...          872.000000  936.000000
mean    500.500000  2012.783000  ...           82.956376   58.985043
std     288.819436     3.205962  ...          103.253540   17.194757
min       1.000000  2006.000000  ...            0.000000   11.000000
25%     250.750000  2010.000000  ...           13.270000   47.000000
50%     500.500000  2014.000000  ...           47.985000   59.500000
75%     750.250000  2016.000000  ...          113.715000   72.000000
max    1000.000000  2016.000000  ...          936.630000  100.000000

[8 rows x 7 columns]
Highest movie rate: 9.0
Title     The Dark Knight
Rating                9.0
Name: 54, dtype: object
Average Revenue of All Movies: 82.95637614678898
Average Revenue of Movies from 2015 to 2017: 68.06402328198025
Number of Movies Released in 2016: 297
Number of Movies Directed by Christopher Nolan: 5
Number of Movies with a Rating of at Least 8.0: 78
Median Rating of Movies Directed by Christopher Nolan: 8.6
Year with the Highest Average Rating: 2007-01-01 00:00:00
Percentage Increase in Number of Movies from 2006 to 2016: 575.00%
Most Common Actor in All Movies: Mark Wahlberg
Number of Unique Genres in the Dataset: 207
Correlation Matrix:
                        Rank  Runtime_(Minutes)  ...  Revenue_(Millions)  Metascore
Rank                1.000000          -0.221739  ...           -0.252996  -0.185159
Runtime_(Minutes)  -0.221739           1.000000  ...            0.247834   0.202239
Rating             -0.219555           0.392214  ...            0.189527   0.604723
Votes              -0.283876           0.407062  ...            0.607941   0.318116
Revenue_(Millions) -0.252996           0.247834  ...            1.000000   0.132304
Metascore          -0.185159           0.202239  ...            0.132304   1.000000

[6 rows x 6 columns]
'''

