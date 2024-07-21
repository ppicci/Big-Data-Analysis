dbQueries = {
    '1 Export all data about users in the HD subscriptions.': """
    SELECT * 
    FROM Users 
    WHERE SubscriptionType = 'HD';  
    """,
    '2 Export all data about actors and their associated movies.': """
    SELECT Actors.ActorID, Actors.Name, Actors.City, Actors.DateOfBirth, Movies.MovieID, Movies.Title, Movies.Genre, Movies.ReleaseDate
    FROM Actors 
    JOIN MovieActors ON Actors.ActorID = MovieActors.ActorID
    JOIN Movies ON MovieActors.MovieID = Movies.MovieID;
    """,
    '3 Export all data to group actors from a specific city, showing also the average age (per city).': """
    SELECT City, COUNT(ActorID) AS NumberOfActors, AVG(YEAR(CURDATE()) - YEAR(DateOfBirth)) AS AverageAge
    FROM Actors
    GROUP BY City;
    """,
    '4 Export all data to show the favourite comedy movies for a specific user.': """
    SELECT FavouriteMovies.Username, Movies.MovieID, Movies.Title, Movies.Genre,Movies.ReleaseDate
    FROM Movies 
    JOIN FavouriteMovies ON Movies.MovieID = FavouriteMovies.MovieID
    WHERE FavouriteMovies.UserID = 'U1' AND Movies.Genre = 'Comedy';
    """,
    '5 Export all data to count how many subscriptions are in the database per country.': """
    SELECT Country, COUNT(*) AS SubscriptionCount
    FROM Users
    GROUP BY Country;
    """,
    '6 Export all data to find the movies that start with the keyword The.': """
    SELECT *
    FROM Movies
    WHERE Title LIKE 'The %';
    """,
    '7 Export data to find the number of subscriptions per movie category.': """
    SELECT Genre, COUNT(DISTINCT SubscriptionID) AS SubscriptionCount
    FROM Movies
    JOIN FavouriteMovies ON Movies.MovieID = FavouriteMovies.MovieID
    JOIN Users ON FavouriteMovies.UserID = Users.UserID
    GROUP BY Genre;
    """,
    '8 Export data to find the username and the city of the youngest customer in the UHD subscription category.': """
    SELECT *
    FROM Users
    WHERE Age = (
        SELECT MIN(Age) 
        FROM Users 
        WHERE SubscriptionType = 'UHD');
    """,
    '9 Export data to find users between 22-30 years old (including 22 and 30).': """
    SELECT *
    FROM Users
    WHERE Age BETWEEN 22 AND 30;
    """,
    '10 Export data to find the average age of users with low score reviews (less than 3). Group your data for users under 20, 21-40, and 41 and over.': """
    SELECT 
      CASE 
        WHEN Age < 21 THEN 'Under 20'
        WHEN Age BETWEEN 21 AND 40 THEN '21-40'
        ELSE '41 and over'
      END AS AgeGroup,
      AVG(Age) AS AverageAge
    FROM Users
    WHERE UserID IN (
        SELECT UserID 
        FROM Reviews 
        WHERE Score < 3
    )
    GROUP BY AgeGroup;
    """,
}

def print_formatted_sql(dbQueries):
    for query_name, sql_command in dbQueries.items():
        print(f"{query_name} SQL Query:")
        print(sql_command.strip())
        print("")

if __name__ == '__main__':
    print_formatted_sql(dbQueries)