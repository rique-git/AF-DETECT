from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware

from app.api import router
from app.dash_app.app import create_dash_app

from app.config import PORT, DEBUG


def create_app():

    fastapi_app = FastAPI()

    # Register API routes
    fastapi_app.include_router(router)

    # Create Dash
    dash_app = create_dash_app()

    # Mount Dash
    fastapi_app.mount(
        "/",
        WSGIMiddleware(dash_app.server)
    )

    return fastapi_app


app = create_app()


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=PORT,
        reload=True
    )
