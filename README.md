
# Web Scraping Project

## Overview

This Python script is designed to scrape all the URLs from a specific website and save them to a text file. The script uses the `requests` and `BeautifulSoup` libraries to fetch the website content and parse the HTML, respectively.

## Requirements

- Python 3.x
- `requests`
- `BeautifulSoup`

Install the required Python packages using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone this repository or download the script to your local machine.
2. Open the script in a text editor and replace `start_url` with the URL of the website you want to scrape. For example, replace it with `https://example.com`.

```python
start_url = 'https://example.com'  # Replace with your website URL
```

3. Save the script and run it using Python:

```bash
python your_script_name.py
```

The script will output the URLs to the console and save them to a text file named `extracted_urls.txt`.

**Note**: The script disables SSL certificate verification by default for debugging purposes. It's not recommended to keep it disabled for production use due to security risks.

## Troubleshooting

The script contains debug prints to help identify issues related to network errors or HTML parsing. If you encounter any issues, the debug information will be printed to the console.

## License

This project is open-source and available under the MIT License.

