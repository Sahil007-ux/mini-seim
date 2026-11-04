import re


def normalize_log(log):
    """
    Convert a raw SSH log into a structured event.
    """

    pattern = (
        r"(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}) "
        r"(?P<hostname>\S+) "
        r"(?P<service>\w+)\[\d+\]: "
        r"(?P<message>.*)"
    )

    match = re.match(pattern, log)

    if not match:
        return None

    event = match.groupdict()

    message = event.pop("message")

    event["event_type"] = "unknown"
    event["username"] = None
    event["source_ip"] = None

    failed_login = re.search(
        r"Failed password for (?:invalid user )?(?P<username>\S+) "
        r"from (?P<ip>\d+\.\d+\.\d+\.\d+)",
        message
    )

    successful_login = re.search(
        r"Accepted password for (?P<username>\S+) "
        r"from (?P<ip>\d+\.\d+\.\d+\.\d+)",
        message
    )

    if failed_login:
        event["event_type"] = "failed_login"
        event["username"] = failed_login.group("username")
        event["source_ip"] = failed_login.group("ip")

    elif successful_login:
        event["event_type"] = "successful_login"
        event["username"] = successful_login.group("username")
        event["source_ip"] = successful_login.group("ip")

    return event