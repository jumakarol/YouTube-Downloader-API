
from fastapi import FastAPI
from typing import Union

from pytube import YouTube


app = FastAPI()


@app.get("/download", tags=["Download Video"])
def get_url(link: str):
	yt = YouTube(link)
	title = yt.title
	views = yt.views
	url = yt.streams.get_lowest_resolution().url
	
	return {"Title": title, "views": views, "url": url}


