from fastapi import FastAPI

from .routers.calculation import router as routes
from .routers.filters import router as filters

app = FastAPI(
    title="Aeroflot App"
)

app.include_router(routes)
app.include_router(filters)
