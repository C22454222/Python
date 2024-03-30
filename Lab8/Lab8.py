def get_tuple(movie_year: str) -> tuple:
    """Gets a string in the format 'Movie (Year)' and returns a tuple (Movie, Year)"""
    movie, year = movie_year.split(" (")
    year = year.strip(")")
    return movie, year


def create_dictionary(file_name: str) -> dict:
    """Gets file name with 'Actor, Movie (Year), Movie (Year),...' per line format and
     returns a dictionary {(Movie,Year):{actor, actor, ...}, (Movie, Year):{actor, actor}...}"""

    file = open(file_name, "r")
    movies_dictionary = {}

    for line in file:
        actor = ""
        for i, elem in enumerate(line.split(", ")):

            if i == 0:
                # Keep actor saved to add to next movies
                actor = elem
            else:
                try:
                    movies_dictionary[get_tuple(elem)].add(actor)
                except KeyError:
                    # Movie doesn't exist yet in the dictionary
                    movies_dictionary[get_tuple(elem)] = {actor}

    return movies_dictionary


def menu():
    file_name = input("Open what file: ")
    movies_dictionary = create_dictionary(file_name)

    while True:
        movies = input("Please enter two movies as 'name (year)' separated by"
                       "the appropriate operator (&, |, -), or enter '.' to quit:")

        if movies == ".":
            break

        if "&" in movies:
            (movie1, year1) = get_tuple(movies.split(" & ")[0])
            (movie2, year2) = get_tuple(movies.split(" & ")[1])

            try:
                print(movies_dictionary[(movie1, year1)].intersection(movies_dictionary[(movie2, year2)]))
            except KeyError:
                print("Movies not in the dictionary")

        if "|" in movies:
            (movie1, year1) = get_tuple(movies.split(" | ")[0])
            (movie2, year2) = get_tuple(movies.split(" | ")[1])

            try:
                print(movies_dictionary[(movie1, year1)].union(movies_dictionary[(movie2, year2)]))
            except KeyError:
                print("Movies not in the dictionary")

        if "-" in movies:
            (movie1, year1) = get_tuple(movies.split(" - ")[0])
            (movie2, year2) = get_tuple(movies.split(" - ")[1])

            try:
                print(movies_dictionary[(movie1, year1)].difference(movies_dictionary[(movie2, year2)]))
            except KeyError:
                print("Movies not in the dictionary")


menu()
