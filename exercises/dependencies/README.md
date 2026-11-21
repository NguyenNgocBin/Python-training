# Bài tập FastAPI Dependencies

Hoàn thành TODO trong [main.py](main.py) để cùng một dependency xác định người dùng cho `/me`, `/orders` và `/settings`. Bài tập dùng dữ liệu trong bộ nhớ và token cố định dành cho thực hành.

## Chạy code khung

Chạy hai lệnh sau trong PowerShell.

```powershell
Set-Location D:/FastAPI/exercises/dependencies
python -m uvicorn main:app --reload --port 8001
```

Mở một PowerShell khác để gửi request. Lúc đầu, `GET /health` trả `200`. Ba route còn lại trả `501` để đánh dấu phần cần hoàn thành.

## TODO 1 · Đọc token từ request

Hoàn thành `get_bearer_token`. FastAPI đã được khai báo lấy giá trị `authorization` từ header `Authorization` bằng `Header()`. Tham số có mặc định `None` để hàm tự xử lý khi header vắng mặt.

- Chấp nhận header dạng `Bearer <token>`. Scheme `Bearer` không phân biệt hoa thường.
- Trả về phần token, ví dụ `demo-linh`. Nếu thiếu header, sai scheme, thiếu token hoặc có thêm thành phần, dùng `raise unauthorized()`.
- Dùng `split()` để kiểm tra số thành phần. Thử gọi trực tiếp `get_bearer_token("Bearer demo-linh")` trước khi gắn nó vào một route.

## TODO 2 · Gắn dependency vào `/me`

1. Thêm tham số `token` cho `get_current_user`. Dùng `Annotated` và `Depends` để khai báo giá trị đến từ `get_bearer_token`.
2. Tra token trong `TOKEN_TO_USER_ID`, rồi lấy `User` tương ứng từ `USERS`. Dùng `raise unauthorized()` khi token lạ hoặc ID trỏ tới người dùng đã bị xóa. `demo-deleted` là dữ liệu để thử trường hợp thứ hai.
3. Thêm tham số `user` cho `read_me` và trả chính `user` đó. Mẫu chung là `tham_so: Annotated[KieuDuLieu, Depends(ham_cung_cap)]`. Truyền hàm vào `Depends` để FastAPI gọi khi có request.

Thêm tạm `print("read_me chạy")` vào đầu `read_me`. Gửi một request hợp lệ rồi một request sai token. Bạn chỉ nên thấy dòng in ở request hợp lệ.

## TODO 3 · Dùng lại dependency cho hai route

- Thêm tham số `user` vào `read_orders` và `read_settings`, cùng khai báo `Depends(get_current_user)`.
- Dùng `user.id` làm khóa tra dữ liệu từ `ORDERS_BY_USER_ID` hoặc `SETTINGS_BY_USER_ID`.
- Gửi cùng một request với hai token để thấy một endpoint có thể nhận hai người dùng khác nhau.

## TODO 4 · Thêm dependency lồng nhau

- Cho `get_user_store()` trả về `USERS`.
- Thêm tham số `store` cho `get_current_user`, khai báo `Depends(get_user_store)`, rồi dùng `store` để tra người dùng.
- Thêm `print()` tạm thời vào đầu bốn hàm. Với `GET /me` có token hợp lệ, dự đoán thứ tự trước khi chạy. Hai dependency con được giải quyết trước khi `get_current_user` nhận được đủ tham số.

```text
GET /me
└── read_me(user)
    └── get_current_user(token, store)
        ├── get_bearer_token(authorization)
        └── get_user_store()
```

## Các trường hợp tự kiểm tra

```powershell
curl.exe -i http://127.0.0.1:8001/health
curl.exe -i -H "Authorization: Bearer demo-linh" http://127.0.0.1:8001/me
curl.exe -i -H "Authorization: Bearer demo-minh" http://127.0.0.1:8001/orders
curl.exe -i -H "Authorization: Bearer demo-deleted" http://127.0.0.1:8001/me
curl.exe -i http://127.0.0.1:8001/settings
```

| Request | Header `Authorization` | Kết quả mong đợi |
| --- | --- | --- |
| `GET /health` | Thiếu | `200`, `{"status":"ok"}` |
| `GET /me` | `Bearer demo-linh` | `200`, `{"id":1,"name":"Linh"}` |
| `GET /me` | `bearer demo-minh` | `200`, `{"id":2,"name":"Minh"}` |
| `GET /orders` | `Bearer demo-linh` | `200`, `[{"id":101,"item":"Notebook"}]` |
| `GET /orders` | `Bearer demo-minh` | `200`, `[]` |
| `GET /settings` | `Bearer demo-linh` | `200`, `{"theme":"dark"}` |
| `GET /settings` | `Bearer demo-minh` | `200`, `{"theme":"light"}` |
| Cả ba route | Thiếu, `Basic demo-linh`, `Bearer`, `Bearer demo-linh extra`, `Bearer demo-unknown` hoặc `Bearer demo-deleted` | `401`, `{"detail":"Not authenticated"}` và header `WWW-Authenticate: Bearer` |

