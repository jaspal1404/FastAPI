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

    auth_token = "eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwOWNjYTdlMS04NTYzLTRjNWItODM4Ni1lZTMyNWZmOGI0ZmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MDIwNzc4NjYsImlhdCI6MTcwMTk5MTQ2NiwianRpIjoiVEdULjUyZWRkZDYyYWYzZjQ0NjA5ODk3YmViNzRkY2JlNGY4LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsInNjbyI6ImVjb20ubm9uZSxvcGVuaWQiLCJjbGkiOiJlY29tLWlvcy0xLjAuMCIsImFzbCI6IkwifQ.D3X66v7zPDA1KS5brDcHkUT-LE5tro7DYbLFG7P6PgPMaHJf2IJlLUo9c8cJoS0XMTm_rFOwyD6R3GmQ8-7AUCE53f-0GNyFnatqIidCfKOgBpe87zv8hSKAhSfXda8aClUh86DSiYTsvhIJKL3HikWMbZ17XV9e43rJn_XHTUq5UGqf2OxPF8vm5eRP3jGiRrySofxM2NPdW1ovGGxpWtKW7YfDt3HMBa_lCf1GOoYK3fDVontmd7xuImIBflCSeGzvcUW59gfVldPkyVss5aYcCNafFQ5fZOv5of0v82LSZctoTd6oaEGr60FM-QtsixHEOpp-3pVIlBLb9qhESg"
    headers = {'Authorization': f'Bearer {auth_token}'}
    data = {"cart_item": {"tcin": item_id, "quantity": quantity},
            "fulfillment": {"ship_method": delivery_method, "type": "PICKUP", "location_id": "2101"},
            "cart_type": "REGULAR", "channel_id": "91"}

    url = 'https://carts.target.com/web_checkouts/v1/cart_items?iOSAppVersion=2023.49.0&key=3d4d4435710335df6435c68e19a7cf67c635a01d'
    response = requests.post(url, json=data, headers=headers)

    return response.status_code