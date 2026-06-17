# Graphology_flask
<p>This is a Flask web application that predicts personality traits based on handwriting analysis. The app leverages machine learning models that are trained on handwriting images and feature extraction across five Jupyter notebooks. Additionally, it includes a specialized model to determine whether a person is introverted or extroverted based on their Hindi handwriting.</p>

<h2>Features</h2>
<ul>
    <li><strong>Handwriting Analysis</strong>: The app processes handwriting samples and extracts features that reveal various personality traits.</li>
    <li><strong>Personality Trait Prediction</strong>: Uses models trained in multiple Jupyter notebooks to predict characteristics such as emotional stability, openness, and conscientiousness.</li>
    <li><strong>Hindi Handwriting Analysis</strong>: An additional feature that focuses on Hindi handwriting, predicting whether a person is introverted or extroverted.</li>
    <li><strong>Airwriting Recognition</strong>: Incorporates an airwriting feature (Notebook_4) to analyze handwriting traced in the air.</li>
    <li><strong>Machine Learning Models</strong>: Models are built using Support Vector Machines (SVMs) and trained across multiple notebooks for different aspects of personality analysis.</li>
</ul>

<h2>Usage</h2>
<ol>
    <li>Open the app in your browser at <code>http://localhost:5000</code>.</li>
    <li>Upload a handwriting image in the supported formats (PNG, JPG) or use the Air writing feature for English.</li>
    <li>The app will extract features and predict personality traits.</li>
</ol>

<h2>Notebooks</h2>
<ul>
    <li><strong>Notebook_1.ipynb</strong>: Handles the feature extraction from handwriting images. Extracts features like baseline angle, slant, letter size, and word spacing.</li>
    <li><strong>Notebook_2.ipynb</strong>: Processes and normalizes the extracted features to ensure consistency.</li>
    <li><strong>Notebook_3.ipynb</strong>: Trains SVM classifiers on the normalized features to predict personality traits.</li>
    <li><strong>Notebook_4.ipynb</strong>: Evaluates the model performance and includes airwriting feature analysis.</li>
    <li><strong>Notebook_5.ipynb</strong>: Integrates all aspects into a single model pipeline for the Flask app.</li>
    <li><strong>hindi_graphology.ipynb</strong>: Specialized notebook for analyzing Hindi handwriting and determining introversion or extroversion.</li>
</ul>
