# create a new class called Review
# the class must have the following properties/attributes:
# 1. restaurant: name of the restaurant
# 2. review_title: the title of the review
# 3. review_body: the body of the review
# 4. rating: a numeric rating from 1 to 5
#
# Your class constructor (__init__ function) must raise an Exception if
# rating provided was not between 1 and 5
#
# Use typing module to hint the class attributes

class Review():
    def __init__(self, restaurant_name: str, title_of_review: str, body_of_review: str, rating: int):
        self.restaurant_name = restaurant_name
        self.title_of_review = title_of_review
        self.body_of_review = body_of_review
        if(rating < 1 or rating > 5):
            raise Exception(
                'Invalid value for rating. Please enter a number between 1 - 5')
        self.rating = rating
