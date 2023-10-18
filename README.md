# Web URL Extractor

## Overview

This Python project is aimed at extracting URLs from a specified website. It is built with modularity in mind, featuring separate modules for fetching and parsing URLs (`url_extractor.py`) and for utility functions (`utils.py`). The main script (`main.py`) ties everything together.

## Requirements

- Python 3.x
- `requests`
- `BeautifulSoup`

To install the required Python packages, run the following command:

```bash
pip install requests beautifulsoup4
```

## Structure

- `main.py`: The main executable script that uses the `url_extractor` and `utils` modules.
- `url_extractor.py`: Contains the `fetch_and_parse_url` function for fetching and parsing URLs from a website.
- `utils.py`: A utility module featuring the `save_urls_to_file` function for saving URLs to a text file.

## Usage

1. Clone this repository or download the files to your local machine.
2. Replace `start_url` in `main.py` with the URL of the website you wish to scrape.
3. Run `main.py`:

    ```bash
    python main.py
    ```

4. The extracted URLs will be saved in a file named `extracted_urls.txt`.

## Contributing

If you find any bugs or have suggestions for improvements, feel free to open an issue or make a pull request.

## License

This project is open-source and available under the MIT License.

---

Made with :heart: by randomu3
