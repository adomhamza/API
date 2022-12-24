from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schema, utils, oauth2

router = APIRouter(tags=["Authentication"])


@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = (
        db.query(schema.User)
        .filter(schema.User.email == user_credentials.username)
        .first()
    )

    if user and utils.verify(user_credentials.password, user.password):
        access_token = oauth2.create_access_token(data={"user": user.id})

        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credential"
    )
