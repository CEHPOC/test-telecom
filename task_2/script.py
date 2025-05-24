import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
logger = logging.getLogger(__name__)

def make_request(url):
    response = requests.get(url)

    if response.status_code < 400:
        logger.info(f"Request to {url} succeeded with status {response.status_code}")
        logger.info(f"Response body: {response.text}")
    else:
        error_msg = f"Request to {url} failed with status {response.status_code}"
        logger.error(error_msg)
        raise Exception(error_msg)

test_urls=[
    "https://httpstat.us/101",
    "https://httpstat.us/200",
    "https://httpstat.us/305",
    "https://httpstat.us/404",
    "https://httpstat.us/500"
]

if __name__ == "__main__":
    for url in test_urls:
        try:
            make_request(url)
        except Exception as e:
            logger.error(f"Error processing request to {url}: {str(e)}")

