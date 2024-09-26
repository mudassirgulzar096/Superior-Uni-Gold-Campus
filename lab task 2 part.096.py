movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000, 72000000),
    ("Memento", 9000000, 40000000),
    ("Requiem for a Dream", 4500000, 7350000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000, 1045000000),
    ("Avengers: Age of Ultron", 365000000, 1405000000),
    ("Avengers: Endgame", 356000000, 2797800000),
    ("Incredibles 2", 200000000, 1245000000)
]

add_more = input("Do you want to add more movies? (yes/no): ")

if add_more.lower() == "yes":
    num_movies_to_add = int(input("How many movies do you want to add? "))

    for i in range(num_movies_to_add):
        movie_name = input("Enter the movie name: ")
        movie_budget = int(input("Enter the movie budget: "))
        movie_revenue = int(input("Enter the movie revenue: "))
        movies.append((movie_name, movie_budget, movie_revenue))


movie_profits = []
for movie_name, budget, revenue in movies:
    profit = revenue - budget
    movie_profits.append((movie_name, profit))


movie_profits.sort(key=lambda x: x[1], reverse=True)


print("Movies sorted by profitability (from most to least profitable):")
for movie_name, profit in movie_profits:
    print(f"{movie_name}: Profit = ${profit}")


total_profit = sum(profit for _, profit in movie_profits)
average_profit = total_profit / len(movies)
print(f"\nAverage profit for all movies: ${average_profit}")

high_profit_movies = [movie for movie in movie_profits if movie[1] > average_profit]
print("\nMovies with profits higher than the average:")
for movie_name, profit in high_profit_movies:
    print(f"{movie_name}: ${profit} profit")
