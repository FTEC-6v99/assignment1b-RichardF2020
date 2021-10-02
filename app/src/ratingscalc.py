# Create a function called: calc_avg_rating
# Parameters: the function should receive 1 parameter: a list of review objects
#             Remember a list can contain duplicates, so you can expect multiple reviews for the same restaurant
# Returns: the function should return a dictionary with restaurant name as key and average rating as value
#
#
# If the list of reviews is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value

def calc_avg_rating(reviews: t.List[Review]) -> dict[str, float]:
    # treating this as an object, using == instead of =. using t/f
    if len(reviews) == {}:
        return {}

    reviews_res: dict[str, t.List[Review]] = {}
    for review in reviews:
        if review.restaurant_name in reviews_res:
            reviews_res.get(review.restaurant_name).append(review)
        else:
            reviews_res[review.restaurant_name] = [review]

    rating_res: dict[str, t.List[float]] = {}
    for name, list_rev in reviews_res.items():
        rating_res[name] = calculate_avg_rating(list_rev)
    return rating_res
