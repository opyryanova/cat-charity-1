from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectCreate


class CharityProjectCRUD:
    async def get_project_by_name(
        self,
        session: AsyncSession,
        project_name: str
    ) -> CharityProject | None:
        result = await session.execute(
            select(CharityProject).where(CharityProject.name == project_name)
        )
        return result.scalars().first()

    async def create(
        self,
        session: AsyncSession,
        obj_in: CharityProjectCreate
    ) -> CharityProject:
        new_project = CharityProject(**obj_in.model_dump())
        session.add(new_project)
        await session.commit()
        await session.refresh(new_project)
        return new_project


charity_project_crud = CharityProjectCRUD()
