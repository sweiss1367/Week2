# Real-Time Edge Detection and Morphological Filtering
### Robotics Vision System — Week 2 Computer Vision Mini-Project

---

## Project Overview

This project implements a real-time computer vision pipeline that detects object boundaries in a live webcam feed using the Canny edge detection algorithm, followed by morphological filtering operations (dilation, erosion, and closing). The system is designed to simulate the perception layer of an industrial robotic system.

---

## Project Structure

```
Week2/
├── edge_detection.py          # Main Python script (webcam + demo mode)
├── generate_presentation.py   # Generates the PowerPoint presentation
├── requirements.txt           # Python package dependencies
├── video_script.md            # 5–7 minute video presentation script
├── references.md              # APA-style references
├── README.md                  # This file
└── outputs/                   # Generated screenshots and presentation
    ├── panel_original.png
    ├── panel_edges.png
    ├── panel_dilated.png
    ├── panel_eroded.png
    ├── panel_overlay.png
    ├── screenshot_demo_*.png
    └── EdgeDetection_Presentation.pptx
```

---

## Requirements

- Python 3.9 or higher
- A webcam (optional — the script includes a demo mode for headless environments)

---

## Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the edge detection script

**With a webcam (live mode):**
```bash
python edge_detection.py
```

- Press **`s`** to save a screenshot to the `outputs/` folder.
- Press **`q`** to quit.

**Without a webcam (demo mode):**
```bash
python edge_detection.py --demo
```

This generates all output images using a synthetic test scene.

### 3. Generate the PowerPoint presentation

Run the demo mode first to produce the panel images, then:

```bash
python generate_presentation.py
```

The file `outputs/EdgeDetection_Presentation.pptx` will be created.

---

## Pipeline Summary

| Step | Operation | Purpose |
|------|-----------|---------|
| 1 | Frame Capture | Obtain raw BGR frame from webcam |
| 2 | Grayscale Conversion | Reduce to single channel for processing speed |
| 3 | Gaussian Blur | Suppress pixel-level noise before edge detection |
| 4 | Canny Detection | Identify edges via gradient thresholds (50 / 150) |
| 5 | Dilation | Expand edges — closes small gaps in boundaries |
| 6 | Erosion | Shrink edges — removes thin noise filaments |
| 7 | Morphological Closing | Seals broken contours without enlarging edges |
| 8 | Colour Overlay | Project edges (green) onto original colour frame |

---

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CANNY_LOW` | 50 | Lower gradient threshold for edge detection |
| `CANNY_HIGH` | 150 | Upper gradient threshold for edge detection |
| `BLUR_KERNEL` | (5, 5) | Gaussian blur kernel size |
| `MORPH_KERNEL_SIZE` | 3 | Structuring element size for morphological ops |

All parameters are defined as constants at the top of `edge_detection.py` for easy tuning.

---

## Output Files

After running both scripts, the `outputs/` directory contains:

| File | Description |
|------|-------------|
| `panel_original.png` | Raw camera frame |
| `panel_edges.png` | Canny edge detection result |
| `panel_dilated.png` | Edges after dilation |
| `panel_eroded.png` | Edges after erosion |
| `panel_overlay.png` | Edges overlaid on colour frame |
| `screenshot_demo_*.png` | Full 2×3 grid composite screenshot |
| `EdgeDetection_Presentation.pptx` | 6-slide PowerPoint presentation |

---

## References

See `references.md` for full APA-style citations.

Key sources:
- Canny, J. (1986). A computational approach to edge detection. *IEEE TPAMI*, 8(6), 679–698.
- González, R. C., & Woods, R. E. (2018). *Digital image processing* (4th ed.). Pearson.
- Bradski, G., & Kaehler, A. (2008). *Learning OpenCV*. O'Reilly Media.

---

## Presentation Materials

| File | Description |
|------|-------------|
| `outputs/EdgeDetection_Presentation.pptx` | 6-slide PowerPoint with speaker notes |
| `video_script.md` | Full word-for-word script for the 5–7 minute video |
| `references.md` | APA-format reference list |
