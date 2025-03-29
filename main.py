import yt_dlp
from fastapi.responses import (Response, FileResponse)
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/youtube-downloader/{format}/{resolution}/{yt_id}")
def download_test(format: str, resolution: str, yt_id: str):
    ydl_opts = {
        "outtmpl": f"./conversions/%(title)s.%(ext)s",
        "format": f"bv[height<={resolution}][ext={format}]+ba[ext=m4a]/b[height<={resolution}][ext={format}]"
    }

    yt_link = f"https://www.youtube.com/watch?v={yt_id}"

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(yt_link, download=True)
            file_path = ydl.prepare_filename(info_dict)

        return FileResponse(
            file_path,
            status_code=200,
            media_type="application/octet-stream",
            filename=info_dict.get("title")+".mp4",
            content_disposition_type="attachment",
        )
    except Exception as e:
        return {f"Error: {e}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}