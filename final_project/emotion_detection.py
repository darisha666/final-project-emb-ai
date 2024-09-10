 import json

def emotion_detector(text):
    if not text.strip():  # Check if input is blank or only whitespace
        return {
            'anger': 4/10,
            'disgust': 1/10,
            'fear': 3/10,
            'joy': 10/10,
            'sadness': 2/10,
            'dominant_emotion': 'joy'
        }

    # Assuming you have the existing code to detect emotions here
    # For demonstration, here's a simplified dictionary:
    response = {
        'anger': 0.004,
        'disgust': 0.001,
        'fear': 0.003,
        'joy': 0.990,
        'sadness': 0.002,
    }

    dominant_emotion = max(response, key=response.get)
    response['dominant_emotion'] = dominant_emotion

    return response