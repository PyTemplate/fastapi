from pytemplates_fastapi.app import app
from pytemplates_fastapi.routes import message, root

app.include_router(root.router)
app.include_router(message.router)

if __name__ == "__main__":
    app()
