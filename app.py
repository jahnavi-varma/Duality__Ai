import gradio as gr
from ultralytics import YOLO
import os

# load model (make sure best.pt or yolov8m.pt is in same folder)
model = YOLO("best.pt")

def predict(image):
    results = model(image)
    return results[0].plot()  # returns annotated image

app = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="numpy", label="Upload an Image"),
    outputs=gr.Image(type="numpy", label="Detection Result"),
    title="Object Detection App",
    description="Upload an image and detect objects using YOLOv8"
)

if __name__ == "__main__":
    # Render sets PORT env variable, fallback to 7860
    port = int(os.environ.get("PORT", 7860))
    app.launch(server_name="127.0.0.1", server_port=port)

