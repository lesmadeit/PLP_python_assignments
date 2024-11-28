#Activity 1

# Defining the base class
class Movie:
    def __init__(self, title, director, genre, duration):
        self.title = title
        self.director = director
        self.genre = genre
        self.duration = duration

    def watch(self):
        return f"You are watching '{self.title}' by {self.director}."

    def get_info(self):
        return f"'{self.title}' is a {self.genre} that runs for {self.duration} minutes"

# Subclass to demonstrate inheritance and encapsulation
class StreamingMovie(Movie):
    def __init__(self, title, director, genre, duration, platform, year_of_release):
        super().__init__(title, director, genre, duration)
        self.platform = platform 
        self.year = year_of_release 

    def watch(self):
        return f"You are streaming '{self.title}' on {self.platform} "

    def is_new_release(self):
        return self.year >= 2023

# Example of use
theater_movie = Movie("The Godfather", "Ford Coppola", "Crime", 328)
streaming_movie = StreamingMovie("The Irishman", "Martin Scorsese", "Crime", 209, "Netflix", 2019)

print(theater_movie.watch())
print(theater_movie.get_info())
print(theater_movie.watch())
print(f"Is '{streaming_movie.title}' a new release? {'Yes' if streaming_movie.is_new_release() else 'No'}")






#Activity 2


# Base class for vehicles
class Animals:
    def sound(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

# Subclass for cow
class Cow(Animals):
    def sound(self):
        return "Moos"

# Subclass for cat
class Cat(Animals):
    def sound(self):
        return "Meows"

# Subclass for snake
class Snake(Animals):
    def sound(self):
        return "Hissess"

# Subclass for boats
class Sheep(Animals):
    def sound(self):
        return "Bleats"

# Example usage
animals = [Cow(), Cat(), Snake(), Sheep()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.sound()}")
