
TEMPLATE = """
<html>
<head>
<meta http-equiv="refresh" content="0; url=URLSTR">
</head>
</html>
"""

def url_conv(url: str, filename: str):
    new_url = TEMPLATE.replace("URLSTR", url)
    with open(filename + ".html", "w") as f:
        f.write(new_url)
    print(new_url)
    print(f"successfully created web file: {filename} with url: {url}")
