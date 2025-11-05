from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.models.donation import Donation


async def invest_new_project(
    project: CharityProject,
    session: AsyncSession,
) -> CharityProject:
    donations = await session.execute(
        select(Donation)
        .where(Donation.fully_invested.is_(False))
        .order_by(Donation.create_date)
    )
    donations = donations.scalars().all()

    for donation in donations:
        if project.fully_invested:
            break

        amount = min(
            project.full_amount - project.invested_amount,
            donation.full_amount - donation.invested_amount,
        )

        project.invested_amount += amount
        donation.invested_amount += amount

        if project.invested_amount == project.full_amount:
            project.fully_invested = True
            project.close_date = datetime.utcnow()

        if donation.invested_amount == donation.full_amount:
            donation.fully_invested = True
            donation.close_date = datetime.utcnow()

        session.add(project)
        session.add(donation)

    await session.commit()
    await session.refresh(project)
    return project


async def invest_donation(
    donation: Donation,
    session: AsyncSession,
) -> Donation:
    projects = await session.execute(
        select(CharityProject)
        .where(CharityProject.fully_invested.is_(False))
        .order_by(CharityProject.create_date)
    )
    projects = projects.scalars().all()

    for project in projects:
        if donation.fully_invested:
            break

        amount = min(
            donation.full_amount - donation.invested_amount,
            project.full_amount - project.invested_amount,
        )

        donation.invested_amount += amount
        project.invested_amount += amount

        if project.invested_amount == project.full_amount:
            project.fully_invested = True
            project.close_date = datetime.utcnow()

        if donation.invested_amount == donation.full_amount:
            donation.fully_invested = True
            donation.close_date = datetime.utcnow()

        session.add(project)
        session.add(donation)

    await session.commit()
    await session.refresh(donation)
    return donation
