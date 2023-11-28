import uvicorn

from config.framework import app, app_config
from config.database import db_config
from controllers import data_controller

routes_controller = [data_controller]


if __name__ == "__main__":
    app_config(routes_controller)
    db_config()

    uvicorn.run(app, host="127.0.0.1", port=8000)

