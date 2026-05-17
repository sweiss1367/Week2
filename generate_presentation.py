"""
Generates the 6-slide PowerPoint presentation for the edge detection project.
Run after edge_detection.py --demo so panel images exist in outputs/.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os

OUTPUT_DIR = "outputs"
PPTX_PATH  = os.path.join(OUTPUT_DIR, "EdgeDetection_Presentation.pptx")

# Brand colours
DARK_BLUE  = RGBColor(0x1F, 0x39, 0x64)   # #1F3964
ACCENT     = RGBColor(0x2E, 0x75, 0xB6)   # #2E75B6
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xF2, 0xF2, 0xF2)

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)


def _new_prs() -> Presentation:
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs


def _blank_layout(prs: Presentation):
    return prs.slide_layouts[6]   # completely blank


def _fill_bg(slide, color: RGBColor):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _add_text_box(slide, text, left, top, width, height,
                  font_size=24, bold=False, color=WHITE,
                  align=PP_ALIGN.LEFT, wrap=True):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf    = txBox.text_frame
    tf.word_wrap = wrap
    p  = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size  = Pt(font_size)
    run.font.bold  = bold
    run.font.color.rgb = color
    return txBox


def _add_image_safe(slide, path, left, top, width, height):
    if os.path.exists(path):
        slide.shapes.add_picture(path, left, top, width=width, height=height)
    else:
        # Placeholder box when image not yet generated
        box = slide.shapes.add_textbox(left, top, width, height)
        tf  = box.text_frame
        tf.paragraphs[0].add_run().text = f"[Image: {os.path.basename(path)}]"


# ── Slide builders ───────────────────────────────────────────────────────────

def slide_01_title(prs):
    slide = prs.slides.add_slide(_blank_layout(prs))
    _fill_bg(slide, DARK_BLUE)

    # Accent bar
    bar = slide.shapes.add_shape(1, Inches(0), Inches(5.6), SLIDE_W, Inches(0.08))
    bar.fill.solid(); bar.fill.fore_color.rgb = ACCENT
    bar.line.fill.background()

    _add_text_box(slide, "REAL-TIME EDGE DETECTION",
                  Inches(0.8), Inches(1.2), Inches(11.7), Inches(1.1),
                  font_size=40, bold=True, align=PP_ALIGN.CENTER)
    _add_text_box(slide, "& Morphological Filtering for Robotic Vision",
                  Inches(0.8), Inches(2.35), Inches(11.7), Inches(0.8),
                  font_size=26, align=PP_ALIGN.CENTER,
                  color=RGBColor(0xBD, 0xD7, 0xEE))
    _add_text_box(slide,
                  "Week 2 Mini-Project  |  Computer Vision  |  MBA Program",
                  Inches(0.8), Inches(5.9), Inches(11.7), Inches(0.6),
                  font_size=18, align=PP_ALIGN.CENTER,
                  color=RGBColor(0xBD, 0xD7, 0xEE))

    notes = (
        "Good [morning/afternoon]. Today I'm presenting my Week 2 mini-project on "
        "real-time edge detection and morphological filtering applied to a robotic "
        "vision system. The goal of this project was to build a working computer vision "
        "pipeline in Python that can identify the boundaries of objects in a live video "
        "feed — a core capability for any autonomous robot that needs to understand its "
        "physical environment."
    )
    slide.notes_slide.notes_text_frame.text = notes


def slide_02_problem(prs):
    slide = prs.slides.add_slide(_blank_layout(prs))
    _fill_bg(slide, LIGHT_GRAY)

    _add_text_box(slide, "The Business Problem", Inches(0.5), Inches(0.3),
                  Inches(12), Inches(0.7), font_size=30, bold=True,
                  color=DARK_BLUE, align=PP_ALIGN.LEFT)

    points = [
        "Robots must detect object boundaries in real time to navigate, pick, and place items safely.",
        "Manual programming of every object shape is impractical — robots need adaptive vision.",
        "Edge detection converts raw camera pixels into structured boundary data.",
        "Morphological filters clean the signal, reducing noise that could cause incorrect decisions.",
        "Together, these techniques form the perception layer of an industrial robotic system.",
    ]
    body = "\n".join(f"• {p}" for p in points)
    _add_text_box(slide, body, Inches(0.7), Inches(1.2), Inches(11.8), Inches(5.5),
                  font_size=20, color=DARK_BLUE, wrap=True)

    notes = (
        "The core business problem is robot perception. A robot on a warehouse floor or "
        "manufacturing line cannot operate safely if it cannot 'see' where objects begin "
        "and end. Edge detection is the first step in translating a raw camera image into "
        "actionable information. Morphological filtering is then applied to remove noise "
        "from the edge map, producing a cleaner signal for downstream decision-making. "
        "Without this pipeline, the robot would either miss objects or misidentify their "
        "boundaries — both costly outcomes in an operational setting."
    )
    slide.notes_slide.notes_text_frame.text = notes


def slide_03_methodology(prs):
    slide = prs.slides.add_slide(_blank_layout(prs))
    _fill_bg(slide, WHITE)

    _add_text_box(slide, "Technical Methodology", Inches(0.5), Inches(0.3),
                  Inches(12), Inches(0.7), font_size=30, bold=True,
                  color=DARK_BLUE)

    steps = [
        ("1. Capture", "Live frame from webcam via OpenCV VideoCapture."),
        ("2. Grayscale", "Convert BGR colour frame to single-channel grayscale."),
        ("3. Gaussian Blur", "Smooth the image (5×5 kernel) to suppress high-frequency noise."),
        ("4. Canny Detection", "Identify edges using gradient thresholds (low=50, high=150)."),
        ("5. Dilation", "Expand edge pixels outward — closes small gaps in boundaries."),
        ("6. Erosion", "Shrink edge pixels — removes thin noise filaments."),
        ("7. Closing", "Dilation followed by erosion — seals broken contours."),
        ("8. Overlay", "Project green edges onto the original colour frame for review."),
    ]
    y = Inches(1.15)
    for title, desc in steps:
        _add_text_box(slide, f"{title}:  {desc}", Inches(0.8), y, Inches(12), Inches(0.45),
                      font_size=17, color=DARK_BLUE)
        y += Inches(0.46)

    notes = (
        "Let me walk through the eight-step pipeline. We start by capturing a frame from "
        "the webcam. We convert it to grayscale because colour information is not needed "
        "for edge detection and processing one channel is faster. Gaussian blur smooths "
        "out pixel-level noise before the Canny algorithm runs its gradient calculation. "
        "Canny produces a binary edge map. We then apply three morphological operations — "
        "dilation, erosion, and closing — each offering a different way to clean and "
        "reinforce the edge boundaries. Finally, we overlay the edges in green on the "
        "original colour frame so a human operator can validate the output visually."
    )
    slide.notes_slide.notes_text_frame.text = notes


def slide_04_results(prs):
    slide = prs.slides.add_slide(_blank_layout(prs))
    _fill_bg(slide, LIGHT_GRAY)

    _add_text_box(slide, "Pipeline Output — Visual Results", Inches(0.5), Inches(0.3),
                  Inches(12), Inches(0.7), font_size=30, bold=True, color=DARK_BLUE)

    images = [
        (os.path.join(OUTPUT_DIR, "panel_original.png"), "Original Frame"),
        (os.path.join(OUTPUT_DIR, "panel_edges.png"),    "Canny Edges"),
        (os.path.join(OUTPUT_DIR, "panel_overlay.png"),  "Edge Overlay"),
    ]
    x_positions = [Inches(0.4), Inches(4.6), Inches(8.8)]
    img_w, img_h = Inches(3.9), Inches(2.9)

    for (path, label), x in zip(images, x_positions):
        _add_image_safe(slide, path, x, Inches(1.2), img_w, img_h)
        _add_text_box(slide, label, x, Inches(4.2), img_w, Inches(0.4),
                      font_size=16, color=DARK_BLUE, align=PP_ALIGN.CENTER)

    notes = (
        "Here we can see three key stages of the pipeline side by side. On the left is "
        "the original captured frame showing geometric shapes used as stand-ins for real "
        "objects. In the centre is the raw Canny edge map — a binary image where white "
        "pixels represent detected boundaries. On the right is the final overlay, where "
        "those edges are projected back onto the colour image in green. In a real "
        "deployment, this overlay is what a robot's control system would consume to "
        "determine object positions and boundaries."
    )
    slide.notes_slide.notes_text_frame.text = notes


def slide_05_morphology(prs):
    slide = prs.slides.add_slide(_blank_layout(prs))
    _fill_bg(slide, WHITE)

    _add_text_box(slide, "Morphological Filtering — Comparison",
                  Inches(0.5), Inches(0.3), Inches(12), Inches(0.7),
                  font_size=30, bold=True, color=DARK_BLUE)

    images = [
        (os.path.join(OUTPUT_DIR, "panel_edges.png"),   "Raw Canny Edges"),
        (os.path.join(OUTPUT_DIR, "panel_dilated.png"), "After Dilation"),
        (os.path.join(OUTPUT_DIR, "panel_eroded.png"),  "After Erosion"),
    ]
    x_positions = [Inches(0.4), Inches(4.6), Inches(8.8)]
    img_w, img_h = Inches(3.9), Inches(2.9)

    for (path, label), x in zip(images, x_positions):
        _add_image_safe(slide, path, x, Inches(1.2), img_w, img_h)
        _add_text_box(slide, label, x, Inches(4.2), img_w, Inches(0.4),
                      font_size=16, color=DARK_BLUE, align=PP_ALIGN.CENTER)

    bullets = (
        "Dilation: thickens boundaries — useful when edges are faint or broken.\n"
        "Erosion: thins boundaries — removes noise pixels around true edges.\n"
        "Closing (Dilate → Erode): fills gaps in contours without enlarging overall shape."
    )
    _add_text_box(slide, bullets, Inches(0.8), Inches(4.7), Inches(11.7), Inches(1.8),
                  font_size=17, color=DARK_BLUE)

    notes = (
        "This slide compares the three morphological outputs. The raw Canny edges can "
        "contain small breaks in contours or stray noise pixels. Dilation fills those "
        "breaks by expanding each edge pixel outward — analogous to widening a road to "
        "make it more visible. Erosion takes the opposite approach, stripping away thin "
        "noise filaments while preserving thicker, genuine boundaries. The closing "
        "operation — dilation followed by erosion — is the most commonly used because "
        "it seals gaps without permanently enlarging the edge map."
    )
    slide.notes_slide.notes_text_frame.text = notes


def slide_06_conclusion(prs):
    slide = prs.slides.add_slide(_blank_layout(prs))
    _fill_bg(slide, DARK_BLUE)

    bar = slide.shapes.add_shape(1, Inches(0), Inches(1.9), SLIDE_W, Inches(0.06))
    bar.fill.solid(); bar.fill.fore_color.rgb = ACCENT
    bar.line.fill.background()

    _add_text_box(slide, "Key Takeaways & Business Value",
                  Inches(0.6), Inches(0.3), Inches(12), Inches(0.8),
                  font_size=30, bold=True, color=WHITE, align=PP_ALIGN.LEFT)

    points = [
        "Real-time edge detection is a proven, low-cost perception technique deployable on standard hardware.",
        "Morphological filtering increases reliability — fewer false positives mean fewer robot errors.",
        "The modular pipeline (capture → filter → detect → clean → overlay) is extensible to object "
        "classification, depth estimation, and path planning.",
        "OpenCV's optimised C++ back-end processes HD frames at >30 fps on a laptop CPU — no GPU required.",
        "Next steps: integrate with a physical robotic arm controller (ROS2) and add contour-based object labelling.",
    ]
    body = "\n\n".join(f"• {p}" for p in points)
    _add_text_box(slide, body, Inches(0.8), Inches(2.1), Inches(11.7), Inches(5.0),
                  font_size=19, color=WHITE, wrap=True)

    notes = (
        "To summarise, this project demonstrates a complete, working robotic vision pipeline "
        "built entirely in Python using OpenCV. The system can process live video, detect "
        "object boundaries in real time, and apply morphological filters to produce clean, "
        "reliable edge maps. From a business perspective, this technology directly reduces "
        "the cost of robot programming and increases operational safety by giving machines "
        "reliable spatial awareness. The code is modular, well-documented, and ready to be "
        "extended — for example, by connecting it to a ROS2 robotic controller or adding "
        "a machine-learning classifier on top of the edge maps. Thank you, and I'm happy "
        "to take any questions."
    )
    slide.notes_slide.notes_text_frame.text = notes


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    prs = _new_prs()
    slide_01_title(prs)
    slide_02_problem(prs)
    slide_03_methodology(prs)
    slide_04_results(prs)
    slide_05_morphology(prs)
    slide_06_conclusion(prs)
    prs.save(PPTX_PATH)
    print(f"[INFO] Presentation saved → {PPTX_PATH}")


if __name__ == "__main__":
    main()
