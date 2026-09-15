from langgraph.graph import StateGraph, START, END
from src.voyagent.state import VoyagentState


def supervisor(state: VoyagentState) -> VoyagentState:

    """
    Entry point node. It's a pass-through — it doesn't change
    anything in state. Its job right now just to prove the graph
    has a real starting node. Later, this is where the routing
    logic (e.g. skip flight search if the user already has a flight) would be added.
    """

    print(f"[supervisor] Starting trip planning for {state['destination']}.")
    return state


def hotel_agent_placeholder(state: VoyagentState) -> VoyagentState:

    """Dummy node — real HotelAgent logic gets written on Day 2."""

    print(f"[hotel_agent] (Placeholder - logic will get written on Day 2)")
    return state


def flight_agent_placeholder(state: VoyagentState) -> VoyagentState:

    """Dummy node — real FlightAgent logic gets written on Day 2."""

    print(f"[flight_agent] (Placeholder - logic will get written on Day 2)")
    return state


def build_graph():

    """
    Builds and compiles the LangGraph StateGraph.

    A StateGraph is just nodes (functions that take state and return
    state) connected by edges (which node runs after which). Today's
    graph is intentionally trivial — one straight line — so you can
    verify the *mechanics* of LangGraph work before adding any real
    logic on top.
    """

    graph = StateGraph(VoyagentState)

    # Register each node under a name the graph will refer to.
    graph.add_node("supervisor", supervisor)
    graph.add_node("hotel_agent", hotel_agent_placeholder)
    graph.add_node("flight_agent", flight_agent_placeholder)

    # Wire the edges: START → supervisor → hotel_agent → flight_agent → END
    graph.add_edge(START, "supervisor")
    graph.add_edge("supervisor", "hotel_agent")
    graph.add_edge("hotel_agent", "flight_agent")
    graph.add_edge("flight_agent", END)

    # .compile() turns the graph definition into something runnable.
    return graph.compile()
