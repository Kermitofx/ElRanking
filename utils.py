from db import cur, con
from pyrogram import Filters


def generate_msg(sql_chats):
    msg = ["🏆 Trending **Groups**\n"]
    for position, chat in enumerate(sql_chats):
        if position == 0:
            prefix = "🥇"
        elif position == 1:
            prefix = "🥈"
        elif position == 2:
            prefix = "🥉"
        else:
            prefix = "🌟"
        msg.append(f"{prefix}: {chat[0]} ({chat[2]} pontos)")
    return "\n".join(msg)


def clear_db():
    cur.execute("UPDATE trd_chats SET chat_points = ?", (0,))
    con.commit()


def migrate_chat(old_chat, new_chat):
    cur.execute("UPDATE trd_chats SET chat_id = ? WHERE chat_id = ?", (new_chat, old_chat))
    con.commit()


def callback_starts(data: str or bytes):
    return Filters.create(lambda flt, cb: cb.data.split()[0] == flt.data, "CallbackStartsFilter", data=data)


def get_switch(status: bool or int):
    return "✅ ON" if status else "☑️ OFF"