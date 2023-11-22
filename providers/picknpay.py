import requests
import json


class PickNPayAPI:
    def __init__(self, base_url, store_code, language, currency):
        self.base_url = base_url
        self.store_code = store_code
        self.language = language
        self.currency = currency

    def get_product_suggestions(self, term, max_suggestions=5, max_products=5):
        url = f"{self.base_url}/products/suggestions"
        params = {
            "term": term,
            "maxSuggestions": max_suggestions,
            "maxProducts": max_products,
            "storeCode": self.store_code,
            "lang": self.language,
            "curr": self.currency
        }
        response = requests.get(url, params=params)
        return json.loads(response.text)

    def get_stores(self, latitude, longitude):
        url = f"{self.base_url}/stores"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "lang": self.language,
            "curr": self.currency
        }
        response = requests.get(url, params=params)
        return response.json()


# Usage
# api = PickNPayAPI(
# "https://www.pnp.co.za/pnphybris/v2/pnp-spa", "WC44", "en", "ZAR")
# suggestions = api.get_product_suggestions("milk")
# print(suggestions)
