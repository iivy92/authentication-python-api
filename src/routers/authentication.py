from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas.user import User, UserCreated, UserToken
from src.services.authentication import AuthenticationService

router_user_v1 = APIRouter(prefix="/v1/users", tags=["Users"])


@router_user_v1.post(
    "/signup", status_code=HTTPStatus.CREATED.value, response_model=UserCreated
)
async def signup_user(user: User) -> JSONResponse:
    user_created = await AuthenticationService().signup(user)
    return JSONResponse(user_created.dict(), status_code=HTTPStatus.CREATED.value)


@router_user_v1.post(
    "/signin", status_code=HTTPStatus.OK.value, response_model=UserToken
)
async def signin_user(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
) -> JSONResponse:
    token_jwt = await AuthenticationService().signin(user_credentials)
    return JSONResponse(token_jwt.dict(), status_code=HTTPStatus.OK.value)


@router_user_v1.get("/me", status_code=HTTPStatus.OK.value, response_model=UserCreated)
async def me(
    user: UserCreated = Depends(AuthenticationService().get_token_header),
) -> JSONResponse:
    return JSONResponse(user.dict(), status_code=HTTPStatus.OK.value)