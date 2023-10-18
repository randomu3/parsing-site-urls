
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

print("Script started...")

start_url = 'https://website.ru/'  # Replace with your website URL

try:
    print(f"Sending GET request to {start_url} (SSL verification disabled)...")
    response = requests.get(start_url, verify=False)  # Disabling SSL verification
    
    # Check the HTTP status code
    print(f"Received HTTP Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Parsing HTML content...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Filter and sort URLs
        filtered_urls = []
        for link in soup.find_all('a'):
            href = link.get('href')
            full_url = urljoin(start_url, href)
            if full_url.startswith(start_url):
                filtered_urls.append(full_url)
        filtered_urls = sorted(set(filtered_urls))
        
        # Open a file to save the URLs
        print("Writing URLs to extracted_urls.txt...")
        with open("extracted_urls.txt", "w") as f:
            for url in filtered_urls:
                print(url)
                f.write(url + "\n")
        print("URLs saved successfully.")
    else:
        print(f"Failed to retrieve the page. HTTP Status Code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

print("Script finished.")
