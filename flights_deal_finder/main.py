from data_manager import DataManager
from flight_search import FlightSearch
import datetime
from notification_manager import NotificationManager

data_manager = DataManager()  # Create an instance of DataManager class
sheet_data = data_manager.get_destination_data()  # Get destination data from the sheet
flight_search = FlightSearch()  # Create an instance of FlightSearch class

ORIGIN_CITY_IATA = "LON"  # Define the origin city IATA code

# Update destination codes if missing in the sheet
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# Set the date for searching flights
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_month_from_today = datetime.datetime.now() + datetime.timedelta(days=180)

# Check flights for each destination
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # Send notification if the flight price is lower than the lowest price in the sheet
    if flight.price < destination["lowestPrice"]:
        send_sms(message=f"Low price alert! Only £{flight.price} to fly from "
                                              f"{flight.origin_city}-{flight.origin_airport} to "
                                              f"{flight.destination_city}-{flight.destination_airport}, "
                                              f"from {flight.out_date} to {flight.return_date}.")
