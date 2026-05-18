# Real-Time Edge Detection and Morphological Filtering
### Computer Vision — Week 2 Assignment

---

## Project Objective

This project implements a real-time computer vision pipeline that detects the boundaries of objects in a live webcam feed. Using Python and OpenCV, the system captures video frames, identifies edges within each frame, and applies morphological operations to refine those edges — all in real time.

The goal is to demonstrate how a robot can be programmed to "see" and interpret its environment by processing raw camera input into structured visual data.

---

## Robotics Business Scenario

A logistics company is deploying robotic arms on a warehouse picking line. Each robot must identify the edges and boundaries of packages moving along a conveyor belt in order to calculate grip points and avoid collisions.

Rather than hardcoding the shape of every possible package, the robot uses a live camera feed and an edge detection pipeline to adapt to any object it encounters. This approach reduces setup time, lowers programming costs, and increases operational flexibility — making it a practical solution for dynamic warehouse environments.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| OpenCV (`opencv-python`) | Video capture, image processing, and display |
| NumPy | Kernel matrix construction for morphological operations |

---

## Installation

**Step 1 — Confirm Python is installed:**
```bash
python --version
```
Python 3.7 or higher is required.

**Step 2 — Install dependencies:**
```bash
pip install -r requirements.txt
```

This installs `opencv-python` and `numpy`.

---

## How to Run the Script

Navigate to the project folder in your terminal and run:

```bash
python edge_detection.py
```

Four windows will open simultaneously, each showing a different stage of the processing pipeline applied to the live webcam feed.

---

## How to Exit the Program

Press the **`q`** key while any of the four display windows is active. The script will stop the webcam, close all windows, and exit cleanly.

---

## Workflow Explanation

The script processes each webcam frame through the following six steps:

**1. Webcam Capture**
The script opens the default system camera using `cv2.VideoCapture(0)`. It reads one frame at a time inside a continuous loop. If the camera cannot be opened, an error message is displayed and the script exits.

**2. Grayscale Conversion**
Each colour frame is converted from BGR (Blue, Green, Red) format to grayscale using `cv2.cvtColor()`. This reduces the image to a single brightness channel. Canny edge detection operates on grayscale data, and working with one channel instead of three also improves processing speed.

**3. Canny Edge Detection**
The grayscale frame is passed to `cv2.Canny()` with a lower threshold of 100 and an upper threshold of 200. The algorithm calculates how sharply brightness changes between neighbouring pixels. Pixels where the change is strong enough are marked as edges; all others are discarded. The result is a black-and-white image where white pixels represent detected boundaries.

**4. Dilation**
The edge image is processed with `cv2.dilate()` using a 5×5 kernel. Dilation expands each white edge pixel outward, which thickens boundary lines and closes small gaps that may have appeared in the edge map. This is useful when a robot needs a complete, unbroken outline to calculate an accurate grip point.

**5. Erosion**
The edge image is also processed with `cv2.erode()` using the same 5×5 kernel. Erosion shrinks each white edge pixel inward, removing thin noise filaments and stray pixels that do not belong to a real boundary. This produces a cleaner, more precise edge map.

**6. Real-Time Display**
All four versions of the frame are displayed simultaneously in separate windows using `cv2.imshow()`. The windows update with every new frame, producing a smooth real-time view of the pipeline in action.

---

## Expected Visual Results

When the script is running you will see four windows:

| Window | What You Will See |
|---|---|
| **Original Frame** | The live colour video feed from your webcam |
| **Edges** | A black image with white lines tracing object boundaries |
| **Dilated Edges** | The same edge lines, slightly thicker and with gaps filled |
| **Eroded Edges** | The same edge lines, slightly thinner and with noise removed |

Edges will appear around objects with well-defined boundaries — hands, books, mugs, and the edges of a desk or monitor are all clearly detected.

---

## Troubleshooting

**The script opens but the windows are black or show no image:**
Ensure your webcam is not being used by another application such as Zoom or Teams. Close those applications and re-run the script.

**Error: Could not open webcam:**
Your system may use a different camera index. Change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` in `edge_detection.py` and try again.

**The pip install command fails:**
Try prefixing with `python -m`:
```bash
python -m pip install -r requirements.txt
```

**The windows appear but performance is slow or laggy:**
Close other running applications to free up CPU resources. This script requires no GPU and runs on standard hardware, but a heavily loaded machine may reduce frame rate.

---

## Business Value of Real-Time Edge Detection in Robotics

Real-time edge detection addresses a fundamental challenge in robotics: giving machines reliable spatial awareness without manual programming.

**Operational flexibility.** A robot using edge detection can handle objects it has never encountered before. It does not need a pre-loaded library of object shapes — it derives boundary information directly from the camera feed on every frame.

**Cost reduction.** Traditional machine vision systems require expensive structured lighting, precise conveyor positioning, and per-product calibration. An edge detection pipeline runs on a standard webcam and a laptop-grade CPU, dramatically lowering the hardware barrier to entry.

**Faster deployment.** New product lines or package types can be introduced to a robotic picking system without reprogramming. The vision pipeline adapts automatically, reducing changeover time from hours to minutes.

**Foundation for advanced automation.** Edge detection is the first step in a larger perception stack. The clean boundary data it produces feeds directly into object classification, depth estimation, and path planning systems — making it a scalable investment rather than a one-time fix.

In short, real-time edge detection transforms a camera from a passive recording device into an active decision-support tool, which is precisely the kind of low-cost, high-adaptability technology that modern robotic deployments require.
