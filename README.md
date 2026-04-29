# emotion-detection-app
This project is an AI-based web application that analyzes text to detect and extract underlying emotions.
Built using Python and the Flask framework, the application integrates with the IBM Watson NLP (Natural Language Processing) API to evaluate user-provided statements and determine the emotional tone.

Key Features:

Emotion Analysis: Processes text to extract confidence scores for five primary emotions: anger, disgust, fear, joy, and sadness, ultimately identifying the dominant emotion.

Web Interface: Provides a simple, interactive web page where users can submit text and view the analysis results in real time.

Error Handling: Gracefully manages invalid, empty, or unprocessable inputs by returning user-friendly error messages and handling HTTP 400 status codes.

Robust Architecture: Packaged as a modular Python application (EmotionDetection) and thoroughly verified using unit testing and static code analysis (Pylint).

Technologies Used: Python, Flask, Requests Library, IBM Watson NLP API.
