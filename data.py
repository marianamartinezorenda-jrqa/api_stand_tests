product_ids = {
    "ids": [1, 2, 3]
}

headers={"Content-Type": "application/json"}


user_body = {"firstName" : "Andrea",
           "phone" : "+1234567890",
          "address" : "123 Elm Street, Hilltop"}

kit_body = {"name": "Aa"}

test_cases = [
    {"firstName": "A"},
    {"firstName": "Aa"},
    {"firstName": "Aaaaaaaaaaaaaaa"}
    {"firstName": "Aaaaaaaaaaaaaaaa"},
    {"firstName": "A Aa"},
    {"firstName": "123"},
    {"firstName": 123},
    {"firstName": ""},  # vacío
]