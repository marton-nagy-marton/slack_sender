from dotenv import load_dotenv
import os
load_dotenv()

import requests

headers = {
    'Content-type': 'application/json',
}

json_data = {
    'text': 'Hello, slack!',
}

response = requests.post(
    f"https://hooks.slack.com/services/T083FD52J10/B083J1S1YMS/{os.environ.get('SLACK_ID')}",
    headers=headers,
    json=json_data,
)

print(response)
