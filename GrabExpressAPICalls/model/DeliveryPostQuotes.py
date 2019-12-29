import json


class DeliveryPostQuotes:
    def __init__(self, serviceType, packages, origin, destination):
        self.serviceType = serviceType
        self.packages = packages
        self.origin = origin
        self.destination = destination

    def to_json(self):
        return json.dumps(self.__dict__)