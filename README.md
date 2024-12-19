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
├── model.h5                 # Trained deep learning model
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

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Access the application locally at `http://127.0.0.1:5000`.

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

## Model Details

- The `model.h5` file is a deep learning model trained on medical X-ray datasets.
- It utilizes convolutional neural networks (CNNs) for feature extraction and classification.
- Training details are available in the `X_RAY.ipynb` file.

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

