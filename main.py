from fastapi import FastAPI
from Recording import Recording
import s3service
from pydub import AudioSegment
import sys

sys.path.append('/path/to/ffmpeg-6.0')

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/api/classification")
async def classify_octave_and_recommendation_songs(recording: Recording):
    print("processiong")
    member_nickname = recording.member_nickname
    file_name = recording.file_name
    str = s3service.downloads_recording(member_nickname, file_name)

    audio = AudioSegment.from_file('recordings/'+str)
    audio.export(member_nickname+'.wav', format='wav')







    

