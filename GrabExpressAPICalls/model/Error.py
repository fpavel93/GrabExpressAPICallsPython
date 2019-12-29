import json


class Error:
    def __init__(self, message):
        self.message = message

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)