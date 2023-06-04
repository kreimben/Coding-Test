"""
https://www.algoexpert.io/questions/valid-starting-city
Valid Starting City
"""


def validStartingCity(distances, fuel, mpg):
    starting_city = 0

    while starting_city < len(distances):
        rest_fuel = 0

        for i in range(len(distances)):
            visiting_city = (i + starting_city) % len(distances)
            # First, I get a fuel.
            rest_fuel += mpg * fuel[visiting_city]
            # Second, Calculate distances from now with rest fuel.
            rest_fuel -= distances[visiting_city]
            # Third, Check if it is not negative.
            if rest_fuel < 0:
                break

        if rest_fuel >= 0:
            return starting_city
        starting_city += 1


assert validStartingCity(
    [5, 25, 15, 10, 15],
    [1, 2, 1, 0, 3],
    10
) == 4
