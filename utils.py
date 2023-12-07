def fix_protocol(url) -> str:
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url