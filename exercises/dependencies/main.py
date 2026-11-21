from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Bài tập FastAPI Dependencies")


class User(BaseModel):
    id: int
    name: str


class Order(BaseModel):
    id: int
    item: str


class Settings(BaseModel):
    theme: str


# Kho người dùng mẫu. Khóa là ID của từng người dùng.
USERS = {
    1: User(id=1, name="Linh"),
    2: User(id=2, name="Minh"),
}

# Tra token để lấy ID, rồi dùng ID đó để tìm User trong USERS.
TOKEN_TO_USER_ID = {
    "demo-linh": 1,
    "demo-minh": 2,
    "demo-deleted": 99,
}

ORDERS_BY_USER_ID = {
    1: [Order(id=101, item="Notebook")],
    2: [],
}

SETTINGS_BY_USER_ID = {
    1: Settings(theme="dark"),
    2: Settings(theme="light"),
}


# Dùng raise unauthorized() để dừng xử lý và trả lỗi 401.
def unauthorized() -> HTTPException:
    return HTTPException(
        status_code=401,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )


# Khi FastAPI gọi hàm, Header() lấy giá trị từ header Authorization của request.
# Nếu request thiếu header, authorization nhận giá trị mặc định None.

# TODO 1 - Kiểm tra header Authorization và trả về phần token.
    # 1. Khi authorization là None, dùng raise unauthorized().
    # 2. Dùng split() để tách, ví dụ "Bearer demo-linh" thành ["Bearer", "demo-linh"].
    # 3. Kiểm tra có đúng hai phần và phần đầu là "bearer" sau khi dùng lower().
    #    Sai một trong hai điều kiện thì dùng raise unauthorized().
    # 4. Trả về phần thứ hai, ví dụ "demo-linh".
    # Thay dòng 501 bên dưới bằng phần bài làm của bạn.
def get_bearer_token(authorization: Annotated[str | None, Header()] = None) -> str:
    # Nếu request thiếu header Authorization thì báo lỗi 401.
    if authorization is None:
        raise unauthorized()
    #Dùng split() để tách, ví dụ "Bearer demo-linh" thành ["Bearer", "demo-linh"].
    parts = authorization.split(" ")
    # Header phải có đúng hai phần thì mới gán được vào hai biến bên dưới.
    if len(parts) != 2:
        raise unauthorized()
    scheme, token =parts

    # lower() cho phép cả "Bearer" và "bearer".
    if scheme.lower() != "bearer":
        raise unauthorized()
    return token

def get_user_store() -> dict[int, User]:
    # TODO 4 - Trả về kho người dùng mẫu.
    # Khi được khai báo trong Depends, giá trị trả về sẽ được truyền vào get_current_user.
    return USERS


def get_current_user(
    token: Annotated[str, Depends(get_bearer_token)],
) -> User:
    # Tra token để lấy ID người dùng.
    user_id = TOKEN_TO_USER_ID.get(token)
    if user_id is None:
        raise unauthorized()

    # Dùng ID để lấy người dùng trong bảng USERS.
    user = USERS.get(user_id)
    if user is None:
        raise unauthorized()

    return user


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/me")
def read_me(user: Annotated[User, Depends(get_current_user)]) -> User:
    return user


@app.get("/orders")
def read_orders(user: Annotated[User, Depends(get_current_user)]) -> list[Order]:
    return ORDERS_BY_USER_ID.get(user.id, [])


@app.get("/settings")
def read_settings(user: Annotated[User, Depends(get_current_user)]) -> Settings:
    return SETTINGS_BY_USER_ID.get(user.id, Settings(theme="light"))