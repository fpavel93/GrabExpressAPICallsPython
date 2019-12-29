import json


class GetDelivery:
    def __init__(self, deliveryID, merchantOrderID, quote, sender, recipient,
    cashOnDelivery, schedule, status, courier, timeline, trackingURL, advanceInfo):
        self.deliveryID = deliveryID
        self.merchantOrderID = merchantOrderID
        self.quote = quote
        self.sender = sender
        self.recipient = recipient
        self.cashOnDelivery = cashOnDelivery
        self.schedule = schedule
        self.status = status
        self.courier = courier
        self.timeline = timeline
        self.trackingURL = trackingURL
        self.advanceInfo = advanceInfo

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)