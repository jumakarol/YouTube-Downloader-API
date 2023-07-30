
from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware

from pytube import YouTube


app = FastAPI()
origins = [
    
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://wisedownloaderpro.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/download", tags=["Download Video"])
def get_url(link: str):
	yt = YouTube(link)
	title = yt.title
	views = yt.views
	url = yt.streams.get_lowest_resolution().url
	
	return {"Title": title, "views": views, "url": url}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0")



