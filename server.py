from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_analyzer():
    
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return "Invalid text! Please try again."
    
    response = emotion_detector(text_to_analyze)
    
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    output_string = (
        "For the given statement, the system response is "
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. "
        "The dominant emotion is {}."
    ).format(anger, disgust, fear, joy, sadness, dominant_emotion)
    
    return output_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)