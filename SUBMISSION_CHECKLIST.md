# Final Submission Checklist
## Real-Time Edge Detection and Morphological Filtering

Complete every item below before submitting. Work through each section in order.

---

## 1. Code Checklist

- [ ] `edge_detection.py` is saved and complete
- [ ] Script imports `cv2` and `numpy`
- [ ] Webcam opens with `cv2.VideoCapture(0)`
- [ ] `cap.isOpened()` check is present with an error message
- [ ] Kernel is defined as `np.ones((5, 5), np.uint8)`
- [ ] Each frame is converted to grayscale with `cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)`
- [ ] Canny is applied as `cv2.Canny(gray_frame, 100, 200)`
- [ ] Dilation is applied as `cv2.dilate(edges, kernel, iterations=1)`
- [ ] Erosion is applied as `cv2.erode(edges, kernel, iterations=1)`
- [ ] All four windows display: `"Original Frame"`, `"Edges"`, `"Dilated Edges"`, `"Eroded Edges"`
- [ ] `q` key exits the loop cleanly
- [ ] `cap.release()` is called after the loop
- [ ] `cv2.destroyAllWindows()` is called after the loop
- [ ] Script runs without errors from a clean terminal: `python edge_detection.py`

---

## 2. GitHub Checklist

- [ ] Repository is created and named clearly
- [ ] Repository visibility is set to **Public** (or shared directly with your grader)
- [ ] The following files are committed and pushed:
  - [ ] `edge_detection.py`
  - [ ] `requirements.txt`
  - [ ] `README.md`
  - [ ] `outputs/` folder with all screenshots
  - [ ] `references.md`
- [ ] Repository has a one-sentence description in the **About** field
- [ ] Topics/tags are added (e.g. `opencv`, `python`, `edge-detection`, `computer-vision`)
- [ ] GitHub repository URL is copied and ready to paste into your slide 7 and submission form

---

## 3. Screenshot Checklist

- [ ] Script is running with a **real webcam** and a real object in frame
- [ ] `screenshot_01_original_frame.png` — live colour feed captured
- [ ] `screenshot_02_edges.png` — Canny edge window captured
- [ ] `screenshot_03_dilated_edges.png` — Dilated Edges window captured
- [ ] `screenshot_04_eroded_edges.png` — Eroded Edges window captured
- [ ] `screenshot_05_terminal_running.png` — terminal showing `python edge_detection.py` running
- [ ] `screenshot_06_all_windows.png` — all four windows visible on screen at the same time
- [ ] All screenshots are saved to the `outputs/` folder
- [ ] All screenshots are committed and pushed to GitHub

---

## 4. PowerPoint Checklist

- [ ] Slide 1 — Title, your name, course name, and date are filled in
- [ ] Slide 2 — Business/robotics scenario is present
- [ ] Slide 3 — Six-step workflow diagram or bullet list is included
- [ ] Slide 4 — Canny edge detection is explained with a before/after image
- [ ] Slide 5 — Dilation and erosion are explained with a three-panel image
- [ ] Slide 6 — Results screenshot (`screenshot_06_all_windows.png`) is placed on the slide
- [ ] Slide 7 — GitHub repository URL placeholder is replaced with your actual link
- [ ] Slide 7 — APA reference list is visible and complete
- [ ] All slides use consistent fonts, colours, and spacing
- [ ] File is saved as `.pptx` (not `.ppt` or `.key`)
- [ ] File is named clearly, e.g. `EdgeDetection_Presentation.pptx`

---

## 5. Speaker Notes Checklist

- [ ] Every slide has speaker notes — no slide is left blank
- [ ] Slide 1 notes introduce you and state the project objective
- [ ] Slide 2 notes explain the warehouse robotics scenario and business case
- [ ] Slide 3 notes walk through the six pipeline steps
- [ ] Slide 4 notes explain how Canny works and why the thresholds were chosen
- [ ] Slide 5 notes explain what dilation and erosion each fix
- [ ] Slide 6 notes describe what you observed and state the business value
- [ ] Slide 7 notes name your sources and close with a thank-you
- [ ] Notes are written in full sentences (not just bullet fragments)
- [ ] Notes match what you actually say in your video recording

---

## 6. Video Recording Checklist

**Before you record:**
- [ ] `[Your Name]` is replaced with your actual name in `video_script.md`
- [ ] Script has been read aloud at least once — mark any sentences that feel awkward and simplify them
- [ ] Microphone is tested — audio is clear with no background noise
- [ ] Screen recording software is open and tested (OBS, Loom, Zoom, or QuickTime)
- [ ] PowerPoint is in full-screen presentation mode
- [ ] All four output screenshots are ready to reference on screen

**During recording:**
- [ ] Introduction names you and states the project clearly
- [ ] Each slide is introduced before you read from the notes
- [ ] All four pipeline stages are mentioned by name: Grayscale, Canny, Dilation, Erosion
- [ ] Business value is explained — not just the technical steps
- [ ] Closing statement is delivered clearly and confidently
- [ ] Invitation for questions is included at the end

**After recording:**
- [ ] Playback the full recording before saving — check audio sync and no missing slides
- [ ] Recording runs between **4 and 7 minutes**
- [ ] Video is exported in a standard format: `.mp4` preferred
- [ ] File is named clearly, e.g. `EdgeDetection_Video_Presentation.mp4`

---

## 7. APA Reference Checklist

- [ ] All six sources are listed in `references.md`
- [ ] Every source cited by name in the video script appears in the reference list
- [ ] Every source cited by name in the speaker notes appears in the reference list
- [ ] References are listed in **alphabetical order** by author surname or organisation name
- [ ] All three OpenCV entries use `n.d.-a`, `n.d.-b`, `n.d.-c` to distinguish them
- [ ] The YouTube video entry includes `[Video]` after the title
- [ ] All six URLs have been **opened in a browser** and confirmed as live
- [ ] In-text citations are used in the speaker notes or written report where relevant
- [ ] `references.md` is committed and pushed to GitHub

---

## Final Pre-Submission Check

Run through this last before you hit submit.

- [ ] GitHub repository is public and the link works when opened in a private browser tab
- [ ] `python edge_detection.py` still runs cleanly from a fresh terminal
- [ ] PowerPoint file opens without errors and all images load correctly
- [ ] Video plays from start to finish with clear audio and no missing slides
- [ ] Your name appears on: the title slide, the video introduction, and the submission form
- [ ] All file names are clean and professional — no `final_FINAL_v3` naming
- [ ] Submission form is filled in completely before clicking submit

---

*Complete every checkbox. If any item cannot be checked, fix it before submitting.*
