dbTables = {
    'Subscriptions': """
    CREATE TABLE IF NOT EXISTS Subscriptions (
        SubscriptionID VARCHAR(3),
        PlanName VARCHAR(10),
        Price DECIMAL(5,2),
        Duration Int(2), 
        PRIMARY KEY (SubscriptionID)
    );
    """,
    'Users': """
    CREATE TABLE IF NOT EXISTS Users (
        UserID VARCHAR(10),
        Username VARCHAR(20),
        Email VARCHAR(30),
        Password VARCHAR(20),
        SubscriptionID VARCHAR(3),
        SubscriptionType VARCHAR(10),
        City VARCHAR(20),
        Country VARCHAR(20),
        Age INT(3),
        PRIMARY KEY (UserID),
        FOREIGN KEY (SubscriptionID) REFERENCES Subscriptions(SubscriptionID)
    );
    """,
    'Actors' :"""
    CREATE TABLE IF NOT EXISTS Actors (
        ActorID VARCHAR(10),
        Name VARCHAR(30),
        City VARCHAR(20),
        DateOfBirth DATE,
        PRIMARY KEY (ActorID)
    );
    """,
    'Movies': """
    CREATE TABLE IF NOT EXISTS Movies (
        MovieID VARCHAR(10),
        Title VARCHAR(30),
        Genre VARCHAR(15),
        ReleaseDate DATE,
        PRIMARY KEY (MovieID)
    );
    """,
    'Reviews': """
    CREATE TABLE IF NOT EXISTS Reviews (
        UserID VARCHAR(10),
        MovieID VARCHAR(10),
        Username VARCHAR(20),
        MovieTitle VARCHAR(30),
        Score INT(1) CHECK (Score BETWEEN 0 AND 5),
        Comment VARCHAR(50),
        PRIMARY KEY (UserID, MovieID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
    );
    """,
    'FavouriteMovies': """
    CREATE TABLE IF NOT EXISTS FavouriteMovies (
        UserID VARCHAR(10),
        MovieID VARCHAR(10),
        Username VARCHAR(20),
        MovieTitle VARCHAR(30),
        Score INT(1) CHECK (Score BETWEEN 0 AND 5),
        PRIMARY KEY (UserID, MovieID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
    );
    """,
    'WatchHistory': """
    CREATE TABLE IF NOT EXISTS WatchHistory (
        UserID VARCHAR(10),
        MovieID VARCHAR(10),
        Username VARCHAR(20),
        MovieTitle VARCHAR(30),
        WatchDate DATE,
        PRIMARY KEY (UserID, MovieID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
    );
    """,
    'MovieActors': """
    CREATE TABLE IF NOT EXISTS MovieActors (
        MovieID VARCHAR(10),
        ActorID VARCHAR(10),
        MovieTitle VARCHAR(30),
        ActorName VARCHAR(30),
        Role VARCHAR(30),
        PRIMARY KEY (MovieID, ActorID),
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
        FOREIGN KEY (ActorID) REFERENCES Actors(ActorID)
    );
    """,
}
def print_formatted_sql(dbTables):
    for table_name, sql_command in dbTables.items():
        print(f"{table_name} Table SQL Command:")
        print(sql_command.strip())
        print("")

if __name__ == '__main__':
    print_formatted_sql(dbTables)