# Background Removal with MediaPipe

This project implements a real-time background removal system using **MediaPipe Selfie Segmentation** and OpenCV.  
It replaces the background of your webcam feed with custom images and allows you to switch between them interactively.

---

## Features
- Real-time background removal using MediaPipe.
- Smooth mask blending with Gaussian blur.
- Adjustable segmentation threshold via trackbar.
- Keyboard controls to switch between multiple backgrounds.
- Side-by-side comparison of original vs processed frames.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/faisal-ajao/background-removal-mediapipe.git
cd background-removal-mediapipe

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\\Scripts\\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

Run the main script:
```bash
python main.py
```

### Controls
- ESC → Exit program  
- N / n → Next background  
- P / p → Previous background  
- Use the trackbar to adjust foreground segmentation threshold.

---

## Output Example (Video)  
[![Watch the output](https://img.youtube.com/vi/k5rxVd-4VRg/hqdefault.jpg)](https://youtu.be/k5rxVd-4VRg?feature=shared)

---

## Project Structure
```
background-removal-mediapipe/
├── backgrounds/           # Directory of background images
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
├── utils.py               # Utility for stacking images
├── main.py                # Main application script
├── README.md
└── requirements.txt
```

---

## Tech Stack
- Python 3.11.5
- OpenCV
- NumPy
- MediaPipe

---

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Install dependencies
```bash
pip install -r requirements.txt
```
