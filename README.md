# Fake News Detector

## Introduction
This is a simple web application built with Python's Flask framework. It uses a pre-trained machine learning model to classify a given text as either **"Real News"** or **"Fake News."** The user-friendly web interface allows for easy text input and real-time analysis.

## Features
* **Web Interface:** A clean and simple front-end for user interaction.
* **Real-time Prediction:** Get an instant result after submitting the text.
* **Machine Learning Powered:** Utilizes a pre-trained model for accurate text classification.

## Prerequisites
Before you begin, ensure you have the following installed on your system:
* Python 3.x
* `pip` (Python package installer)
* `Jupyter` Notebook (for exploring the training process)

## Installation
Follow these steps to set up and run the project on your local machine.

1.  **Clone the Repository**
    ```
    git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git)
    cd your-repository
    ```
    *(Note: Replace `https://github.com/your-username/your-repository.git` with your project's actual repository URL.)*

2.  **Install Required Libraries**
    Install the necessary Python libraries using `pip`:
    ```
    pip install Flask scikit-learn joblib jupyter pandas numpy seaborn matplotlib
    ```

3.  **Run the Application**
    From the root directory of your project, execute the following command in your terminal:
    ```
    python app.py
    ```

4.  **Access the Web App**
    Open your web browser and navigate to the following URL:
    `http://127.0.0.1:5000`

5.  **Explore the Model Training Process**
    You can open the `fake_news_detection.ipynb` file in Jupyter Notebook to see the step-by-step process of how the model was trained, evaluated, and saved. To do this, run the following command in your terminal:
    ```
    jupyter notebook
    ```
    Then, open the `fake_news_detection.ipynb` file from the Jupyter interface.

## File Structure
* `app.py`: The main Flask application file that handles routing and model prediction.
* `templates/`: This directory contains the HTML templates for the web interface.
    * `index.html`: The single page of the web application.
* `fake_news_model.pkl`: The pre-trained machine learning model saved as a serialized file.
* `fake_news_detection.ipynb`: The Jupyter Notebook containing the code used to train the model.
* `Fake.csv` & `True.csv`: The original datasets used to train and test the model.
* `Fake_cleaned.csv` & `True_cleaned.csv`: The cleaned versions of the datasets used for training.

## How It Works
The application uses a **trained machine learning model**, likely a classification model like a Logistic Regression or a Naive Bayes classifier, that has been trained on a large dataset of real and fake news articles. When you submit text, the `app.py` script sends the text to the model, which processes it and returns a prediction (0 for real, 1 for fake). The application then displays the corresponding result on the page. The Jupyter Notebook provides a detailed walkthrough of this training process, including data loading, cleaning, and model evaluation.
