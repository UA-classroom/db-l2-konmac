from fastapi import FastAPI
from typing import List
from test_model import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Ahmed",
        gender = Gender.female,
        roles=[Role.student, Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Alex",
        last_name="Jones",
        gender = Gender.female,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"HEllo: Mundo"}