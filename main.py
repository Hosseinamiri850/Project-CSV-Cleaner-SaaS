from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ai_cleaning import ai_suggest
import pandas as pd
import io, math

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def clean_value(v):
    if isinstance(v, float) and math.isnan(v):
        return None
    return v

def clean_dict(d):
    return {k: clean_value(v) for k, v in d.items()}

app.mount("/static", StaticFiles(directory="frontend/src"), name="static")

@app.get("/")
async def root():
    return FileResponse("frontend/src/index.html")

@app.post("/clean")
async def clean_csv(file: UploadFile):
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))

    report = {
        "rows_before": len(df),
        "duplicates": int(df.duplicated().sum()),
        "nulls": {k: int(v) for k, v in df.isnull().sum().items()},
    }

    df = df.drop_duplicates()
    df = df.dropna(thresh=len(df.columns) * 0.5)
    df.columns = [c.strip().lower() for c in df.columns]
    report["rows_after"] = len(df)

    sample = df.head(3).to_csv(index=False)
    ai_notes = await ai_suggest(sample)

    output = io.StringIO()
    df.to_csv(output, index=False)

    preview_raw = df.head(5).to_dict()
    preview = {
        col: clean_dict(rows)
        for col, rows in preview_raw.items()
    }

    return {
        "report": report,
        "ai_notes": ai_notes,
        "preview": preview,
        "csv": output.getvalue()
    }