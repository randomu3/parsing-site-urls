def save_urls_to_file(urls: list, filename: str):
    with open(filename, "w") as f:
        for url in urls:
            f.write(url + "\n")
