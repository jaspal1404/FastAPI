from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
import requests


class Items(Base):
    __tablename__ = 'items'

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    brand = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    delivery_method = Column(String)
    store_id = Column(String)


def access_cart(item_id: str, delivery_method: str, quantity: int):

    auth_token = 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI0MDAwYTY1OS1iM2Y1LTQ4YjItOWYwMi0zZGYzNjkwMmU2NWUiLCJpc3MiOiJNSTYiLCJleHAiOjE3MDIwNzA0MDQsImlhdCI6MTcwMTk4NDAwNCwianRpIjoiVEdULjUwMmZiZDNhMzFjOTRkNTZiMjQ1ZjIzOTk5YmM0M2E4LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjAwQTg2MkFGLTAwQkUtNDgwNC1BNDk4LUE2NEQ5MTlFNjMwMyIsInNjbyI6ImVjb20ubm9uZSxvcGVuaWQiLCJjbGkiOiJlY29tLWlvcy0xLjAuMCIsImFzbCI6IkwifQ.dU0CLJJRm4SRIwFD_yNdJwqEPf03B0YmoyNz4QvKqsn_Fpj4YY8HUSRDHDvBZ43jC8plvKnNmVwoycsrJHZPCC5H1sW4GAGSOxicYWX5NvjV0uI_oboohHybNxXW6XwZ76lFVVrWfzxQPb6FZFpAic88-TxCN22v6XzBk8C2jmV1jSNJP-2SZI55OJOXIIe4wc4198sl-bo6eQe46pxrYWy1bTsabABguiHSxTTabSOZWxgac13KLHZSRJwSJAFDG8Fps-USh3fIGtvnRi4iJoIsdCabdqIN_XcEgPq818bIrc9Rjgq9XtjfFJo6vyaVgnaCgh7_ZNBoHatj2DIe7g'
    headers = {'Authorization': f'Bearer {auth_token}'}
    data = {"cart_item": {"tcin": item_id, "quantity": quantity},
            "fulfillment": {"ship_method": delivery_method, "type": "PICKUP", "location_id": "664"},
            "cart_type": "REGULAR", "channel_id": "91"}

    url = 'https://carts.target.com/web_checkouts/v1/cart_items?iOSAppVersion=2023.49.0&key=3d4d4435710335df6435c68e19a7cf67c635a01d'
    response = requests.post(url, json=data, headers=headers)

    return response.status_code