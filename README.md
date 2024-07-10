Virtual Painter
===============

This project is a virtual painting tool that allows users to control brushes and erasers in a video feed using their fingers in the air. The tool provides smooth and intuitive drawing capabilities.

Table of Contents
-----------------

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

Introduction
------------

Virtual Painter is a project that leverages OpenCV and MediaPipe for hand tracking to create a virtual painting environment. Users can control brushes and erasers in a live video feed using their fingers, making it possible to draw and erase smoothly in the air.

Features
--------

- Hand tracking using OpenCV and MediaPipe.
- Brush and eraser tools controlled by finger gestures.
- Smooth and intuitive drawing experience.
- Dynamic adjustment of brush and eraser sizes.

Installation
------------

To run this project, you need to have Python installed along with the following libraries:

- OpenCV
- MediaPipe
- NumPy

You can install the required libraries using pip:

\`\`\`bash
pip install opencv-python mediapipe numpy
\`\`\`

Usage
-----

To use this project, follow these steps:

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/your-username/virtual-painter.git
   \`\`\`

2. Navigate to the project directory:
   \`\`\`bash
   cd virtual-painter
   \`\`\`

3. Run the hand tracking script:
   \`\`\`bash
   python HandTrack.py
   \`\`\`

4. Run the Virtual Painter script:
   \`\`\`bash
   python VirtualPainter.py
   \`\`\`

The \`HandTrack.py\` script will use your webcam to track hand movements, and the \`VirtualPainter.py\` script will enable the virtual painting environment.

Code Structure
--------------

- \`HandTrack.py\`: Contains the code for hand tracking using OpenCV and MediaPipe.
- \`VirtualPainter.py\`: Contains the code for controlling the virtual painting environment.

### HandTrack.py

This script is responsible for:
- Initializing the hand detector.
- Capturing video from the webcam.
- Tracking hand landmarks.
- Detecting fingers up and calculating distances.

### VirtualPainter.py

This script is responsible for:
- Setting up the virtual painting environment.
- Detecting finger gestures to control brush and eraser tools.
- Drawing and erasing on a canvas based on finger movements.
- Dynamically adjusting brush and eraser sizes based on finger positions.

Contributing
------------

Contributions are welcome! If you have any improvements or suggestions, please open an issue or create a pull request.
