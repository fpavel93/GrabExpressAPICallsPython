import json


class DeliveryPost:
    def __init__(self, merchantOrderID, serviceType, paymentMethod, packages, sender,
                 recipient, origin, destination, cashOnDelivery, schedule, highValue):
        self.merchantOrderID = merchantOrderID
        self.serviceType = serviceType
        self.paymentMethod = paymentMethod
        self.packages = packages
        self.sender = sender
        self.recipient = recipient
        self.origin = origin
        self.destination = destination
        self.cashOnDelivery = cashOnDelivery
        self.schedule = schedule
        self.highValue = highValue

    def to_json(self):
        return json.dumps(self.__dict__)