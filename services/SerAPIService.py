import os
import requests

from serpapi import GoogleSearch


class SerpAPIService:
  def get_google_data(self, question: str) -> str:
    key = os.getenv("APIKEY-SERPAPI")
    params = {
      "enginge": "google",
      "q": question,
      "location": "Warsaw",
      "api_key": key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    url = results["organic_results"][0]["link"]
    return url