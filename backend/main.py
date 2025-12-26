from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import io

# Initialize FastAPI app
app = FastAPI()

# --- CORS Middleware ---
# This is crucial for allowing the frontend (running on a different port)
# to communicate with this backend.
origins = [
    "http://localhost",
    "http://localhost:8080", # Add the port your frontend is served on if needed
    "http://127.0.0.1",
    "http://127.0.0.1:5500", # Often used by VS Code Live Server
    "null", # To allow requests from local file system (file://)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Model Loading ---
# Load the pre-trained Vision Transformer model and its feature extractor.
# This happens once when the server starts up.
model_name = 'ilyesdjerfaf/vit-base-patch16-224-in21k-quickdraw'
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

print("Model loaded successfully!")

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Etch-A-Sketch AI Guesser API"}

@app.post("/guess")
async def guess_drawing(file: UploadFile = File(...)):
    """
    Receives an image file, processes it, and returns the model's top guess.
    """
    # 1. Read the image data from the upload
    contents = await file.read()
    
    # 2. Open the image using Pillow
    try:
        image = Image.open(io.BytesIO(contents))
        # Ensure image is in RGB format, as the model expects it
        if image.mode != "RGB":
            image = image.convert("RGB")
    except Exception as e:
        return {"error": f"Failed to open or process image: {str(e)}"}

    # 3. Use the feature extractor to prepare the image for the model
    inputs = feature_extractor(images=image, return_tensors="pt")

    # 4. Make a prediction
    outputs = model(**inputs)
    logits = outputs.logits

    # 5. Get the top prediction
    predicted_class_idx = logits.argmax(-1).item()
    prediction = model.config.id2label[predicted_class_idx]

    # 6. Return the result
    return {"guess": prediction}
