from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


BLOCK_DELIMITERS = ['{%', '%}']
VARIABLE_DELIMITERS = ['{{{', '}}}']


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount('/w3images', StaticFiles(directory='w3images', html=True), name='w3images')


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
