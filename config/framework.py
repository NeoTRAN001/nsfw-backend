from fastapi import FastAPI

app = FastAPI()


def app_config(controllers):
    app.title = 'NSFW Backend'
    app.version = '0.0.1'

    for controller in controllers:
        app.include_router(controller.router)