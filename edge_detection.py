"""
Real-Time Edge Detection and Morphological Filtering
Robotics Vision System — Week 2 Assignment
"""

import cv2
import numpy as np
import os
import sys
from datetime import datetime

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Tunable parameters ──────────────────────────────────────────────────────
CANNY_LOW   = 50
CANNY_HIGH  = 150
BLUR_KERNEL = (5, 5)
MORPH_KERNEL_SIZE = 3
# ────────────────────────────────────────────────────────────────────────────


def build_morph_kernel(size: int = MORPH_KERNEL_SIZE) -> np.ndarray:
    return cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))


def process_frame(frame: np.ndarray, kernel: np.ndarray) -> dict:
    """Return a dict of processed images for a single BGR frame."""
    gray      = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred   = cv2.GaussianBlur(gray, BLUR_KERNEL, 0)
    edges     = cv2.Canny(blurred, CANNY_LOW, CANNY_HIGH)
    dilated   = cv2.dilate(edges, kernel, iterations=1)
    eroded    = cv2.erode(edges, kernel, iterations=1)
    closed    = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    overlay   = frame.copy()
    overlay[edges > 0] = [0, 255, 0]   # green edge overlay on colour frame

    return {
        "original":  frame,
        "grayscale": cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR),
        "edges":     cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR),
        "dilated":   cv2.cvtColor(dilated, cv2.COLOR_GRAY2BGR),
        "eroded":    cv2.cvtColor(eroded, cv2.COLOR_GRAY2BGR),
        "closed":    cv2.cvtColor(closed, cv2.COLOR_GRAY2BGR),
        "overlay":   overlay,
    }


def build_display_grid(views: dict) -> np.ndarray:
    """Arrange six panels in a 2×3 grid with labels."""
    panels = ["original", "grayscale", "edges", "dilated", "eroded", "overlay"]
    labels = ["Original", "Grayscale", "Canny Edges", "Dilated", "Eroded", "Edge Overlay"]
    cells  = []

    for key, label in zip(panels, labels):
        img = views[key].copy()
        cv2.putText(img, label, (8, 22),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 255), 2, cv2.LINE_AA)
        cells.append(img)

    row1 = np.hstack(cells[:3])
    row2 = np.hstack(cells[3:])
    return np.vstack([row1, row2])


def save_screenshot(grid: np.ndarray, tag: str = "") -> str:
    ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
    name = f"screenshot_{tag}_{ts}.png" if tag else f"screenshot_{ts}.png"
    path = os.path.join(OUTPUT_DIR, name)
    cv2.imwrite(path, grid)
    return path


def run_demo_mode() -> None:
    """
    Headless demo: generate output images from a synthetic test pattern
    so the project can be evaluated without a physical webcam.
    """
    print("[INFO] No webcam detected — running in demo mode.")
    h, w = 480, 640
    frame = np.zeros((h, w, 3), dtype=np.uint8)

    # Draw geometric shapes to produce clear, demonstrable edges
    cv2.rectangle(frame, (80, 80), (280, 280), (180, 60, 60), -1)
    cv2.circle(frame, (480, 180), 120, (60, 180, 60), -1)
    cv2.ellipse(frame, (320, 380), (160, 80), 30, 0, 360, (60, 60, 180), -1)
    cv2.line(frame, (0, 0), (w, h), (200, 200, 0), 3)
    cv2.line(frame, (w, 0), (0, h), (0, 200, 200), 3)
    # Add Gaussian noise for realism
    noise = np.random.normal(0, 12, frame.shape).astype(np.int16)
    frame = np.clip(frame.astype(np.int16) + noise, 0, 255).astype(np.uint8)

    kernel = build_morph_kernel()
    views  = process_frame(frame, kernel)
    grid   = build_display_grid(views)

    path = save_screenshot(grid, tag="demo")
    print(f"[INFO] Demo screenshot saved → {path}")

    # Save individual panels for the presentation
    for key in ("original", "edges", "dilated", "eroded", "overlay"):
        out_path = os.path.join(OUTPUT_DIR, f"panel_{key}.png")
        cv2.imwrite(out_path, views[key])
        print(f"[INFO] Panel saved → {out_path}")


def run_webcam_mode() -> None:
    """Live webcam loop. Press 's' to save a screenshot, 'q' to quit."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[WARN] Could not open webcam — switching to demo mode.")
        run_demo_mode()
        return

    kernel = build_morph_kernel()
    print("[INFO] Webcam active. Press 's' to save screenshot, 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Frame capture failed.")
            break

        views = process_frame(frame, kernel)
        grid  = build_display_grid(views)

        cv2.imshow("Edge Detection — Robotics Vision System", grid)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        elif key == ord("s"):
            path = save_screenshot(grid)
            print(f"[INFO] Screenshot saved → {path}")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    demo_flag = "--demo" in sys.argv
    if demo_flag:
        run_demo_mode()
    else:
        run_webcam_mode()
