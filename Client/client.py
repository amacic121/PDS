import requests

url = "http://192.168.1.102:8080/users"

payload = "{\r\n    \"ime\": \"Andrej\",\r\n    \"prezime\": \"Macic\",\r\n    \"smer\": \"RI\",\r\n    \"predmeti\": [\r\n        {\r\n            \"ime\": \"Linearna algebra i analiticka geometrijai\",\r\n            \"espb\": \"8\"\r\n        },{\r\n        \t\"ime\": \"Diskretne strukture\",\r\n            \"espb\": \"8\"\r\n        },{\r\n        \t\"ime\": \"Napredna matematicka analiza\",\r\n            \"espb\": \"8\"\r\n        },{\r\n        \t\"ime\": \"Vestacka inteligencija\",\r\n            \"espb\": \"8\"\r\n        },{\r\n        \t\"ime\": \"Namenski racunarski sistemi\",\r\n            \"espb\": \"8\"\r\n        },{\r\n        \t\"ime\": \"Povezivanje mreza\",\r\n            \"espb\": \"8\"\r\n        },{\r\n        \t\"ime\": \"Napredno web programiranje\",\r\n            \"espb\": \"8\"\r\n        }\r\n    ]\r\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "93209b96-2860-91de-471d-347cde84be2a"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)