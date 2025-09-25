# Duality AI Hackathon - Object Detection (7 Classes)

## Overview
This project was developed for the **HackWithHyderabad 2025 Hackathon (Duality AI Track)**.  
We trained a **YOLOv8 model** on the provided 7-class dataset and achieved:

- **mAP50:** 86.2%  
- **mAP50-95:** 74.9%  

The goal was to build a multiclass object detection system using synthetic-to-real datasets.

---

## Dataset
- Dataset provided by **Duality AI** (Hackathon challenge).  
- Contains **7 object classes** across training (`train2`) and validation (`val2`) sets.  
- Includes both images and YOLO-format labels.  
- `labels.png` (attached in repo) shows the class layout.  

---

## Model Training
- Framework: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)  
- Training setup:
  - Epochs: 60  
  - Image size: 640x640  
  - Batch size: 16  
- Validation results:
  - **mAP50 = 86.2%**  
  - **mAP50-95 = 74.9%**

Artifacts saved:
- `args.yml` → Training configuration  
- `labels.png` → Dataset classes visualization  
- `train_batch0.jpg` / `test_batch0.png` → Sample labeled images from dataset  

---

## Results
- Training & validation console logs (with mAP scores) are saved as screenshots in `results/`.  
- Example outputs:  

![Dataset Classes](results/labels.png)  
*Figure: 7-class dataset visualization*  

![Training Sample](results/train_batch0.jpg)  
*Figure: Example training batch with labels*  

---

## Bonus Application
As a **bonus challenge**, we built a **local application** to run inference with our trained model (`best.pt`).  

- Runs on **localhost** (`127.0.0.1:7860`)  
- Functionality:  
  - Upload any image → YOLO model detects objects  
  - Displays predictions with bounding boxes  

⚡ Note: The app is **self-contained** and does not rely on other open-source hosting platforms. It uses **our own trained model**.

---

## Files
- `notebook.ipynb` → Training and evaluation in Colab  
- `app.py` → Local app for object detection  
- `requirements.txt` → Dependencies for running the app  
- `results/` → Screenshots, training artifacts, evaluation results (`labels.png`, `args.yml`, `test_batch0.png`, console screenshots)

---

## Team
**Team Name:** [The Firewalls]  
**Members:** [Jahnavi kandula, Prasanna Guntoju, Amulya Eragani, Srivalli Kiranmaii Paka]