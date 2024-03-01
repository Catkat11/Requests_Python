class FlightData:
    """
    A class to represent flight data.

    Attributes:
    - price (float): The price of the flight.
    - origin_city (str): The origin city of the flight.
    - origin_airport (str): The origin airport of the flight.
    - destination_city (str): The destination city of the flight.
    - destination_airport (str): The destination airport of the flight.
    - out_date (str): The departure date of the flight.
    - return_date (str): The return date of the flight.
    """

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
