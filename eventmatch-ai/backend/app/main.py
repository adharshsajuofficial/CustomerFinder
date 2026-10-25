from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import MatchRequest
from .data import load_profiles
from .scoring import score_profile

app = FastAPI(title="EventMatch AI API", version="0.1.0",
              description="Explainable event-to-audience matching with fictional demo data.")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/api/health")
def health():
    return {"status":"ok","service":"EventMatch AI API"}

@app.get("/api/events/examples")
def examples():
    return {"events":[
      {"title":"AI Buildathon","description":"Build AI and machine learning projects","city":"Thiruvananthapuram","interests":["AI","machine learning","hackathons","coding"],"skills":["Python","machine learning","React"],"event_type":"hackathon","max_results":10},
      {"title":"Design for Good Workshop","description":"UX, visual design and social impact","city":"Kochi","interests":["design","UX","social impact","creativity"],"skills":["Figma","UI design","research"],"event_type":"workshop","max_results":10},
      {"title":"Startup Networking Meetup","description":"Meet founders and product builders","city":"Kozhikode","interests":["startups","entrepreneurship","business","networking"],"skills":["pitching","marketing","product management"],"event_type":"meetup","max_results":10}
    ]}

@app.post("/api/match")
def match(req: MatchRequest):
    event = req.event.model_dump()
    try: profiles = load_profiles()
    except (FileNotFoundError, ValueError) as e: raise HTTPException(500, str(e))
    result = []
    for p in profiles:
        s = score_profile(event, p)
        result.append({"user_id":str(p["user_id"]), "display_name":str(p["display_name"]),
          "city":str(p["city"]), "interests":[x for x in str(p["interests"]).split("|") if x],
          "skills":[x for x in str(p["skills"]).split("|") if x],
          "preferred_event_types":[x for x in str(p["preferred_event_types"]).split("|") if x],
          "score":s["score"], "reasons":s["reasons"], "explanation":s["explanation"]})
    result.sort(key=lambda x:(-x["score"],x["user_id"]))
    result = result[:event["max_results"]]
    return {"event_title":event["title"],"total_profiles":len(profiles),
      "returned_matches":len(result),
      "scoring_note":"Prototype relevance score, not a probability of registration. Profiles are fictional.",
      "matches":result}
