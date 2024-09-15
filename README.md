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

1.Clone the Repository:

```bash
git clone https://github.com/mtptisid/Face-Recognization-with-Flask-App.git
cd Face-Recognization-with-Flask-App
```


2.Install Dependencies:
Make sure you have Python installed. Run the following command to install the required packages:

```bash
pip install -r requirements.txt
```


3.Add Face Images:
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



## Screenshots

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/c4b259e5-6ba0-4712-8217-a7d53e028af6" alt="Image 1" style="width: 48%;"/>
  <img src="https://github.com/user-attachments/assets/9e35d230-8acc-4ea8-b392-faf2dc7625d8" alt="Image 2" style="width: 48%;"/>
</div>

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/eb38965e-9122-4f3e-9d7f-80379659c212" alt="Image 1" style="width: 48%;"/>
  <img src="https://github.com/user-attachments/assets/ef5c36d7-e7bd-46d2-9d31-4f1c116381b6" alt="Image 2" style="width: 48%;"/>
</div>

- It will be Name UNKNOW for the non-known face.
<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/2de1e5d6-b406-44a7-9cc5-62e3c3f78afd" alt="Image 1" style="width: 48%;"/>
  <img src="https://github.com/user-attachments/assets/4555e433-97f6-4dae-b836-1e089df449c9" alt="Image 2" style="width: 48%;"/>
</div>



## To-Do

- Add more advanced face recognition features (e.g., emotion detection).
- Save captured images to the server with metadata like timestamp.
- Add authentication and user management to store personalized galleries for each user.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This is individual project created by Siddharamayya M
