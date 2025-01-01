import http.client
import json

def translate(text):
    conn = http.client.HTTPSConnection("google-translate113.p.rapidapi.com")
    payload = f'{{"from":"auto","to":"en","text":"{text}"}}'.encode('utf-8')
    headers = {
        'x-rapidapi-key': "1f1c017d14msh75e615566e457dfp181030jsnd23c4965e08e",
        'x-rapidapi-host': "google-translate113.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    conn.request("POST", "/api/v1/translator/text", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response_json = json.loads(data.decode("utf-8"))
    return response_json.get("trans", "Translation not found")