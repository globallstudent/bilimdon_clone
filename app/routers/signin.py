from fastapi import APirouter, Depends, HTTPException, status as http_status
from app.schemas.login import SignIn, SignInResponse
from app.dependencies import get_db
from app.models import User
from sqlalchemy.orm import Session


router = APirouter(prefix="/auhtentication", tags=["Authentication"])


@router.post("/signin", response_model)


def signin(db_session: Session = Depends(get_db), user: SignIn):
    """
    Sign in a user with email and password.
    """
    db_user = db_session.query(User).filter(User.email == user.email).first()
    
    if not db_user:
        raise HTTPException(
            status_code=http_status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not db_user.verify_password(user.password):
        raise HTTPException(
            status_code=http_status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return SignInResponse.from_orm(db_user)