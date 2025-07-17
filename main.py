from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/api/tiktok")
async def tiktok(request: Request):
    url = request.query_params.get("url")
    r = requests.get(f'https://tikwm.com/api/?url={url}')
    if r.status_code == 200:
        d = r.json()
        return {
            "video": d["data"]["play"],
            "music": d["data"]["music"]
        }
    return {"error": "فشل الاتصال"}
