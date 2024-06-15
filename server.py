from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=['GET'])
def detect_emotion():
    # Get text to analyze from User
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)
    # Get response Data from Server
    emotions = emotion_detector(text_to_analyze)

    if emotions:
        response = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": emotions["dominant_emotion"]
        }

        responseText = f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}." 

        return render_template('index.html', responseText=responseText), 200
    else:
        return render_template('index.html', responseText="No emotions detected."), 400