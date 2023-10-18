
# Web Scraping Project: NPF-SNG URL Extractor

## Repository Name
`parsing-site-urls`

## Description

This project is aimed at extracting all URLs that belong to the domain `https://site.ru/` from the website's main page. The URLs are sorted and saved in a text file named `extracted_urls.txt` for further analysis.

## Prerequisites

1. Python 3.x
2. `requests` library
3. `BeautifulSoup` library

To install the required packages, run:
```
pip install requests beautifulsoup4
```

## How to Run

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the script by executing `python domain_filtered_main.py`.

## Features

- Extracts URLs only from the specified domain
- Sorts the URLs
- Saves the URLs to a text file

## Warnings

The script is set to ignore SSL certificate verification for debugging purposes. This is not recommended for production use due to security risks.

## Contributing

Feel free to submit pull requests to improve the project.

## License

This project is licensed under the MIT License.

## Author

[randomu3]
