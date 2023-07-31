from XtraEngines.ytDownloader import VideoEngine, ThumbnailEngine, CaptionEngine
from XtraEngines.ytSearch import SearchEngine, AutoSuggestEngine
from fastapi import FastAPI, HTTPException
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse




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

@app.get("/", response_class=RedirectResponse, status_code=301)
async def redirect_documentation():
    return "/redoc"
@app.get("/video", tags=["Video Details"])
def get_details(link: str):
	try:
		getVideo = VideoEngine(link)
		return getVideo
	except:
		raise HTTPException(status_code = 404, detail= f"could not process the video with url '{link}'. please confirm the video link and try again")
		
@app.get("/video/thumbnails", tags=["Video Details"])
def get_thumbnails(link: str):
	try:
		getVideo = ThumbnailEngine(link)
		return getVideo
	except:
		raise HTTPException(status_code = 404, detail= f"could not process the video with url '{link}'. please confirm the video link and try again")
@app.get("/video/captions", tags=["Video Details"])
def get_captions(link: str):
	try:
		getVideo = CaptionEngine(link)
		return getVideo
	except:
		raise HTTPException(status_code = 404, detail= f"could not process the video with url '{link}'. please confirm the video link and try again")
		
@app.get("/search", tags=["Search for Videos"])
def search_videos(searchTerm: str):
	try:
		searchVideos = SearchEngine(searchTerm)
		return searchVideos
	except:
		raise HTTPException(status_code = 404, detail= f"could not process the video with url '{searchTerm}'. please confirm the video link and try again")


@app.get("/search/suggest", tags=["Search for Videos"])
def auto_suggest(searchTerm: str):
	try:
		searchVideos = AutoSuggestEngine(searchTerm)
		return searchVideos
	except:
		raise HTTPException(status_code = 404, detail= f"No auto suggestion available")



	
	

#for production

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0 ")



