import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from supadef import task


@task()
def extract_links(url):
    try:
        # Send an HTTP GET request
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags (links)
        links = soup.find_all('a')

        # Extract and normalize the URLs
        extracted_links = []
        for link in links:
            href = link.get('href')
            if href:
                # Normalize and join the URL with the base URL
                full_url = urljoin(url, href)
                extracted_links.append(full_url)

        return extracted_links

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

# if __name__ == "__main__":
#     # Example URL to parse
#     target_url = "https://example.com"
#
#     # Extract and print the links
#     links = extract_links(target_url)
#     for link in links:
#         print(link)
