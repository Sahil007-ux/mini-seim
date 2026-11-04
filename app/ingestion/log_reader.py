from pathlib import Path


def read_logs(file_path):
    """
    Read log entries from a file.

    Args:
        file_path: Path to the log file.

    Returns:
        A list containing individual log entries.
    """

    log_entries = []

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {path}")
  
    with path.open("r", encoding="utf-8", errors="replace") as file:
        for line in file:
            line = line.strip()

            if line:
                log_entries.append(line)

    return log_entries