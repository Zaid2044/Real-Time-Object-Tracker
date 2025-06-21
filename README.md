# 🤖 Real-Time Object Tracker with YOLOv8

An advanced computer vision system that uses the state-of-the-art YOLOv8 model to detect and track objects in a live webcam feed. The application assigns a persistent ID to each object, allowing for stable tracking across frames.


---

## ✨ Key Features

-   **State-of-the-Art Detection:** Powered by `ultralytics` YOLOv8, a highly accurate and efficient object detection model.
-   **Real-Time Tracking:** Assigns a unique and persistent ID to each detected object, allowing it to be tracked as it moves across the screen.
-   **Smart Logging:** The console only prints a message the **first time** a new object ID is detected, preventing a flood of repetitive logs.
-   **Automated Model Management:** The required YOLOv8 model is automatically downloaded on the first run.
-   **Simple & Efficient:** The code is clean, concise, and optimized for real-time performance on a standard webcam.

---

## 🛠️ Technology Stack

-   **Python**
-   **Ultralytics YOLOv8:** The core library for object detection and tracking.
-   **OpenCV-Python:** Used for capturing and displaying the video feed.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.9+
-   Git
-   A webcam connected to your computer

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Zaid2044/Real-Time-Object-Tracker.git
    cd Real-Time-Object-Tracker
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *(Note: On Windows, the activation command is `source venv/Scripts/activate`)*

3.  **Install the required dependencies:**
    ```bash
    pip install ultralytics opencv-python
    ```

---

## ⚡ Usage

To run the main application, simply execute the `tracker.py` script:

```bash
python3 tracker.py