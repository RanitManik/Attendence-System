# Facial Recognition Attendance System

<div>
    
  ![GitHub Created At](https://img.shields.io/github/created-at/RanitManik/Attendence-System)
  ![GitHub repo size](https://img.shields.io/github/repo-size/RanitManik/Attendence-System)
  ![GitHub Discussions](https://img.shields.io/github/discussions/RanitManik/Attendence-System)
  ![GitHub License](https://img.shields.io/github/license/RanitManik/Attendence-System)
  ![wakatime](https://wakatime.com/badge/github/RanitManik/Attendence-System.svg)
  
</div>

Welcome to the Facial Recognition Attendance System v1.0 created by Ranit Manik. This project uses Python, Flask,
OpenCV, and face_recognition to create an attendance system that recognizes faces and records attendance.


## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Recognizes faces using `face_recognition`.
- Captures attendance and stores it in a CSV file.
- Runs a web server using Flask to display the video feed.

## Requirements

- Python 3.0+
- Flask
- OpenCV
- face_recognition
- numpy
- gunicorn

## Installation

1. **Clone the repository:**

      ```bash
      git clone https://github.com/yourusername/facial-recognition-attendance-system.git
      cd facial-recognition-attendance-system
      ```

2. **Create and activate a virtual environment:**

      ```bash
      python3 -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```

3. **Install the dependencies:**

      ```bash
      pip install -r requirements.txt
      ```

4. **Run the application:**

      ```bash
      python3 app.py
      ```

## Usage

Once the application is running, you can access the video feed at `http://localhost:5000/video_feed`. The application
will detect faces and record attendance in a CSV file named with the current date.

## Contributing

Feel free to fork the project and submit pull requests. For major changes, please open an issue first to discuss what
you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
