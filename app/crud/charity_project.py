from datetime import timedelta
from typing import Optional, Union

from sqlalchemy import select, true
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import FUNDRAISING_DURATION
from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                project_name == CharityProject.name
            )
        )
        return db_project_id.scalars().first()

    async def get_projects_by_completion_rate(
            self, session: AsyncSession
    ) -> list[list[Union[str, timedelta]]]:
        """
        Provides closed projects sorted by fundraising duration.

        Columns:

        Project name - fundraising duration - project description
        """
        closed_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == true()
            ))
        closed_projects = closed_projects.scalars().all()
        data = []
        for project in closed_projects:
            name = project.name
            fundraising_duration = project.close_date - project.create_date
            description = project.description
            data.append((name, fundraising_duration, description))
        return sorted(data, key=lambda days: days[FUNDRAISING_DURATION])


charity_crud = CRUDCharityProject(CharityProject)
