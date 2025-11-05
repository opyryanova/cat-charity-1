from fastapi import FastAPI

from app.api.endpoints import charity_project, donation
from app.core.constants import CommonMessages
from app.core.db import Base, engine


app = FastAPI(
    title=CommonMessages.APP_TITLE,
    description=CommonMessages.APP_DESCRIPTION,
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
)

app.include_router(
    charity_project.router,
    prefix='/charity_project',
    tags=['Charity Projects'],
)
app.include_router(
    donation.router,
    prefix='/donation',
    tags=['Donations'],
)


@app.on_event('startup')
async def init_models() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
