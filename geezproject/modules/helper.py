""" geezproject module for other small commands. """
from geezproject import CMD_HANDLER as cmd
from geezproject import CMD_HELP
from geezproject.utils import edit_or_reply, geez_cmd


@geez_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari GeezProjects:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-GeezProjects-09-22)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}ihelp`\
        \n  ββΈ : **Bantuan Untuk GeezProjects.\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}listvar`\
        \n  ββΈ : **Melihat Daftar Vars.\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}repo`\
        \n  ββΈ : **Melihat Repository GeezProjects.\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}string`\
        \n  ββΈ : **Link untuk mengambil String GeezProjects.\
    "
    }
)
