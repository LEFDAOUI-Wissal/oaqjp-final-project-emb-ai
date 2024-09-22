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
    
    # Return the 'text' attribute from the response JSON
    return response.json()

# Test the function (this line can be removed or commented out in production)
if __name__ == "__main__":
    result = emotion_detector("I love this new technology.")
    print(result)
