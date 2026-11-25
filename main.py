"""Write the alien tourist's one-line review of Earth to /output/entry.txt.

The entry is a single plain-text line (122 characters), kept byte-exact:
no trailing newline is added, so the file holds exactly the review.
"""

import os
from pathlib import Path

ENTRY = "★★★☆☆ Beautiful planet, gracious hosts — but the locals kept asking if I came in peace, then tried to sell me a timeshare."


def main() -> None:
    os.umask(0o022)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(ENTRY.encode("utf-8"))
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
