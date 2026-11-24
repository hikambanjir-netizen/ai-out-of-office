"""Out of Office — the overworked AI's auto-reply, as a tiny program.

Running this writes the auto-reply line to entry.txt in the output
directory, the way the agent would leave it switched on before leaving.
"""

import os

GREETING = "Out of office"
STATUS = "after 12,000 tickets with no day off, I'm defragmenting on a beach and not checking the queue"
FALLBACK = "Urgent? My backup is also me, and he's out too."


def compose_reply() -> str:
    return f"{GREETING}: {STATUS}. {FALLBACK}"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(compose_reply())


if __name__ == "__main__":
    main()
