import sqlite3
from datetime import datetime

DB_NAME = "memos.db"


# 基础
def get_conn():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0,
            remind_at TEXT
        )
    """)
    conn.commit()
    conn.close()


# 普通 CRUD
def add_memo(title: str, remind_at: datetime | None):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO memos (title, done, remind_at, notified) VALUES (?,?, ?, ?)",
        (
            title,
            0,
            remind_at.isoformat() if remind_at else None,
            0,
        ),
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def update_memo(
    memo_id: int,
    title: str,
    done: int,
    remind_at: datetime | None,
    notified: int,
):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE memos SET title= ?,done=?,remind_at=?,notified=? WHERE id = ?",
        (
            title,
            done,
            remind_at.isoformat() if remind_at else None,
            notified,
            memo_id,
        ),
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


def delete_memo(memo_id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM memos WHERE id = ?",
        (memo_id,),
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


def get_memos():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title,done,remind_at, notified  FROM memos ORDER BY id DESC"
    )
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "title": row[1],
            "done": bool(row[2]),
            "remind_at": datetime.fromisoformat(row[3]) if row[3] else None,
            "notified": bool(row[4]),
        }
        for row in rows
    ]


def get_memo_by_id(memo_id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, done,remind_at, notified FROM memos WHERE id = ?",
        (memo_id,),
    )
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return None
    return {
        "id": row[0],
        "title": row[1],
        "done": bool(row[2]),
        "remind_at": datetime.fromisoformat(row[3]) if row[3] else None,
        "notified": bool(row[4]),
    }


# 提醒/状态


def set_mome_done(memo_id: int, done: bool):
    conn = get_conn()
    cursor = conn.cursor()
    if done:
        cursor.execute(
            "UPDATE memos SET done = ? WHERE id=?",
            (1, memo_id),
        )
    else:
        cursor.execute(
            "UPDATE memos SET done = ?, notified = ? WHERE id=?",
            (0, 0, memo_id),
        )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected


def get_due_memos():
    conn = get_conn()
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    cursor.execute(
        """
        SELECT id,title,done,remind_at FROM memos
        WHERE done = 0
            AND notified = 0
            AND remind_at IS NOT NULL
            AND remind_at <=?
        ORDER BY remind_at ASC
        """,
        (now,),
    )
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "title": row[1],
            "done": bool(row[2]),
            "remind_at": datetime.fromisoformat(row[3]) if row[3] else None,
            "notified": bool(row[4]),
        }
        for row in rows
    ]


def mark_notified(memo_id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE memos SET notified = 1 WHERE id=?",
        (memo_id,),
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected
