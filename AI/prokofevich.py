from typing import List
import requests as req
import json

class Prokofevich() :
    def __init__(self) -> None:
        self.ai_url = "https://pelevin.gpt.dobro.ai/generate/"
        self.p_length = 30

    def get_text(self, beginning : str, number : int) -> List[str] :
        payload = {"prompt": beginning, "length": self.p_length}
        result = []

        for i in range((number + 2) // 3) :
            res = req.post(self.ai_url, json=payload)
            if res.status_code == 200 :
                result = result + json.loads(res.text)["replies"]
            else :
                raise Exception("Invalid request or server is down. Prokofevich")
        return result[:number]