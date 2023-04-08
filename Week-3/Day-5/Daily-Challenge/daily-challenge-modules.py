import requests
import time

def get_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    return end_time - start_time

url = 'https://www.google.com'
load_time = get_page_load_time(url)
print(f'The page at {url} took {load_time:.2f} seconds to load.')