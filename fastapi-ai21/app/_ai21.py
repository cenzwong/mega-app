# import ai21

# def ai21_rewrite(text, intent):
#     print(text, intent)
#     ai21.api_key = ''
#     r = ai21.Experimental.rewrite(
#         text=text, 
#         intent=intent
#     )
#     print(r)
#     return r["values"]["suggestions"]

import requests

# 
def ai21_rewrite(text, intent, key):

    url = "https://api.ai21.com/studio/v1/paraphrase"

    payload = {
        "style": f"{intent}",
        "text": f"{text}"
        }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)