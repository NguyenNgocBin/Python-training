from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.schemas.user import User


# Dữ liệu giả để thử dependency ngay trên Swagger.
USERS = {
    1: User(id=1, name="Linh"),
    2: User(id=2, name="Minh"),
}
TOKEN_TO_USER_ID = {
    "demo-linh": 1,
    "demo-minh": 2,
    "demo-deleted": 99,
}

# HTTPBearer khai báo kiểu xác thực để Swagger hiện nút Authorize.
bearer = HTTPBearer(
    auto_error=False,
    description="Token mẫu để thực hành là demo-linh hoặc demo-minh.",
)


def unauthorized() -> HTTPException:
    return HTTPException(
        status_code=401,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )


def get_bearer_token(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer)],
) -> str:
    # Lấy chuỗi token và tự trả 401 nếu HTTPBearer trả về None.
    if credentials is None:
        raise unauthorized()
    return credentials.credentials


def get_user_store() -> dict[int, User]:
    return USERS


def get_current_user(
    token: Annotated[str, Depends(get_bearer_token)],
    store: Annotated[dict[int, User], Depends(get_user_store)],
) -> User:
    # FastAPI chuẩn bị cả token và bảng người dùng trước khi chạy thân hàm.
    user_id = TOKEN_TO_USER_ID.get(token)
    if user_id is None:
        raise unauthorized()

    user = store.get(user_id)
    if user is None:
        raise unauthorized()
    return user