## Bài mở rộng

### TODO 5 · Kiểm thử endpoint bằng người dùng giả

Trong một file `check_me.py` cùng thư mục, import `app`, `User`, `get_current_user` và `read_me` từ `main`. Dùng `TestClient` từ `fastapi.testclient`. Môi trường FastAPI hiện tại cần cài thêm `httpx2` cho bước này (`python -m pip install httpx2`).

1. Viết một hàm không nhận tham số, trả về `User(id=99, name="Người dùng test")`.
2. Gán hàm đó làm giá trị cho khóa `get_current_user` trong `app.dependency_overrides`.
3. Gửi `GET /me` không kèm header qua `TestClient(app)`. Kiểm tra mã `200` và JSON của người dùng test. Dọn override trong `finally` bằng `app.dependency_overrides.pop(get_current_user, None)`, rồi gửi lại request. Lần này kết quả phải là `401`.

Thử so sánh với việc gọi trực tiếp `read_me(user_mau)`. Cách gọi nào đi qua cơ chế dependency của FastAPI? [Tài liệu về dependency override](https://fastapi.tiangolo.com/advanced/testing-dependencies/)

### TODO 6 · Đếm số lần gọi trong một request

Thêm tạm một tham số thứ hai vào `read_me` với cùng khai báo `Depends(get_current_user)`. In một dòng ở đầu `get_current_user`. Khi gửi một request, bạn sẽ thấy một lần in. Giữ nguyên tham số thứ nhất và thêm `use_cache=False` vào `Depends` của tham số thứ hai. Gửi lại request để thấy hai lần in. Gỡ tham số thử nghiệm khi xong. [Tài liệu về cache dependency](https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/#using-the-same-dependency-multiple-times)

### TODO 7 · Quan sát vòng đời với `yield`

Đổi `get_user_store` thành hàm sinh có kiểu trả về `Generator[dict[int, User], None, None]` từ `collections.abc`. In `store: open` trước `try`, rồi `yield USERS` trong `try` và in `store: close` trong `finally`. Thử cả token hợp lệ lẫn `demo-deleted`. Lần thứ hai kho đã được lấy trước khi `get_current_user` phát sinh lỗi `401`, nên bạn vẫn thấy `store: close`.

Mở [`get_db()` trong dự án Todo](../../todo-list/app/db/session.py#L12) và chỉ ra dòng cấp phiên SQLAlchemy cùng dòng đóng phiên. Trong FastAPI, vị trí khai báo quyết định route nào dùng dependency. Tham số `scope=` của `Depends` điều khiển thời điểm dọn dẹp dependency có `yield`. Với `scope="function"`, phần dọn dẹp chạy trước khi gửi response. Với `scope="request"` mặc định cho dependency có `yield`, phần đó chạy sau khi gửi response. [Tài liệu về `yield` và `scope`](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#early-exit-and-scope)

## Đối chiếu với mã nguồn FastAPI

Các dòng dưới đây theo FastAPI **0.162.0** đang cài trong môi trường. Lệnh sau in đường dẫn đến thư mục chứa mã nguồn.

```powershell
python -c "import fastapi; from pathlib import Path; print(Path(fastapi.__file__).parent)"
```

| Mã nguồn | Điều cần tìm |
| --- | --- |
| `param_functions.py:2391` và `:2477` | `Depends` tạo một đối tượng khai báo chứa callable cần gọi. |
| `dependencies/utils.py:321–359` | `get_dependant` đọc chữ ký hàm rồi gọi đệ quy để xây cấu trúc dependency con. |
| `dependencies/utils.py:680–737` | `solve_dependencies` chọn override nếu có, giải dependency con, gọi hàm hoặc lấy kết quả từ cache, rồi đặt kết quả vào `values` theo tên tham số. |
| `routing.py:745–749` | FastAPI chuyển `solved_result.values` đến hàm gọi endpoint. |
| `dependencies/utils.py:627–631` và `:719–729` | FastAPI đưa hàm sinh vào context manager để quản lý phần `yield` và dọn dẹp. |

Đọc dòng `values[sub_dependant.name] = solved`. Trong chữ ký `read_me(user: ...)`, khóa này là gì, và giá trị đến từ lời gọi hàm nào?
