import requests

def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Define the input JSON
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to Watson NLP API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convert the response text into a dictionary
    response_dict = response.json()

    # Extract emotions from the response
    emotions = response_dict['emotionPredictions'][0]['emotion']  # Assuming the key 'emotion_predictions' holds emotion data
    
    # Extract the relevant emotions
    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0)
    }

    # Find the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Add the dominant emotion to the dictionary
    emotion_scores['dominant_emotion'] = dominant_emotion
    
    # Return the formatted output
    return emotion_scores

# Test the function (this line can be removed or commented out in production)
if __name__ == "__main__":
    result = emotion_detector("I am so happy I am doing this.")
    print(result)
