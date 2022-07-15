from pytemplates_fastapi.app.app import app
from pytemplates_fastapi.app.router import router

app.include_router(router)


if __name__ == "__main__":
    app()
