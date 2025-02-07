# Medical Report Analysis - X-Ray Analysis

## Overview

Medical Report Analysis is a web-based application designed to analyze and interpret X-ray images. This project integrates deep learning and web technologies to provide accurate predictions based on uploaded X-ray images. The system leverages a pre-trained model for medical image classification, enhancing diagnostic capabilities.

## Features

- **X-ray Image Upload**: Upload X-ray images for analysis.
- **Deep Learning Model Integration**: Uses a trained `.h5` model to classify medical images.
- **Interactive Web Interface**: User-friendly web application for seamless interaction.
- **Visualization**: Displays analyzed results with insightful information.
- **Secure Storage**: Manages uploaded files securely.

## Project Structure

```
├── static/                  # Static files (CSS, JavaScript, etc.)
├── templates/               # HTML templates for the web application
├── uploads/                 # Directory to store uploaded X-ray images
├── app.py                   # Flask backend script
├── forms.py                 # Forms for user input handling
├── requirements.txt         # Dependencies
├── vercel.json              # Configuration for Vercel deployment
├── README.md                # Project documentation
├── X_RAY.ipynb              # Jupyter notebook for model training
```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/divyanshsaxena21/X-Ray_Analysis.git
   cd X-Ray_Analysis
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   - **Open X_RAY.ipynb in Jupyter Notebook.
   - **Follow the instructions inside the notebook to load the dataset, preprocess the data, train the convolutional neural network (CNN), and save the trained model.
   - **Save the trained model as model.h5 and place it inside the model/ directory.
   
3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Access the application locally at `http://127.0.0.1:5000`.

## Training the Model
1. Load Dataset:
   - **Ensure the dataset is available in the required directory.
   - **Modify the X_RAY.ipynb notebook to point to the correct dataset location.

2. Preprocess Data:
   - **Normalize the images and split the dataset into training and testing sets.
   - **Apply data augmentation techniques if necessary.

3. Train the Model:
   - **Use a convolutional neural network (CNN) for feature extraction.
   - **Train the model with appropriate hyperparameters (epochs, batch size, learning rate, etc.).
   - **Evaluate the model’s performance on the test set.

4. Save the Model:
   - **Once training is complete, save the trained model as model.h5 inside the model/ directory.
## Usage

1. Open the web application.
2. Upload an X-ray image (supported formats: `.jpg`, `.png`, `.jpeg`).
3. Click on the **Analyze** button.
4. View the prediction results and insights on the results page.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Deep Learning**: TensorFlow/Keras
- **Deployment**: Vercel
- **Notebook**: Jupyter Notebook for model training and testing

## Deployment

The application is deployed using **Vercel**, making it accessible online. Update the `vercel.json` file for custom deployment configurations.

## Screenshots

Include screenshots of the application interface and prediction results to give users a visual idea of the project.

## Contributing

Contributions are welcome! Please follow the steps below:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- Inspiration from advancements in medical image processing.
- Dataset and resources used for training the model.

