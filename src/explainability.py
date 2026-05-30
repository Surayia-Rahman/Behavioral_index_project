
def explain_bvi(personality, fatigue):

    P = (
        0.25 * personality["self_focus"] +
        0.20 * personality["dominance"] +
        0.25 * personality["aggression"] +
        0.15 * personality["emotional_intensity"] +
        0.15 * (1 - personality["social_focus"])
    )

    F = fatigue["fatigue_score"]

    interaction = F * P

    contributions = {
        "fatigue": 0.40 * F,
        "personality": 0.35 * P,
        "interaction": 0.25 * interaction
    }

    total = sum(contributions.values())

    return {k: (v / total) * 100 for k, v in contributions.items()}
