# ✋🎨 Hand Gesture Drawing App using OpenCV & MediaPipe

Welcome to the **Hand Gesture Drawing App** — an intuitive, real-time, AI-powered application that enables users to draw on a virtual canvas using nothing but their hands. Built with the precision of **MediaPipe** and the flexibility of **OpenCV**, this project transforms simple finger movements into expressive digital strokes.

---

## 🌟 Features

🚀 **Gesture-Based Controls** (no mouse or touch needed!)  
🖌️ **Smooth Drawing** with one-finger motion  
🎨 **Color Picker Popup** (triggered by 3 fingers)  
🧽 **Clear Canvas** instantly with 4 fingers  
💾 **Save Artwork** with 5 fingers  
🪄 **Dynamic Brush Size** control using `+` and `-` keys  
🎥 **Real-Time Camera Feed** with seamless overlay  
🖐️ **Gesture Recognition** powered by 21 hand landmarks  

---

## 📁 Project Structure

```

hand\_draw/
├── main.py            # 🎯 Main application logic and UI
├── utils.py           # ✋ Hand gesture (finger count) detection
└── color\_popup.py     # 🎨 Tkinter-based color selection popup

````

---

## 🧠 Requirements

Make sure you have the following installed:

```bash
pip install opencv-python mediapipe
````

✅ Optional (already included with Python on most systems): `tkinter` for the color popup.

---

## ⚙️ How to Run

```bash
python main.py
```

Then just use your hand in front of the webcam!

---

## ✋ Gesture Controls

| ✋ Gesture        | 🧠 Action                              |
| ---------------- | -------------------------------------- |
| 1 Finger (Index) | ✍️ Start/Continue Drawing              |
| 2 Fingers        | ⏸️ Pause Drawing                       |
| 3 Fingers        | 🎨 Open Color Picker                   |
| 4 Fingers        | 🧹 Clear Canvas                        |
| 5 Fingers        | 💾 Save Drawing (`drawing_output.png`) |
| `+` / `-` Keys   | 🔧 Increase / Decrease Brush Size      |
| `q` Key          | ❌ Quit Application                     |

---

## 📌 Future Enhancements (Ideas 💡)

* ✏️ Shape drawing (circle, rectangle) via gestures
* 🖼️ Image gallery of saved artworks
* 🧠 Train a custom model for gesture classification
* 🌐 Web-based drawing using Flask + JS
* 🧲 Magnetic brush (auto-smooth lines)

---

## 🧑‍💻 Authors & Acknowledgments

Built with ❤️ by [Tirth Chhatrala](https://github.com/TirthChhatrala/VisionDraw-AI-Powered-Hand-Gesture-Drawing-Interface.git)
Leveraging **MediaPipe**, **OpenCV**, and **Tkinter** magic.

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and build upon it for your creative projects.

---

> 🔔 *Tip: This app is a fantastic base for interactive art, sign language recognition, or virtual whiteboarding tools.*
