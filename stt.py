import whisper
import json
import os

model = whisper.load_model("large-v2")

result = model.transcribe(
    r"D:\RAG\audios\1_heading-paragraphs-and-links-sigma-web-development-course-tutorial.mp3",
    language="hi",
    task="translate",
    word_timestamps=False
)
chunks= []
for segment in result["segments"]:
  chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"],"number": segment["number"],"tittle":segment["tittle"]})

print(chunks)

chunks_with_metadata={
    "chunks":chunks,
    "text":result["text"]
}
os.makedir("json",exist_ok=True)
with open("output.json","w") as f:
  json.dump(chunks_with_metadata, f,indent=4)

