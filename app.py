from flask import Flask, render_template, request
import joblib

# Load the trained model pipeline
model = joblib.load('fake_news_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news_text']
        prediction = model.predict([news_text])
        
        # Interpret the prediction (0 for real, 1 for fake)
        result = 'Fake News' if prediction[0] == 1 else 'Real News'
        
        return render_template('index.html', prediction_result=result, news_text=news_text)

if __name__ == '__main__':
    app.run(debug=True)