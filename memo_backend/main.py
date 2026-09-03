from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from memo_backend.db import (
    add_memo,
    init_db,
    get_memos,
    get_memo_by_id,
    update_memo,
    delete_memo,
    set_mome_done,
    get_due_memos,
    mark_notified,
)
from memo_backend.schemas import (
    MemoCreate,
    MemoUpdate,
    MemoDoneUpdate,
    MemoRead,
    MemoReplace,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    init_db()


# 基础
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


def get_mome_or_404(memo_id: int):
    memo = get_memo_by_id(memo_id)
    if memo is None:
        raise HTTPException(status_code=404, detail="Memo not found")
    return memo


# 普通 CRUD
@app.get("/memos", response_model=list[MemoRead])
def read_memos():
    return get_memos()


@app.get("/memos/{memo_id}", response_model=MemoRead)
def get_memo(memo_id: int):
    return get_mome_or_404(memo_id)


@app.post("/memos", response_model=MemoRead, status_code=201)
def create_memo(memo: MemoCreate):
    new_id = add_memo(memo.title, memo.remind_at)
    return get_memo_by_id(new_id)


@app.delete("/memos/{memo_id}", status_code=200)
def remove_memo(memo_id: int):
    afftected = delete_memo(memo_id)
    if afftected == 0:
        raise HTTPException(status_code=404, detail="Memo not found")
    return {"message": "Memo deleted successfully"}


@app.put("/memos/{memo_id}", response_model=MemoRead)
def edit_memo(memo_id: int, memo: MemoReplace):
    affected = update_memo(memo_id, memo.title, int(memo.done), memo.remind_at)
    if affected == 0:
        raise HTTPException(status_code=404, detail="Memo not found")
    return get_memo_by_id(memo_id)


@app.patch("/memos/{memo_id}", response_model=MemoRead)
def patch_done(memo_id: int, memo: MemoUpdate):
    old_memo = get_memo_by_id(memo_id)

    new_title = memo.title if memo.title is not None else old_memo["title"]
    new_done = memo.done if memo.done is not None else old_memo["done"]
    new_remind_at = (
        memo.remind_at if memo.remind_at is not None else old_memo["remind_at"]
    )
    new_notified = memo.notified if memo.notified is not None else old_memo["notified"]
    if new_remind_at != old_memo["remind_at"]:
        new_notified = False

    update_memo(memo_id, new_title, int(new_done), new_remind_at, int(new_notified))

    return get_memo_by_id(memo_id)


# 提醒/状态


@app.patch("/memos/{memo_id}/done")
def update_memo_done(memo_id: int, memo: MemoDoneUpdate):
    affected = set_mome_done(memo_id, int(memo.done))
    if affected == 0:
        raise HTTPException(status_code=404, detail="Memo not found")
    return get_memo_by_id(memo_id)


@app.patch("/memos/{memo_id}/notified")
def update_memo_notified(memo_id: int):
    affected = mark_notified(memo_id)
    if affected == 0:
        raise HTTPException(status_code=404, detail="Memo not found")
    return {"message": "Memo notified"}


@app.get("/memos/due", response_model=list[MemoRead])
def read_due_memos():
    return get_due_memos()
