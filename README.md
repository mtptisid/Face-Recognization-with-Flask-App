# Flask Face Recognition App

This project is a Flask-based web application that performs live face recognition using OpenCV and the `face_recognition` library. The app captures live video from your webcam, detects and recognizes faces, and allows you to capture images from the video feed. The captured images are displayed in a gallery where they can be previewed and deleted with a hover effect.

## Features

- **Live Video Feed**: Streams live video from your webcam.
- **Face Recognition**: Real-time recognition of known faces using the `face_recognition` library.
- **Capture Images**: Capture images from the video feed and add them to a gallery.
- **Image Gallery with Delete Option**: Displays captured images with a delete button on hover.
- **Dark Themed Interface**: The application features a modern dark theme using Bootstrap.

## Requirements

Make sure you have the following installed before running the project:

- **Python 3.x**
- **Flask**
- **OpenCV** (`cv2`)
- **face_recognition**
- **NumPy**

### Install dependencies:

Use the following command to install the required Python libraries:

```bash
pip install flask opencv-python face_recognition numpy
```


Installation and Setup

	1.	Clone the Repository:

```bash
git clone https://github.com/your-username/flask-face-recognition-app.git
cd flask-face-recognition-app
```


	2.	Install Dependencies:
Make sure you have Python installed. Run the following command to install the required packages:

```bash
pip install -r requirements.txt
```


3.	Add Face Images:
	•	Create a folder for each person in the project directory.
	•	Add their images to these folders.
	
4. Run the Application:
Run the Flask app using:

```bash
python app.py
```


## Access the Application

Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the app.

## Usage

- Once the application is running, it will start capturing live video from your webcam.
- If the face is recognized, the person’s name will be displayed on the video feed.
- You can capture an image by clicking the **Capture Image** button, and it will be displayed in the gallery on the right side of the page.
- Hover over an image in the gallery to reveal the delete button. Click on it to remove the image.

## Preview

## Screenshots

## To-Do

- Add more advanced face recognition features (e.g., emotion detection).
- Save captured images to the server with metadata like timestamp.
- Add authentication and user management to store personalized galleries for each user.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.