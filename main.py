from url_extractor import fetch_and_parse_url
from utils import save_urls_to_file

print("Script started...")

start_url = 'https://example.com/'  # Replace with your website URL

try:
    print(f"Sending GET request to {start_url} (SSL verification disabled)...")
    urls = fetch_and_parse_url(start_url)
    
    # Open a file to save the URLs
    print("Writing URLs to extracted_urls.txt...")
    save_urls_to_file(urls, "extracted_urls.txt")
    print("URLs saved successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

print("Script finished.")
