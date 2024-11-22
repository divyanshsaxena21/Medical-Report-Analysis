from flask import Flask, render_template, request, redirect, url_for
from forms import InputForm
import os
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Initialize the Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

# Directory to save uploaded images in the static folder
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Load the pre-trained model
model = load_model('model.h5')

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Ensure the upload directory exists (for both local and deployment)
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title="Home")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = InputForm()

    if form.validate_on_submit():
        if 'image' not in request.files:
            return redirect(request.url)

        file = request.files['image']
        
        if file.filename == '' or not allowed_file(file.filename):
            return redirect(request.url)

        if file:
            # Save the image to the static folder
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            # Open and preprocess the image
            image = Image.open(filename)
            image = image.resize((150, 150))  # Resize the image to 150x150 (or whatever size your model expects)
            image = np.array(image)

            # If the image is grayscale, convert it to RGB (3 channels)
            if len(image.shape) == 2:
                image = np.stack([image] * 3, axis=-1)

            # Normalize the image to the range [0, 1] (this depends on how your model was trained)
            image = image / 255.0

            # Add a batch dimension to the image (the model expects a batch of images)
            image = np.expand_dims(image, axis=0)

            # Make the prediction
            prediction = model.predict(image)

            # Define your labels
            labels = ["COVID-19", "Pneumonia", "Normal", "Tuberculosis"]

            # Get the predicted class index and map it to the label
            predicted_class_index = np.argmax(prediction, axis=1)[0]  # Get the index of the highest probability
            predicted_class = labels[predicted_class_index]  # Map index to label

            # Render the result, passing the filename relative to the static folder
            return render_template('prediction_result.html', prediction=predicted_class, image_url=url_for('static', filename=f'uploads/{file.filename}'))

    return render_template('predict.html', title="Predict", form=form)

if __name__ == "__main__":
    app.run(debug=True)
