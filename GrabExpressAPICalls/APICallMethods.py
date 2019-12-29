import requests

from model.DeliveryPost import DeliveryPost
from model.DeliveryPostQuotes import DeliveryPostQuotes
from model.Error import Error
from model.GetDelivery import GetDelivery
from model.Quotes import Quotes


class APICallMethods:
    def __init__(self):
        # Holds the API URL
        self.apiUrl = "https://partner-api.grab.com/grab-express/v1/grab-express/v1/deliveries"

    # Post Method: Request for delivery service
    def delivery(self, delivery1):
        r = requests.post(url=self.apiUrl, data=DeliveryPost.to_json(delivery1))
        results = None
        # if responseCode is OK return GetDelivery object from the response
        if r.status_code == 200:
            results = GetDelivery.from_json(r.json())
        # if responseCode is HTTP_BAD_REQUEST, HTTP_NOT_FOUND or HTTP_CONFLICT
        # get the message from the response and print to the console
        elif r.status_code == 400 or r.status_code == 404 or r.status_code == 409:
            print(Error.from_json(r.content).message)
        else:
            print("ERROR: Connection refused")
        return results

    # Post Method: Request for delivery service quotes
    def deliveryQuotes(self, delivery1):
        r = requests.post(url=self.apiUrl + "/quotes", data=DeliveryPostQuotes.to_json(delivery1))
        results = None
        # if responseCode is OK return Quotes object from the response
        if r.status_code == 200:
            results = Quotes.from_json(r.json())
        # if responseCode is HTTP_BAD_REQUEST, HTTP_NOT_FOUND or HTTP_CONFLICT
        # get the message from the response and print to the console
        elif r.status_code == 400 or r.status_code == 404 or r.status_code == 409:
            print(Error.from_json(r.content).message)
        else:
            print("ERROR: Connection refused")
        return results

    # Get Method: Get the full information of a delivery
    def getDelivery(self, id1):
        r = requests.get(self.apiUrl + "/" + id1)
        results = None
        # if responseCode is OK return GetDelivery object from the response
        if r.status_code == 200:
            results = GetDelivery.from_json(r.json())
        # if responseCode is HTTP_BAD_REQUEST or HTTP_NOT_FOUND
        # get the message from the response and print to the console
        elif r.status_code == 400 or r.status_code == 404:
            print(Error.from_json(r.content).message)
        else:
            print("ERROR: Connection refused")
        return results

    # Delete Method: Cancel a delivery
    def deleteDelivery(self, id1):
        r = requests.delete(self.apiUrl + "/" + id1)
        results = None
        # if responseCode is OK print Delivery deleted to the console
        if r.status_code == 200:
            print("Delivery deleted")
        # if responseCode is HTTP_BAD_REQUEST, HTTP_NOT_FOUND or HTTP_CONFLICT
        # get the message from the response and print to the console
        elif r.status_code == 400 or r.status_code == 404 or r.status_code == 409:
            print(Error.from_json(r.content).message)
        else:
            print("ERROR: Connection refused")
        return results