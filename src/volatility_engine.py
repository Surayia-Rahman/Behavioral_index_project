
# Core interaction model:
# Fatigue × Personality instability

def compute_personality_instability(p):

    return (
        0.25 * p["self_focus"] +
        0.20 * p["dominance"] +
        0.25 * p["aggression"] +
        0.15 * p["emotional_intensity"] +
        0.15 * (1 - p["social_focus"])
    )

def compute_bvi(personality, fatigue):

    F = fatigue["fatigue_score"]
    P = compute_personality_instability(personality)

    interaction = F * P

    bvi = (
        0.40 * F +
        0.35 * P +
        0.25 * interaction
    )

    return {
        "fatigue": F,
        "personality_instability": P,
        "interaction": interaction,
        "BVI": bvi * 100
    }
