dbInserts = {
    'Subscriptions': """
    INSERT INTO Subscriptions (SubscriptionID, PlanName, Price, Duration) VALUES
        ('S1','HD', 9.99, 1),
        ('S2','UHD', 14.99, 1)
        ON DUPLICATE KEY UPDATE
        PlanName=VALUES(PlanName), 
        Price=VALUES(Price), 
        Duration=VALUES(Duration);
    """,
    'Users': """
    INSERT INTO Users (UserID, Username, Email, Password, SubscriptionID, SubscriptionType, City, Country, Age) VALUES
        ('U1','john_doe', 'john@example.com', 'password1', 'S1', 'HD', 'New York', 'USA', 28),
        ('U2','alice_smith', 'alice@example.com', 'password2', 'S1', 'HD', 'London', 'UK', 34),
        ('U3','jane_doe', 'jane@example.com', 'password3', 'S2', 'UHD', 'Chicago', 'USA', 19),
        ('U4','bob_jones', 'bob@example.com', 'password4', 'S2', 'UHD', 'Boston', 'USA', 30),
        ('U5','emma_johnson', 'emma@example.com', 'password5', 'S1', 'HD', 'Toronto', 'Canada', 55)
        ON DUPLICATE KEY UPDATE
        Username=VALUES(Username), 
        Email=VALUES(Email), Password=VALUES(Password), 
        SubscriptionID=VALUES(SubscriptionID),
        SubscriptionType=VALUES(SubscriptionType), 
        City=VALUES(City), 
        Country=VALUES(Country), 
        Age=VALUES(Age);
    """,
    'Actors': """
    INSERT INTO Actors (ActorID, Name, City, DateOfBirth) VALUES
        ('A1', 'Millie Bobby Brown', 'Los Angeles', '2004-02-19'),
        ('A2', 'Bryan Cranston', 'Hollywood', '1956-03-07'),
        ('A3', 'Winona Ryder', 'New York', '1971-10-29'),
        ('A4', 'Aaron Paul', 'Boise', '1979-08-27'),
        ('A5', 'David Harbour', 'White Plains', '1975-04-10')
        ON DUPLICATE KEY UPDATE
        Name=VALUES(Name), 
        City=VALUES(City), 
        DateOfBirth=VALUES(DateOfBirth);
    """,
    'Movies': """
    INSERT INTO Movies (MovieID, Title, Genre, ReleaseDate) VALUES
        ('M1', 'Stranger Things', 'Sci-Fi', '2016-07-15'),
        ('M2', 'Breaking Bad', 'Drama', '2008-01-20'),
        ('M3', 'The Office', 'Comedy', '2005-03-24'),
        ('M4', 'Parks and Recreation', 'Comedy', '2009-04-09'),
        ('M5', 'The Godfather', 'Crime', '1972-03-24')
        ON DUPLICATE KEY UPDATE
        Title=VALUES(Title), 
        Genre=VALUES(Genre), 
        ReleaseDate=VALUES(ReleaseDate);
    """,
    'Reviews': """
    INSERT INTO Reviews (UserID, MovieID, Username, MovieTitle, Score, Comment) VALUES
        ('U1', 'M1', 'john_doe', 'Stranger Things', 5, 'Amazing show!'),
        ('U2', 'M2', 'alice_smith', 'Breaking Bad', 3, 'Good show'),
        ('U3', 'M3', 'jane_doe', 'The Office', 4, 'Funny and smart'),
        ('U4', 'M4', 'bob_jones', 'Parks and Recreation', 2, 'Not my taste'),
        ('U5', 'M5', 'emma_johnson', 'The Godfather', 5, 'A classic!')
        ON DUPLICATE KEY UPDATE
        Username=VALUES(Username), 
        MovieTitle=VALUES(MovieTitle), 
        Score=VALUES(Score), 
        Comment=VALUES(Comment);
    """,
    'FavouriteMovies': """
    INSERT INTO FavouriteMovies (UserID, MovieID, Username, MovieTitle, Score) VALUES
        ('U1', 'M3', 'john_doe', 'The Office', 5),
        ('U1', 'M4', 'john_doe', 'Parks and Recreation', 4),
        ('U2', 'M5', 'alice_smith', 'The Godfather', 3),
        ('U3', 'M1', 'jane_doe', 'Stranger Things', 5),
        ('U4', 'M2', 'bob_jones', 'Breaking Bad', 4)
        ON DUPLICATE KEY UPDATE
        Username=VALUES(Username), 
        MovieTitle=VALUES(MovieTitle), 
        Score=VALUES(Score);
    """,
    'WatchHistory': """
    INSERT INTO WatchHistory (UserID, MovieID, Username, MovieTitle, WatchDate) VALUES
        ('U1', 'M1', 'john_doe', 'Stranger Things', '2023-07-01'),
        ('U1', 'M3', 'john_doe', 'The Office', '2023-07-02'),
        ('U2', 'M2', 'alice_smith', 'Breaking Bad', '2023-07-03'),
        ('U3', 'M1', 'jane_doe', 'Stranger Things', '2023-07-04'),
        ('U5', 'M5', 'emma_johnson', 'The Godfather', '2023-07-06')
        ON DUPLICATE KEY UPDATE
        Username=VALUES(Username), 
        MovieTitle=VALUES(MovieTitle), 
        WatchDate=VALUES(WatchDate);
    """,
    'MovieActors': """
    INSERT INTO MovieActors (MovieID, ActorID, MovieTitle, ActorName, Role) VALUES
        ('M1', 'A1', 'Stranger Things', 'Millie Bobby Brown', 'Eleven'),
        ('M2', 'A2', 'Breaking Bad', 'Bryan Cranston', 'Walter White'),
        ('M1', 'A3', 'Stranger Things', 'Winona Ryder', 'Joyce Byers'),
        ('M2', 'A4', 'Breaking Bad', 'Aaron Paul', 'Jesse Pinkman'),
        ('M1', 'A5', 'Stranger Things', 'David Harbour', 'Jim Hopper')
        ON DUPLICATE KEY UPDATE
        MovieTitle=VALUES(MovieTitle), 
        ActorName=VALUES(ActorName), 
        Role=VALUES(Role);
    """,
}

def print_formatted_sql(dbInserts):
    for insert_name, sql_command in dbInserts.items():
        print(f"{insert_name} SQL Insertion Command:")
        print(sql_command.strip())
        print("")

if __name__ == '__main__':
    print_formatted_sql(dbInserts)