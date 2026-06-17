from flask import Flask, render_template, request, redirect, url_for, send_file
import subprocess
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Ensure the upload folder exists
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home route to display the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle language selection
@app.route('/language_selection/<language>', methods=['POST'])
def language_selection(language):
    if language == 'hindi':
        return redirect(url_for('hindi_processing'))
    return redirect(url_for('index'))

# Route to start capturing handwriting
@app.route('/start_capture', methods=['POST'])
def start_capture():
    # Run Notebook_4 to capture handwriting using MediaPipe and save Canvas.png
    notebook_4_path = os.path.join(os.getcwd(), 'Notebook_4.ipynb')
    try:
        subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_4_path, '--output', 'Notebook_4_output.ipynb'], check=True)
    except subprocess.CalledProcessError as e:
        return render_template('error.html', error_message=f"Error executing Notebook_4: {e}")
    
    return redirect(url_for('show_result'))

# Route to process the captured handwriting and predict personality traits
@app.route('/show_result')
def show_result():
    notebook_5_path = os.path.join(os.getcwd(), 'Notebook_5.ipynb')
    try:
        subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_5_path, '--output', 'Notebook_5_output.ipynb'], check=True)
    except subprocess.CalledProcessError as e:
        return render_template('error.html', error_message=f"Error executing Notebook_5: {e}")
    
    result_file_path = os.path.join(os.getcwd(), 'result.txt')
    if os.path.exists(result_file_path):
        with open(result_file_path, 'r') as f:
            captured_output = f.read()
    else:
        captured_output = "No result found. Please try again."

    return render_template('result.html', captured_output=captured_output)

@app.route('/english_selection')
def english_selection():
    return render_template('english_selection.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Simply render the 'coming soon' page instead of analyzing the image
    return render_template('coming_soon.html')

# Route to download image
@app.route('/download_image')
def download_image():
    return send_file(os.path.join('static', 'Canvas.png'), as_attachment=True)

# Route for Hindi processing page
@app.route('/hindi_processing')
def hindi_processing():
    return render_template('hindi_processing.html')

# Route to handle Hindi image upload and processing
@app.route('/process_hindi_image', methods=['POST'])
def process_hindi_image():
    if 'image' not in request.files:
        return render_template('error.html', error_message="No file part")
    
    file = request.files['image']
    if file.filename == '':
        return render_template('error.html', error_message="No selected file")
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Process the image with your model
        result = analyze_image(file_path)
        
        return render_template('hindi_result.html', result=result)

def analyze_image(image_path):
    # Load and preprocess the image
    image = Image.open(image_path)
    image = image.resize((128, 128))  # Resize to match the model's expected input shape
    image_array = np.array(image)
    image_array = image_array / 255.0  # Normalize the image
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Load the model
    model = tf.keras.models.load_model(r'C:\Users\gaura\OneDrive\Desktop\hackathon-backend\graphology_model_final_transfer.h5')

    # Make predictions
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    # Map the predicted class to the corresponding personality trait
    if predicted_class == 0:
        return "Introvert"
    else:
        return "Extrovert"

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)

#********************************************************************************************************

# from flask import Flask, render_template, request, redirect, url_for, send_file
# import subprocess
# import os

# app = Flask(__name__)

# # Home route to display the index page
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to start capturing handwriting
# @app.route('/start_capture', methods=['POST'])
# def start_capture():
#     # Run Notebook_4 to capture handwriting using MediaPipe and save Canvas.png
#     notebook_4_path = os.path.join(os.getcwd(), 'Notebook_4.ipynb')
#     try:
#         subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_4_path, '--output', 'Notebook_4_output.ipynb'], check=True)
#     except subprocess.CalledProcessError as e:
#         return render_template('error.html', error_message=f"Error executing Notebook_4: {e}")
    
#     # Redirect to result page
#     return redirect(url_for('show_result'))

# # Route to process the captured handwriting and predict personality traits
# @app.route('/show_result')
# def show_result():
#     try:
#         # Run Notebook_5 to analyze the handwriting image (Canvas.png)
#         notebook_5_path = os.path.join(os.getcwd(), 'Notebook_5.ipynb')
#         try:
#             subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_5_path, '--output', 'Notebook_5_output.ipynb'], check=True)
#         except subprocess.CalledProcessError as e:
#             return render_template('error.html', error_message=f"Error executing Notebook_5: {e}")

#         # Read captured output from result.txt
#         result_file_path = os.path.join(os.getcwd(), 'result.txt')
#         if os.path.exists(result_file_path):
#             with open(result_file_path, 'r') as f:
#                 captured_output = f.read()
#         else:
#             captured_output = "No result found. Please try again."

#         return render_template('result.html', captured_output=captured_output)
    
#     except Exception as e:
#         return render_template('error.html', error_message=f"An unexpected error occurred: {e}")

# # Route to download the captured Canvas.png
# @app.route('/download_image')
# def download_image():
#     return send_file(os.path.join('static', 'Canvas.png'), as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)

#-------------------------------------------------------------------------------------------------------------


# from flask import Flask, render_template, redirect, url_for,request
# import subprocess
# import os

# app = Flask(__name__)

# # Home route to display the index page
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/language_selection/<language>', methods=['POST'])
# def language_selection(language):
#     if language == 'hindi':
#         # Render the Hindi processing page
#         return render_template('hindi_processing.html')

# @app.route('/start_capture', methods=['POST'])
# def start_capture():
#     # Run Notebook_4 to capture handwriting using MediaPipe and save Canvas.png
#     notebook_4_path = os.path.join(os.getcwd(), 'Notebook_4.ipynb')
#     try:
#         subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_4_path, '--output', 'Notebook_4_output.ipynb'], check=True)
#     except subprocess.CalledProcessError as e:
#         return render_template('error.html', error_message=f"Error executing Notebook_4: {e}")
    
#     # Redirect to result page
#     return redirect(url_for('show_result'))

# # Route to process and show results (as before)
# @app.route('/show_result')
# def show_result():
#     notebook_5_path = os.path.join(os.getcwd(), 'Notebook_5.ipynb')
#     try:
#         subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_5_path, '--output', 'Notebook_5_output.ipynb'], check=True)
#     except subprocess.CalledProcessError as e:
#         return render_template('error.html', error_message=f"Error executing Notebook_5: {e}")
    
#     result_file_path = os.path.join(os.getcwd(), 'result.txt')
#     if os.path.exists(result_file_path):
#         with open(result_file_path, 'r') as f:
#             captured_output = f.read()
#     else:
#         captured_output = "No result found. Please try again."

#     return render_template('result.html', captured_output=captured_output)

# # Route to download image (if needed)
# @app.route('/download_image')
# def download_image():
#     return send_file(os.path.join('static', 'Canvas.png'), as_attachment=True)

# # Hindi processing placeholder
# @app.route('/hindi_processing')
# def hindi_processing():
#     return render_template('hindi_processing.html')

# if __name__ == '__main__':
#     app.run(debug=True)

#*******************************************************************************************************