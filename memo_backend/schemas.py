from pydantic import BaseModel  # 数据校验工具
from datetime import datetime


class MemoBase(BaseModel):
    title: str


class MemoCreate(MemoBase):
    remind_at: datetime | None = None


class MemoReplace(BaseModel):
    title: str
    done: bool
    remind_at: datetime | None = None


class MemoUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None
    remind_at: datetime | None = None
    notified: bool | None = None


class MemoDoneUpdate(BaseModel):
    done: bool


class MemoRead(MemoBase):
    id: int
    done: bool
    remind_at: datetime | None = None
    notified: bool
