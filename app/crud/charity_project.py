from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectCreate


class CRUDCharityProject(CRUDBase[CharityProject, CharityProjectCreate]):
    async def get_project_by_name(self, session, name: str):
        result = await session.execute(
            select(CharityProject).where(CharityProject.name == name)
        )
        return result.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)
