from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Items
from typing import Annotated
from database import SessionLocal

import requests

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ItemRequest(BaseModel):
    name: str
    description: str
    brand: str
    category: str
    price: float
    quantity: int
    driveup_allowed: bool
    shipping_allowed: bool
    store_pickup_allowed: bool
    store_id: int


db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/", status_code=status.HTTP_200_OK)
async def search(item_name: str, delivery_mrthod: str, quantity: int):

    response = requests.get("https://redsky.target.com/redsky_aggregations/v1/apps/unified_search_v2?app_version=2023.49.0&channel=APPS&count=20&default_purchasability_filter=true&include_sponsored=true&key=3f015bca9bce7dbb2b377638fa5de0f229713c78&keyword=bread&new_search=true&offset=0&os_family=iOS&page=/s/bread&pricing_context=digital&pricing_store_id=664&spellcheck=true&store_id=664&store_ids=664%2C664%2C2223%2C100%2C3%2C693&visitor_id=018c36577ef501041A1083BD1D3945F7")
    #response = requests.get("https://carts.target.com/web_checkouts/v1/cart_views?cart_type=REGULAR&field_groups=ADDRESSES,CART,CART_ITEMS,FINANCE_PROVIDERS,PROMOTION_CODES,SUMMARY&iOSAppVersion=2023.49.0&key=3d4d4435710335df6435c68e19a7cf67c635a01d")
    return {"status_code": response.status_code, "data": response.content}


@router.get("/get-item/", status_code=status.HTTP_200_OK)
async def get_item_by_name(db: db_dependency, item_name: str, delivery_method: str, quantity: int):

    item = db.query(Items).filter(Items.name == item_name).first()
    if item is None:
        return {"response": False, "reason": "Item not found! Would you like to try another item ?"}
    else:
        if item.quantity >= quantity:
            if "item."+delivery_method+"_allowed":
                return {"response": True, "reason": "Item available"}
            else:
                return {"response": False, "reason": "Item not available for " + delivery_method + ". Would you like to try a different delivery method ?"}
        else:
            if "item." + delivery_method + "_allowed":
                return {"response": False, "reason": "Only " + quantity + " units of the item available. Would you like to proceed ?"}
            else:
                return {"response": False, "reason": "Only " + quantity + " units of the item available. Would you like to proceed ?"}


@router.get("/add-to-cart/", status_code=status.HTTP_200_OK)
async def add_to_cart(item_id: str, delivery_method: str, quantity: int):
    auth_token = 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI0MDAwYTY1OS1iM2Y1LTQ4YjItOWYwMi0zZGYzNjkwMmU2NWUiLCJpc3MiOiJNSTYiLCJleHAiOjE3MDIwNzA0MDQsImlhdCI6MTcwMTk4NDAwNCwianRpIjoiVEdULjUwMmZiZDNhMzFjOTRkNTZiMjQ1ZjIzOTk5YmM0M2E4LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjAwQTg2MkFGLTAwQkUtNDgwNC1BNDk4LUE2NEQ5MTlFNjMwMyIsInNjbyI6ImVjb20ubm9uZSxvcGVuaWQiLCJjbGkiOiJlY29tLWlvcy0xLjAuMCIsImFzbCI6IkwifQ.dU0CLJJRm4SRIwFD_yNdJwqEPf03B0YmoyNz4QvKqsn_Fpj4YY8HUSRDHDvBZ43jC8plvKnNmVwoycsrJHZPCC5H1sW4GAGSOxicYWX5NvjV0uI_oboohHybNxXW6XwZ76lFVVrWfzxQPb6FZFpAic88-TxCN22v6XzBk8C2jmV1jSNJP-2SZI55OJOXIIe4wc4198sl-bo6eQe46pxrYWy1bTsabABguiHSxTTabSOZWxgac13KLHZSRJwSJAFDG8Fps-USh3fIGtvnRi4iJoIsdCabdqIN_XcEgPq818bIrc9Rjgq9XtjfFJo6vyaVgnaCgh7_ZNBoHatj2DIe7g'

    if delivery_method == "driveup":
        delivery_method = "CURBSIDE"
    elif (delivery_method == "store pickup" or delivery_method == "pickup"):
        delivery_method = "STORE_PICKUP"
    else:
        delivery_method = delivery_method

    headers = {'Authorization': f'Bearer {auth_token}'}
    data = {"cart_item": {"tcin": item_id, "quantity": quantity},
            "fulfillment": {"ship_method": delivery_method, "type": "PICKUP", "location_id": "664"},
            "cart_type": "REGULAR", "channel_id": "91"}

    url = 'https://carts.target.com/web_checkouts/v1/cart_items?iOSAppVersion=2023.49.0&key=3d4d4435710335df6435c68e19a7cf67c635a01d'
    response = requests.post(url, json=data, headers=headers)

    return response.status_code


@router.post("/add-item", status_code=status.HTTP_201_CREATED)
async def add_item(db: db_dependency, item: ItemRequest):

    item_model = db.query(Items).filter(Items.name == item.name).first()
    if item_model is None:
        item_model = Items(**item.dict())
        db.add(item_model)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Item already exists")
