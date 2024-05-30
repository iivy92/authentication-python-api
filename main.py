from fastapi import FastAPI
from src.routers import users


def create_app() -> FastAPI:
    app = FastAPI(
        title="Authentication API",
        version="1.0.0"
    )
    app.include_router(users.router_user_v1)
    return app

app = create_app()