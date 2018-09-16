def to_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default
