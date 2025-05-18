from datetime import date

import pytest
from pydantic import ValidationError
from src.pydantic_tutorial.models import User


def test_user_validation_success():
    user = User.model_validate(
        {"id": 1, "name": "MilkTea", "email": "milktea@example.com"}
    )
    assert user.id == 1
    assert user.name == "MilkTea"
    assert user.email == "milktea@example.com"


def test_user_validation_email_failure():
    with pytest.raises(ValidationError) as exc_info:
        User.model_validate({"id": 1, "name": "MilkTea", "email": "milktea"})
    assert "value is not a valid email address" in str(exc_info.value)


def test_user_validation_birthday_failure():
    with pytest.raises(ValidationError) as exc_info:
        User.model_validate(
            {
                "id": 1,
                "name": "MilkTea",
                "email": "milktea@example.com",
                "birthday": date(2024, 1, 1),
            }
        )
    assert "User must be at least 20 years old" in str(exc_info.value)
