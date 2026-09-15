from typing import TypedDict, Optional

class VoyagentState(TypedDict):

    """
    This is the single shared object that flows through every node in the
    LangGraph graph. Every agent reads from it and writes back to it —
    it's the 'memory' of one run of the pipeline.
    """

    # --- inputs, set once at the start of a run ---
    destination: str
    start_date: str
    end_date: str
    budget: float
    preferences: Optional[str]

    # --- filled in by HotelAgent / FlightAgent ---
    hotel_options: list
    flight_options: list
    selected_hotel: Optional[dict]
    selected_flight: Optional[dict]

    # --- filled in by BudgetAgent / ReviewerAgent ---    
    within_budget: Optional[bool]
    retry_count: int

    # --- filled in by GuideAgent ---
    guide_text: Optional[str]

    # --- filled in by BookingAgent ---
    total_cost: Optional[float]
    total_saved: Optional[float]
    approved: bool
