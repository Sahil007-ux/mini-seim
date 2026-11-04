from pathlib import Path

from app.ingestion.log_reader import read_logs
from app.normalization.parser import normalize_log


def main():
    project_root = Path(__file__).resolve().parent.parent

    log_file = project_root / "data" / "sample" / "auth.log"

    logs = read_logs(log_file)

    print(f"\nTotal logs collected: {len(logs)}")

    print("\nNormalized security events:\n")

    for log in logs:
        event = normalize_log(log)

        if event:
            print(event)


if __name__ == "__main__":
    main()