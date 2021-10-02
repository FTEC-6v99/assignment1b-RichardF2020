# Use unittest library to create a unit test method to test the calc_avg_rating function created in the ratingscalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest
from app.src.ratingscalc import calc_avg_rating
from app.src.Review import Review


class Testcalcavgrating(unittest.TestCase):
    def test_calc_avg_rating(self):
        reviews = [
            Review("Ray's Pizza", "This place is great", "Must Try!", 4.5),
            Review("Ray's Pizza", "This place is disgusting!",
                   "Found bugs in my salad, dirty floors, and the server spat in my food!", 1.0),
            Review("Bumpin' Bobba", "Best bobba tea in the city!",
                   "Went here last night, order taro bobba with extra bobba, super fast, but kinda pricey.", 4.0),
            Review("Bumpin' Bobba", "Could be better",
                   "Went here this afternoon for a to go order, got my order, it was the wrong one. called the store, refused a refund. won't be coming back.", 2.0),
            Review("Thumpin' Taquitos", "Best tacos, hands down. Don't @ me.",
                   "This place is the go to spot after you had beers from the local dive bars around town. The al pastor makes you forget all your trauma", 5.0),
            Review("Thumpin' Taquitos", "Tortas Tuesday, best value in town",
                   "Did your mom died suddenly and you never had that last meal from her? don't worry, you can get that loving taste of mom's cooking here!", 5.0)
        ]
        expected = {
            "Ray's Pizza": 2.75, "Bumpin' Bobba": 3.00, "Thumpin' Taquitos": 5.00
        }
        actual = calc_avg_rating(reviews)
        self.assertEquals(expected, actual)
