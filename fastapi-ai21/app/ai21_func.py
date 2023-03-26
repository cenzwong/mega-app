

# import requests

# def ai21_rewrite(text, intent):
#     api_key = ''
#     r = requests.post(
#         "https://api.ai21.com/studio/v1/experimental/rewrite",
#         headers={"Authorization": f"Bearer {api_key}"},
#         json={
#             "text": text,
#             "intent": "general"
#         }
#     )
#     print(r.json())
#     return r.json()["suggestions"]

# ai21_rewrite("Tomorrow is a good day.", "general")
