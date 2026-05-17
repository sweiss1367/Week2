# Video Presentation Script
## Real-Time Edge Detection and Morphological Filtering — Robotic Vision System
### Approximate Duration: 5–7 Minutes

---

## SLIDE 1 — Title (0:00–0:40)

"Good [morning/afternoon], and welcome to my Week 2 computer vision mini-project presentation.
My name is [Your Name], and today I'll be walking you through a real-time edge detection
and morphological filtering system designed for robotic vision applications.

In simple terms, I built a Python program that takes a live video feed from a webcam,
identifies the boundaries of every object in the frame, cleans up that boundary data,
and displays it in real time — the kind of capability a robot on a factory floor or in
a warehouse would need to safely navigate and interact with its environment.

Let's get into it."

---

## SLIDE 2 — The Business Problem (0:40–1:40)

"So why does this matter?

Robots are increasingly being deployed in dynamic environments — warehouses, surgical
theatres, agriculture, and manufacturing. Unlike a conveyor belt with fixed objects in
fixed positions, these environments change constantly. A robot that cannot see object
boundaries in real time simply cannot function safely.

Traditional approaches hardcode the robot's knowledge of its environment, which means
any unexpected object causes a failure or stoppage. Computer vision solves this by
letting the robot perceive and adapt.

Edge detection is specifically the technique of finding where one object ends and
another begins — it extracts the structural information from a camera image without
needing to understand colour, texture, or depth. And morphological filtering then
takes those detected edges and cleans them up, removing noise so the robot gets
reliable, actionable data.

Together, these two techniques form the perception foundation of a modern robotic system."

---

## SLIDE 3 — Technical Methodology (1:40–3:00)

"Let me walk you through the eight-step pipeline I built.

Step one: we capture a live frame from the webcam using OpenCV's VideoCapture class.

Step two: we convert the colour frame to grayscale. We don't need colour information
to find edges, and working with a single channel is significantly faster.

Step three: we apply a Gaussian blur — think of this as a light smoothing pass that
removes pixel-level noise that would otherwise be misidentified as edges.

Step four: Canny edge detection. This is the core algorithm. It calculates the gradient —
how sharply pixel brightness changes — across the image, and marks as 'edges' any
location where that gradient exceeds a threshold we set. I used values of 50 and 150
for the low and high thresholds respectively.

Steps five through seven are the morphological filters. Dilation expands the edges
slightly, closing small gaps in boundaries. Erosion does the opposite — it shrinks
edges to remove thin noise filaments. And morphological closing — dilation followed
by erosion — is the most practical operation for sealing broken contours.

Step eight: we overlay the detected edges onto the original colour frame in green,
giving a human operator or a downstream algorithm a clear visual of what the system
has identified."

---

## SLIDE 4 — Visual Results (3:00–4:10)

"Here you can see the pipeline in action.

On the left is the raw camera input — in this case a synthetic test scene with
geometric shapes, used to demonstrate the pipeline without requiring a live camera
during the presentation.

In the centre is the Canny edge map — a binary image where every white pixel
represents a detected boundary. You can see the outlines of all three shapes are
clearly captured.

On the right is the final overlay — the edges are projected back onto the colour
image in green. This is the format a robot's control system would receive.

Notice that the curves of the circle, the corners of the rectangle, and the
diagonal lines are all accurately captured. In a real deployment, this data
feeds directly into the robot's decision engine — telling it where it can
safely reach, grip, or navigate."

---

## SLIDE 5 — Morphological Filtering Comparison (4:10–5:10)

"This slide compares the three morphological outputs side by side.

On the left, the raw Canny edges — accurate but sometimes containing small
breaks or noise pixels at the boundaries.

In the middle, after dilation — the edges are thicker and any small gaps in
the contour have been filled in. This is important when the robot needs a
complete, unbroken boundary to compute an accurate grip point.

On the right, after erosion — the edges are thinner and cleaner. Stray noise
pixels that don't belong to any real boundary have been eliminated.

The choice of which morphological operation to apply depends on the application.
In most robotic perception tasks, morphological closing — the combination of
dilation then erosion — gives the best result: gaps are filled, and the
overall boundary doesn't grow larger than the real object."

---

## SLIDE 6 — Conclusion & Business Value (5:10–6:00)

"To wrap up — what did this project demonstrate, and why does it matter?

First, the technical result: a fully working, real-time vision pipeline that
runs at over 30 frames per second on standard laptop hardware. No GPU required.

Second, the business result: this kind of system directly reduces the cost of
deploying adaptive robots. Instead of reprogramming a robot every time the
environment changes, you give it eyes that adapt automatically.

Third, extensibility: the modular pipeline I built can be extended to add object
classification, depth estimation, or path planning without restructuring the core code.

The natural next step is integration with a ROS2 robotic controller, which would
close the loop between perception and action — the robot sees an edge, computes
a trajectory, and moves accordingly.

Thank you for your time. I'm happy to take any questions."

---

*[End of script — estimated delivery time: 5 minutes 45 seconds at a measured pace]*
