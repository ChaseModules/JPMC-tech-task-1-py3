import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):

  def test_getDataPoint_calculatePrice(self):
    quotes = [
        {
            "top_ask": {
                "price": 121.2,
                "size": 36
            },
            "timestamp": "2019-02-11 22:06:30.572453",
            "top_bid": {
                "price": 120.48,
                "size": 109
            },
            "id": "0.109974697771",
            "stock": "ABC",
        },
        {
            "top_ask": {
                "price": 121.68,
                "size": 4
            },
            "timestamp": "2019-02-11 22:06:30.572453",
            "top_bid": {
                "price": 117.87,
                "size": 81
            },
            "id": "0.109974697771",
            "stock": "DEF",
        },
    ]
    """ ------------ Add the assertion below ------------ """
    quote0 = "ABC", 120.48, 121.2, (120.48 + 121.2) / 2

    self.assertEqual(getDataPoint(quotes[0]), quote0)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
        {
            "top_ask": {
                "price": 119.2,
                "size": 36
            },
            "timestamp": "2019-02-11 22:06:30.572453",
            "top_bid": {
                "price": 120.48,
                "size": 109
            },
            "id": "0.109974697771",
            "stock": "ABC",
        },
        {
            "top_ask": {
                "price": 121.68,
                "size": 4
            },
            "timestamp": "2019-02-11 22:06:30.572453",
            "top_bid": {
                "price": 117.87,
                "size": 81
            },
            "id": "0.109974697771",
            "stock": "DEF",
        },
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      expectedResult = (
          quote["stock"],
          quote["top_bid"]["price"],
          quote["top_ask"]["price"],
          round(((quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2),
                2),
      )
      self.assertEqual(getDataPoint(quote), expectedResult)

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatioAgainstAZeroPrice(self):
    self.assertEqual(getRatio(100, 0), False)

  def test_getRatio_caclulateRatioOnFirstPriceZero(self):
    self.assertEqual(getRatio(0, 1233.3), 0)

  def test_getRatio_calculateRatioAgainstLess(self):
    self.assertGreater(getRatio(123.32, 53.23), 1)

  def test_getRatio_calculateRatioAgainstGreater(self):
    self.assertLess(getRatio(123.32, 153.23), 1)

  def test_getRatio_calculateRatioAgainstGreater(self):
    self.assertEqual(getRatio(1, 1), 1)


if __name__ == "__main__":
  unittest.main()
