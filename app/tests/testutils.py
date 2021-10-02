# Create a unit test method to test the calculate_avg_rating function created in the utils module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
from logging import NullHandler
from typing import Type
from app.src.utils import calculate_avg_rating
from app.src.Review import Review
import unittest


class Testutil(unittest.TestCase):
    def test_calculate_avg_rating(self):
        reviews = [
            Review("Ray's Pizza", "This place is great", "Must Try!", 4.5),
            Review("Ray's Pizza", "This place is disgusting!",
                   "Found bugs in my salad, dirty floors, and the server spat in my food!", 1.0),
        ]
        expected = 2.75
        actual = calculate_avg_rating(reviews)
        self.assertEquals(expected, actual)

    # def test_calculate_avg_rating_type_error(self):
    #     reviews = [Review(1, 2, 3, 'a')]

    #     self.assertRaises(TypeError, calculate_avg_rating, reviews)

# def test_calculate_avg_rating_ne(self):
      #  reviews = [
       #     Review("Ray's Pizza", "This place is great", "Must Try!", 4.5),
        #    Review("Ray's Pizza", "This place is disgusting!",
        #          "Found bugs in my salad, dirty floors, and the server spat in my food!", 1.0),
        # ]
        # expected = 2.75
        # actual = calculate_avg_rating(reviews)
        # self.assertRaises(Exception, calculate_avg_rating, reviews)
