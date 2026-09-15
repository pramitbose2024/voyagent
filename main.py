from src.voyagent.graph import build_graph


def run_sample_trip():

    graph = build_graph()

    initial_state = {
        "destination": "London",
        "start_date": "2026-09-10",
        "end_date": "2026-09-15",
        "budget": 900.0,
        "preferences": "food & culture",
        "hotel_options": [],
        "flight_options": [],
        "selected_hotel": None,
        "selected_flight": None,
        "within_budget": None,
        "retry_count": 0,
        "guide_text": None,
        "total_cost": None,
        "total_saved": None,
        "approved": False
    }

    print("=" * 50)
    print("Running Voyagent...")
    print("=" * 50)

    final_state = graph.invoke(initial_state)

    print("=" * 50)
    print("Final state:")
    for key, value in final_state.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    run_sample_trip()