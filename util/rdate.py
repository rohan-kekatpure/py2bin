from datetime import datetime as dt

def get_timestamp():
    fmt = "%Y-%m-%d %H:%M:%S"
    return dt.now().strftime(fmt)
