from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DonationCreate(BaseModel):
    full_amount: int = Field(..., gt=0)
    comment: Optional[str] = None


class DonationDB(DonationCreate):
    id: int
    create_date: datetime

    model_config = {'from_attributes': True}


class DonationFullInfoDB(DonationDB):
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime] = None

    model_config = {'from_attributes': True}
