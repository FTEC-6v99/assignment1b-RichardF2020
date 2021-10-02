# Create a function called calculate_avg_rating
# Parameters: the function should have one argument of type list of Review (i.e., the arg should be a list of Review objects)
# Returns: the function should return a float: the average of all raview ratings that are given in the list as an argument to this function.
#          The returned value should be rounded to the closest second decimal. Use the build-in round function: https://www.w3schools.com/python/ref_func_round.asp
#
# If the argument is an empty list, return 0.0
# for reference on exceptions, check the class notes here: https://github.com/FTEC-6v99/python-overview/blob/master/advanced/exceptions.py
#
# Make sure that you add type hints to the function paramter and return value

from app.src.Review import Review
import typing as t


def calculate_avg_rating(reviews: t.List[Review]) -> float:
    if reviews == {}:
        return 0.0
    s = 0.0
    for review in reviews:
        s += review.rating
    return round(s/len(reviews), 2)
