from pathlib import Path
from random import sample

import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image
from sklearn.cluster import KMeans
from starlette.responses import HTMLResponse


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATE_DIR = BASE_DIR / "templates"
UPLOAD_DIR = STATIC_DIR / "uploads"
RESULT_DIR = STATIC_DIR / "results"

app = FastAPI(title="RestArt FastAPI Web Prototype")

templates = Jinja2Templates(directory=str(TEMPLATE_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


def ensure_directory_exists(path: Path) -> None:
    """Create a directory if it does not already exist."""
    path.mkdir(parents=True, exist_ok=True)


def save_clustered_image(file_path: Path, output_path: Path, num_clusters: int = 5) -> None:
    """
    Save a clustered-color version of the uploaded image.

    This function converts the image to RGB, applies K-means clustering,
    and saves the clustered image result.
    """
    try:
        image = Image.open(file_path).convert("RGB")
        data = np.array(image)

        reshaped_data = data.reshape((-1, 3))

        kmeans = KMeans(n_clusters=num_clusters, n_init=10)
        kmeans.fit(reshaped_data)

        clustered_data = kmeans.cluster_centers_[kmeans.labels_]
        clustered_image = clustered_data.reshape(data.shape).astype(np.uint8)

        clustered_result = Image.fromarray(clustered_image)
        clustered_result.save(output_path)

    except Exception as exc:
        raise RuntimeError(f"Error during image processing: {exc}") from exc


@app.post("/upload/")
async def handle_upload(file: UploadFile = File(...)):
    """
    Receive an uploaded image file and return a clustered image result path.
    """
    ensure_directory_exists(UPLOAD_DIR)
    ensure_directory_exists(RESULT_DIR)

    safe_filename = Path(file.filename).name

    file_location = UPLOAD_DIR / safe_filename
    output_path = RESULT_DIR / f"clustered_{safe_filename}"

    try:
        with open(file_location, "wb") as file_object:
            file_object.write(await file.read())

    except Exception as exc:
        return {"error": f"Failed to save file: {exc}"}

    try:
        save_clustered_image(file_location, output_path)

    except Exception as exc:
        return {"error": f"Failed to process image: {exc}"}

    return {
        "info": "Uploaded and processed",
        "result_image": f"/static/results/clustered_{safe_filename}",
    }


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    """Render the main page."""
    return templates.TemplateResponse(
        "main_page.html",
        {"request": request},
    )


@app.get("/ai_recomm", response_class=HTMLResponse)
async def ai_recomm(request: Request):
    """
    Render the AI recommendation page with sample emotion keywords.

    The original prototype used a random sample of emotion labels.
    Broken encoded strings were replaced with readable Korean emotion labels.
    """
    emotions = [
        "평온",
        "기쁨",
        "사랑",
        "우울",
        "감각적",
        "활기",
        "경외",
        "신비",
        "미소",
        "걱정",
        "외로움",
        "공포",
        "여유",
        "열정",
        "동정",
    ]

    selected_emotions = sample(emotions, 3)

    return templates.TemplateResponse(
        "ai_recomm.html",
        {
            "request": request,
            "fin": selected_emotions,
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )