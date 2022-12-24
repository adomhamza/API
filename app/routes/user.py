from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import session
from ..database import get_db
from typing import List
from .. import models, schema, utils

router = APIRouter(prefix="/user", tags=["User"])


# Gets all users


@router.get(
    "", status_code=status.HTTP_200_OK, response_model=List[models.ResponseUserModel]
)
def get_all_users(db: session = Depends(get_db)):
    users = db.query(schema.User).all()
    if len(users) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing Here"
        )
    return users


# Gets specific user by phone_number


@router.get(
    "/{phone_number}",
    status_code=status.HTTP_200_OK,
    response_model=models.ResponseUserModel,
)
def get_user(phone_number: int, db: session = Depends(get_db)):
    user = (
        db.query(schema.User).filter(schema.User.phone_number == phone_number).first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{phone_number} Not found"
        )
    return user


# Create/Post a new user
@router.post(
    "", status_code=status.HTTP_201_CREATED, response_model=models.ResponseUserModel
)
def create_user(user: models.User, db: session = Depends(get_db)):
    hashed_pwd = utils.hash_password(user.password)
    user.password = hashed_pwd

    query_email = db.query(schema.User).filter(schema.User.email == user.email).first()

    query_phone_number = (
        db.query(schema.User)
        .filter(schema.User.phone_number == user.phone_number)
        .first()
    )
    print(query_phone_number, query_email)

    if query_email or query_phone_number:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist"
        )

    create_user = schema.User(**user.dict())
    db.add(create_user)
    db.commit()
    db.refresh(create_user)
    return create_user


# Delete a user from the database by phone_number


@router.delete("/{phone_number}", status_code=status.HTTP_200_OK)
def delete_user(phone_number: int, db: session = Depends(get_db)):
    deleted = db.query(schema.User).filter(schema.User.phone_number == phone_number)
    if deleted.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{phone_number} does not exist.",
        )
    deleted.delete(synchronize_session=False)

    db.commit()
    return f"{phone_number} deleted successfully"


# Updates specific user by phone_number


@router.put(
    "/{phone_number}",
    status_code=status.HTTP_200_OK,
    response_model=models.ResponseUserModel,
)
def update_user(phone_number: int, user: models.User, db: session = Depends(get_db)):

    update = db.query(schema.User).filter(schema.User.phone_number == phone_number)

    if update.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{phone_number} not found"
        )
    update.update(user.dict(), synchronize_session=False)
    db.commit()
    return update.first()
