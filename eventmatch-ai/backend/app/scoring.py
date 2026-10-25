import re

WEIGHTS = {"interest": .40, "skills": .25, "location": .20, "event_preference": .15}

def tags(value):
    if isinstance(value, list): raw = value
    else: raw = str(value or "").split("|")
    return {re.sub(r"\\s+", " ", str(x).strip().lower()) for x in raw if str(x).strip()}

def overlap(targets, profile):
    t, p = tags(targets), tags(profile)
    return len(t & p) / len(t) if t else .5

def score_profile(event, profile):
    interest = overlap(event.get("interests", []), profile.get("interests", ""))
    skills = overlap(event.get("skills", []), profile.get("skills", ""))
    city = str(event.get("city", "")).strip().lower()
    user_city = str(profile.get("city", "")).strip().lower()
    location = (1.0 if city == user_city else 0.0) if city else .5
    etype = str(event.get("event_type", "other")).strip().lower()
    prefs = tags(profile.get("preferred_event_types", ""))
    preference = (1.0 if etype in prefs else 0.0) if etype and etype != "other" else .5
    components = {
        "interest": round(interest*100, 1), "skills": round(skills*100, 1),
        "location": round(location*100, 1), "event_preference": round(preference*100, 1)
    }
    total = 100 * (interest*WEIGHTS["interest"] + skills*WEIGHTS["skills"] + location*WEIGHTS["location"] + preference*WEIGHTS["event_preference"])
    reasons = []
    if interest >= .5 and event.get("interests"): reasons.append("Interests overlap with the event topic")
    if skills >= .5 and event.get("skills"): reasons.append("Has relevant skills listed for the event")
    if location == 1: reasons.append("Located in the event city")
    if preference == 1: reasons.append("Prefers this type of event")
    if not reasons: reasons.append("Limited profile overlap; review before targeting")
    return {"score": round(total,1), "reasons": components, "explanation": reasons}
