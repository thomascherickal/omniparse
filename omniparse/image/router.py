from fastapi import FastAPI, UploadFile, File, HTTPException , APIRouter,  status , Form
from fastapi.responses import JSONResponse
from omniparse import get_shared_state
from omniparse.image import parse_image, process_image

image_router = APIRouter()
model_state = get_shared_state()

@image_router.post("/image")
async def parse_image_endpoint(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        result = parse_image(file_bytes, model_state)
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@image_router.post("/process_image")
async def process_image_route(image: UploadFile = File(...), task: str = Form(...)):
    try:
        file_bytes = await image.read()
        result = process_image(file_bytes, task, model_state)
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))