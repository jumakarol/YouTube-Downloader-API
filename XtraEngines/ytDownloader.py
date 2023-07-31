from pytube import YouTube

# link = https://www.youtube.com/watch?v=PeMlggyqz0Y




def VideoEngine(link):
	vE = YouTube(link)
	title = vE.title
	author = vE.author
	keywords = vE.keywords
	views = vE.views
	duration = vE.length	
	thumbnail = vE.thumbnail_url
	publish_date = vE.publish_date
	rating = vE.rating
	description = vE.description
	video_info = vE.vid_info
	thumbnail_list = video_info["videoDetails"] ["thumbnail"]
	caption_tracks = vE.captions.all()
	
	video_streams = vE.streams.filter(progressive=True)
	
	
	# Initialize a dictionary to store video qualities and download URLs
	video_qualities = []
        
        # Iterate through the video streams and store the information
	for stream in video_streams:
            # Check if the stream is a video stream (excludes audio-only streams)
		if "video" in str(stream):
			quality_info = {"resolution": stream.resolution, "url": stream.url, "mime_type": stream.mime_type}
			
			video_qualities.append(quality_info) 
			#video_qualities[stream.resolution] = stream.url
                
	return {"data" :{"title": title,"author":author, "views": views, "duration": duration, "featured_thumbnail": thumbnail,"publish_date":publish_date,"rating": rating, "description": description, "keywords": keywords,"thumbnails":thumbnail_list, "qualities": video_qualities   }}
	
	
def ThumbnailEngine(link):
	vE = YouTube(link)
	video_info = vE.vid_info
	thumbnail_list = video_info["videoDetails"] ["thumbnail"]
	return {"details": thumbnail_list}

def CaptionEngine(link):
	vE = YouTube(link)
	caption_tracks = vE.captions.all()
	
	caption_info = []
	for track in caption_tracks:
		captions_info.append({
                "language_code": track.code,
                "language": track.name,
                "caption": track.generate_srt_captions()
            })
	
	return {"details": caption_info }

	
	
	
	
	
	
