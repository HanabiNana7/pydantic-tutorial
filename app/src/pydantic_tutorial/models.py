from datetime import date, datetime
from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


class User(BaseModel):
    """
    使用者資料模型
    """

    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=50)
    email: EmailStr
    birthday: date | None = None
    created_at: Annotated[datetime, Field(default_factory=datetime.utcnow)]

    @field_validator("name")
    @classmethod
    def strip_name(cls, v: str) -> str:
        return v.strip()

    @model_validator(mode="after")
    def check_adult(self):
        if self.birthday and (date.today() - self.birthday).days < 20 * 365:
            raise ValueError("User must be at least 20 years old")
        return self
