from typing import Dict

FORTUNE_PREDICTIONS: Dict[str, Dict[str, str]] = {
    "monday": {
        "general": "You are a natural leader with great determination.",
        "today": "Today brings new opportunities for growth and success.",
        "love": "Your relationships will flourish with patience and understanding.",
        "career": "A promising career opportunity may present itself soon.",
        "health": "Focus on maintaining a balanced lifestyle for optimal health."
    },
    "tuesday": {
        "general": "You possess great energy and enthusiasm for life.",
        "today": "Today is perfect for starting new projects or ventures.",
        "love": "Your charm will attract positive attention in relationships.",
        "career": "Your hard work will be recognized and rewarded.",
        "health": "Stay active and maintain your exercise routine."
    },
    "wednesday": {
        "general": "You have excellent communication skills and adaptability.",
        "today": "Today brings clarity to important decisions.",
        "love": "Open communication will strengthen your relationships.",
        "career": "Your creative ideas will be well-received.",
        "health": "Focus on mental well-being and stress management."
    },
    "thursday": {
        "general": "You are blessed with wisdom and good judgment.",
        "today": "Today is favorable for learning and personal growth.",
        "love": "Your relationships will benefit from your wisdom.",
        "career": "Your expertise will be valuable to others.",
        "health": "Maintain a balanced diet and regular exercise."
    },
    "friday": {
        "general": "You bring joy and happiness to those around you.",
        "today": "Today brings good fortune and positive outcomes.",
        "love": "Your relationships will be filled with joy and harmony.",
        "career": "Success comes through your positive attitude.",
        "health": "Your natural optimism contributes to good health."
    },
    "saturday": {
        "general": "You have a strong sense of responsibility and reliability.",
        "today": "Today is good for completing tasks and projects.",
        "love": "Your dedication will strengthen your relationships.",
        "career": "Your reliability will lead to career advancement.",
        "health": "Focus on maintaining a regular routine."
    },
    "sunday": {
        "general": "You possess great creativity and spiritual awareness.",
        "today": "Today brings peace and spiritual growth.",
        "love": "Your relationships will deepen with understanding.",
        "career": "Your creative talents will be recognized.",
        "health": "Balance physical and spiritual well-being."
    }
}

def get_fortune(day: str, aspect: str = "general") -> str:
    """
    Get fortune prediction based on birth day and aspect of life.
    
    Args:
        day (str): Day of the week (case insensitive)
        aspect (str): Aspect of life to predict (general, today, love, career, health)
    
    Returns:
        str: Fortune prediction
    """
    day = day.lower()
    aspect = aspect.lower()
    
    if day not in FORTUNE_PREDICTIONS:
        return "Invalid day of the week. Please provide a valid day (Monday through Sunday)."
    
    if aspect not in FORTUNE_PREDICTIONS[day]:
        return "Invalid aspect. Please choose from: general, today, love, career, health."
    
    return FORTUNE_PREDICTIONS[day][aspect] 