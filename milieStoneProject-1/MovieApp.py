MAIN_MENU = "\n Enter 'a' to add a movie to the list, 'l' to see the list of movies, 'f' to find a movie by title, or 'q' to quit the app::"

movies = []


def addMovie():
    title = input("Enter Movie Title ")
    director = input("Enter the Director Name")
    year = input("Enter the year of movie release")

    # append function is used to add the dictionary to the list
    # _add_ function is used to add the list to list,  movies.__add__(
    # TypeError: can only concatenate list (not "dict") to list
    movies.append(
        {
            "movie": title,
            "director": director,
            "year": year
        })


def showMovie():
    for movie in movies:
        print_Movie(movie)


def print_Movie(movie):
    print(f"Movie Title :: {movie['movie']}")
    print(f"Movie Director :: {movie['director']}")
    print(f"Movie Release Year :: {movie['year']}")


def find_Movie():
    search_title = input("Enter the movie title....")
    for movie in movies:
        if movie['movie'] == search_title:
            print_Movie(movie)


user_options = {
    "a": addMovie,
    "l":showMovie,
    "f":find_Movie
}

def menu():
    selection = input(MAIN_MENU)

    while selection != "q":
        if selection in user_options:
            selectedFunction = user_options[selection]
            selectedFunction()
        else:
            print("Enter a valid command ....Command Unknow...")

        selection = input(MAIN_MENU)


# print(movies)

menu()
