from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/api/whoami")
def read_headers(request: Request):
    
    client_host = request.client.host
    language = request.headers['accept-language']
    software = request.headers["user-agent"]

    return {"client_host": client_host, "Language": language, "Software": software}
