from flask import Flask, render_template, request
from image_processing import process_image

app = Flask(__name__)

app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfYXGMpAAAAAF4prpNKDsWXWdLkfLmXHzK3JTK7'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfYXGMpAAAAAK5jj6PsFBo5pJ8079Diyssgp0Gp'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}

# app.py
from flask import Flask, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    contrast_level = float(request.form['contrast_level'])
    image_file = request.files['image_file']
    if image_file:
        image_path = 'static/histograms.jpg'
        image_file.save(image_path)
        processed_image_path = process_image(image_path, contrast_level)
        return render_template('index.html', processed_image=processed_image_path)
    return render_template('index.html')
