import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content  # bytes


    def load_json(self):
        body = self.get_response_body()
        text = body.decode("utf-8")
        return json.loads(text)
