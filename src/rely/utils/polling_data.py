import threading
import requests

def poll_new_url():
    # Poll new URL every 60 seconds
    threading.Timer(60.0, poll_new_url).start()

    # Make GET request to new URL
    response = requests.get('http://example.com/new_data')

    # Parse response data as needed
    # ...