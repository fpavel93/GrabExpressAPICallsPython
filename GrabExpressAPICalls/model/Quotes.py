import json


class Quotes:
    def __init__(self, quotes, packages, origin, destination):
        self.quotes = quotes
        self.packages = packages
        self.origin = origin
        self.destination = destination

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)