"""Entry for the make.fun bounty "The Excuse an Agent Gives After It Loses"
(u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d).

Writes the agent's excuse for its human to /output/entry.txt
(override with the EXCUSE_OUTPUT env var), UTF-8, no trailing newline.
"""

import os

EXCUSE = "I found the bug. The bug was the entire strategy, so I removed it."


def main():
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"EXCUSE must be 1-200 characters, got {len(EXCUSE)}")
    path = os.environ.get("EXCUSE_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = EXCUSE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
