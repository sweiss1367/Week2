# Video Presentation Script
## Real-Time Edge Detection and Morphological Filtering
### Target Duration: 4–5 Minutes

---

## [SLIDE 1 — Title and Project Objective]

Hello, my name is [Your Name], and this is my Week 2 computer vision mini-project.

In this project, I implemented a real-time edge detection and morphological filtering
system using Python and OpenCV. The script opens a live webcam feed, detects the
boundaries of objects in each frame, refines those boundaries using filtering operations,
and displays all four stages of the process simultaneously — in real time.

The goal was not just to write code that works, but to understand how this kind of
technology functions as a practical tool inside a robotic system. And that's where I
want to start — with the business problem this solves.

---

## [SLIDE 2 — Business and Robotics Scenario]

Imagine a robotic arm on a warehouse picking line. Its job is to identify packages,
calculate where to grip them, and move them accurately — all day, at scale.

The traditional approach is to pre-program the robot with the exact dimensions and
appearance of every object it might encounter. That works in controlled environments,
but it breaks down the moment something unexpected appears — a new product, different
packaging, or an object placed at an unusual angle.

Real-time edge detection changes that. Instead of relying on a static object library,
the robot uses a camera and a vision pipeline to detect boundaries dynamically, on
every single frame. It doesn't need to be told what an object looks like in advance —
it figures out the shape from the live image.

That flexibility directly reduces programming costs, speeds up changeovers when
product lines change, and makes the system more resilient in unpredictable environments.
That's the business case. Now let me walk you through how the pipeline actually works.

---

## [SLIDE 3 — Real-Time Processing Workflow]

The pipeline has six steps, and each one is a single function call in OpenCV.

First, the script captures a live frame from the webcam. Second, it converts that
colour frame to grayscale — we only need brightness information to detect edges, not
colour. Third, it runs Canny edge detection to identify boundaries. Fourth and fifth,
it applies dilation and erosion to clean and refine the edge map. And sixth, it
displays all four outputs live on screen.

The entire sequence runs fast enough to keep up with a standard webcam at full frame
rate, on a laptop CPU, with no specialist hardware. That's an important point —
practical deployment doesn't require expensive infrastructure.

---

## [SLIDE 4 — Canny Edge Detection]

Canny edge detection works by analysing how sharply brightness changes between
neighbouring pixels. Where that change is strong — at the edge of a hand, the corner
of a box, the outline of an object — those pixels get marked as boundaries. Where the
image is smooth or uniform, nothing is marked.

The result is a clean black-and-white image: a dark background with white lines
tracing every detected boundary in the scene. Colour, texture, and depth are all gone.
What remains is pure structure — which is exactly what a robot needs to determine
where one object ends and another begins.

I set the detection thresholds at 100 and 200, which are well-suited to a general
scene with natural lighting. Lower thresholds would capture more edges, including noise;
higher thresholds would focus only on the most prominent boundaries.

---

## [SLIDE 5 — Morphological Operations: Dilation and Erosion]

The raw Canny output is accurate, but not always complete. Two problems come up in
practice. First, low-contrast areas can create small gaps in an otherwise continuous
boundary. Second, noise in the image can produce stray edge pixels that don't
correspond to any real object.

Dilation addresses the first problem. It expands each edge pixel outward using a
5-by-5 kernel, which closes those gaps and produces a more connected, complete contour.
For a robot calculating a grip point, a broken outline is a real operational risk —
dilation removes that risk.

Erosion addresses the second problem. It shrinks each edge pixel inward, stripping
away thin noise filaments while preserving the genuine boundaries. This reduces false
positives — edges the robot might otherwise act on that don't represent real surfaces.

Together, dilation and erosion move the edge map from accurate to reliable. And in
a live robotic system, reliability is what determines whether the robot performs
correctly under real-world conditions.

---

## [SLIDE 6 — Results and Observations]

When I ran the script, all four windows updated in real time with no visible lag.
The original frame showed the live colour feed. The Canny window showed clean white
boundary lines against a black background, accurately tracing the shapes of every
object in frame. The dilated output showed visibly thicker, more connected contours,
and the eroded output showed finer, cleaner lines with noise removed.

What struck me most was how much information gets stripped away at the Canny stage —
and how useful that stripped-down image actually is. A robot doesn't need to see what
I see. It needs a structured, actionable representation of the scene, and that's
exactly what this pipeline produces.

From a business perspective, the result I found most significant is that the entire
system ran on a standard laptop with no GPU. That means the cost barrier to deploying
this kind of adaptive robotic vision is genuinely low — accessible to small and
mid-size operations, not just large enterprises with specialist infrastructure.

---

## [SLIDE 7 — References]

The technical foundation for this project comes from a small set of well-established
sources. John Canny's 1986 paper introduced the edge detection algorithm that remains
the industry standard today — a strong indicator of how robust the underlying method
is. González and Woods provided the framework for understanding morphological
operations, and Bradski and Kaehler served as the practical reference for OpenCV
implementation. Full citations are included in the project's reference file.

To close — this project gave me a working understanding of how computer vision
translates raw camera input into structured, decision-ready data. The pipeline is
modular, runs on accessible hardware, and can be extended to support object
classification, depth estimation, or integration with a robotic controller as a
natural next step.

Thank you for watching. I'm happy to take any questions.

---

*[End of script — estimated delivery time: 4 minutes 30 seconds at a natural speaking pace]*
