# app/main.py
import os
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import PlainTextResponse
from rag_agent import build_agent, answer_query
from pydantic import BaseModel
import uvicorn
import requests
import tempfile
import subprocess

app = FastAPI()
qa = build_agent()

# Twilio webhook for incoming WhatsApp messages
@app.post("/webhook/twilio")
async def twilio_webhook(request: Request):
    form = await request.form()
    body = form.get("Body", "")
    num_media = int(form.get("NumMedia", "0"))
    from_number = form.get("From")
    # If audio is sent, Twilio provides MediaUrl0
    if num_media > 0:
        media_url = form.get("MediaUrl0")
        content_type = form.get("MediaContentType0")
        # fetch media and run speech-to-text
        text = await transcribe_media(media_url)
        query = text
    else:
        query = body

    result = answer_query(qa, query)
    reply_text = format_reply(result)
    # respond to Twilio with XML or simple text
    return PlainTextResponse(reply_text)

async def transcribe_media(media_url):
    # download media and call OpenAI Speech-to-Text or Whisper
    r = requests.get(media_url)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".ogg")
    tmp.write(r.content); tmp.flush()
    # Example: call OpenAI speech-to-text via requests (pseudo)
    # For demo: use whisper locally OR OpenAI speech API
    # Here we assume an external shell tool or API; keep simple:
    # Replace with actual OpenAI speech-to-text call per API docs
    txt = run_whisper_local(tmp.name)
    return txt

def run_whisper_local(file_path):
    # If you installed openai-whisper or local model, you can call it here.
    # Minimal example using whisper (python package) or system call:
    try:
        import whisper
        model = whisper.load_model("small")
        res = model.transcribe(file_path)
        return res.get("text","")
    except Exception as e:
        print("whisper local error", e)
        return ""

def format_reply(result):
    # Format the RAG response + simple citations for WhatsApp
    text = result.get("result", "")
    return text

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
