from datetime import date

from src.pydantic_tutorial.models import User


def demo():
    user = User.model_validate(
        {
            "id": 1,
            "name": "MilkTea",
            "email": "milktea@example.com",
            "birthday": date(2000, 1, 1),
        }
    )
    print("→ dict :", user.model_dump())
    print("→ JSON :", user.model_dump_json(indent=2))


if __name__ == "__main__":
    demo()
