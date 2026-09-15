from src.voyagent.data.mock_hotels import get_mock_hotels
from src.voyagent.data.mock_flights import get_mock_flights


def test_get_mock_hotels_returns_results_for_known_city():
    hotels = get_mock_hotels("New York")
    assert len(hotels) > 0

def test_get_mock_hotels_is_case_insensitive():

    hotels_lower = get_mock_hotels("london")
    hotels_mixed = get_mock_hotels("London")
    
    assert hotels_lower == hotels_mixed

def test_get_mock_hotels_returns_empty_list_for_unknown_city():
    hotels = get_mock_hotels("Antarctica")
    assert hotels == []

def test_hotel_entries_have_required_fields():

    hotels = get_mock_hotels("Tokyo")
    required_fields = {"name", "price", "list_price", "rating", "review_count"}
    for hotel in hotels:
        assert required_fields.issubset(hotel.keys())

def test_get_mock_flights_returns_results_for_known_city():
    flights = get_mock_flights("New York")
    assert len(flights) > 0

def test_get_mock_flights_returns_empty_list_for_unknown_city():
    flights = get_mock_flights("Kolkata")
    assert flights == []

def test_flight_entries_have_required_fields():

    flights = get_mock_flights("London")
    required_fields = {"airline", "price", "list_price", "departure", "arrival", "stops"}
    for flight in flights:
        assert required_fields.issubset(flight.keys())

def test_hotel_prices_are_never_negative_discounts():

    """Sanity check: list_price should never be less than price."""

    for city_hotels in [get_mock_hotels("paris"), get_mock_hotels("tokyo"), get_mock_hotels("new york")]:
        for hotel in city_hotels:
            assert hotel["list_price"] >= hotel["price"]