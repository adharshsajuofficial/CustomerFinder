from app.scoring import score_profile

def test_relevant_profile_scores_higher():
    event={"interests":["AI","hackathons"],"skills":["Python"],"city":"Thiruvananthapuram","event_type":"hackathon"}
    strong={"interests":"AI|hackathons|coding","skills":"Python|React","city":"Thiruvananthapuram","preferred_event_types":"hackathon|workshop"}
    weak={"interests":"cooking|gardening","skills":"baking","city":"Kochi","preferred_event_types":"meetup"}
    assert score_profile(event,strong)["score"] > score_profile(event,weak)["score"]

def test_empty_event_signals_are_neutral():
    event={"interests":[],"skills":[],"city":"","event_type":"other"}
    profile={"interests":"AI","skills":"Python","city":"Kochi","preferred_event_types":"hackathon"}
    assert score_profile(event,profile)["score"] == 50.0
