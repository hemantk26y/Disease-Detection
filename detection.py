from flask import Flask, render_template, request
from pymongo import MongoClient
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['health_data']
covid_collection = db['covid_data']
pneum_model_github_13epochs_collection = db['pneum_model_github_13epochs_data']

# Load the models
covid_model = load_model('covid_model.h5')
pneum_model_github_13epochs_model = load_model('pneum_model_github_13epochs.h5')

# Helper function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for the main form
@app.route('/')
def index():
    return render_template('home.html')

# Route for COVID detection form
@app.route('/covid_form', methods=['GET', 'POST'])
def covid_form():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        email = request.form['email']
        phone_number = request.form['phone_number']
        age = request.form['age']

        # Save the uploaded image
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                extension = file.filename.rsplit('.', 1)[1].lower()
                filename = f"{first_name}_{last_name}.{extension}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                # Run COVID model prediction
                prediction = run_covid_prediction(file_path)

                # Save data to MongoDB
                covid_data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'gender': gender,
                    'email': email,
                    'phone_number': phone_number,
                    'age': age,
                    'image': filename,
                    'prediction': prediction
                }
                covid_collection.insert_one(covid_data)

                return render_template('result.html',
                                       prediction=prediction,
                                       first_name=first_name,
                                       last_name=last_name,
                                       gender=gender,
                                       age=age,
                                       filename=filename)

    return render_template('COVID.html')

# Route for pneum_model_github_13epochs disease form
@app.route('/pneum_model_github_13epochs_form', methods=['GET', 'POST'])
def pneum_model_github_13epochs_form():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        email = request.form['email']
        phone_number = request.form['phone_number']
        age = request.form['age']

        # Save the uploaded image
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                extension = file.filename.rsplit('.', 1)[1].lower()
                filename = f"{first_name}_{last_name}_{phone_number}.{extension}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                # Run pneum_model_github_13epochs disease model prediction
                prediction = run_pneum_model_github_13epochs_prediction(file_path)

                # Save data to MongoDB
                pneum_model_github_13epochs_data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'gender': gender,
                    'email': email,
                    'phone_number': phone_number,
                    'age': age,
                    'image': filename,
                    'prediction': prediction
                }
                pneum_model_github_13epochs_collection.insert_one(pneum_model_github_13epochs_data)

                return render_template('result.html',
                                       prediction=prediction,
                                       first_name=first_name,
                                       last_name=last_name,
                                       gender=gender,
                                       age=age,
                                       filename=filename)
    return render_template('Pneumonia.html')

# Function to run COVID model prediction
def run_covid_prediction(image_location):
    img = Image.open(image_location).convert('RGB')
    img = img.resize((224, 224))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0
    prediction = covid_model.predict(x)
    if prediction.any() < 0.5:
        return 'COVID Positive'
    else:
        return 'COVID Negative'

# Function to run pneum_model_github_13epochs disease model prediction
def run_pneum_model_github_13epochs_prediction(image_location):
    img = Image.open(image_location).convert('RGB')
    img = img.resize((150, 150))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0
    prediction = pneum_model_github_13epochs_model.predict(x)
    if prediction.any() < 0.5:
        return 'Pneumonia Disease Present'
    else:
        return 'No Pneumonia Disease'


@app.route("/About")
def about():
    return render_template('about.html')


@app.route("/Contact")
def Contact():
    return render_template('Contact.html')


@app.route("/Pneumonia")
def Pneumonia():
    return render_template('Pneumonia.html')


@app.route("/COVID")
def COVID():
    return render_template('COVID.html')


if __name__ == '__main__':
    app.run(debug=True)
