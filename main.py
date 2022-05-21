from fastapi import FastAPI, Request, form
from fastapi.templating import Jinja2templates

app = FastAPI()
templates = Jinja2templates(directory="/code")

@app.get("/")
def form_post(request: Request):
    return templates.TemplateResponce('form.html', context={'request': request})
