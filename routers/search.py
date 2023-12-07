from fastapi import APIRouter
from starlette import status
import requests

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def search():

    response = requests.get("https://redsky.target.com/redsky_aggregations/v1/apps/unified_search_v2?app_version=2023.49.0&channel=APPS&count=20&default_purchasability_filter=true&include_sponsored=true&key=3f015bca9bce7dbb2b377638fa5de0f229713c78&keyword=bread&new_search=true&offset=0&os_family=iOS&page=/s/bread&pricing_context=digital&pricing_store_id=664&spellcheck=true&store_id=664&store_ids=664%2C664%2C2223%2C100%2C3%2C693&visitor_id=018c36577ef501041A1083BD1D3945F7")
    #response = requests.get("https://carts.target.com/web_checkouts/v1/cart_views?cart_type=REGULAR&field_groups=ADDRESSES,CART,CART_ITEMS,FINANCE_PROVIDERS,PROMOTION_CODES,SUMMARY&iOSAppVersion=2023.49.0&key=3d4d4435710335df6435c68e19a7cf67c635a01d")
    return {"status_code": response.status_code, "data": response.content}



@router.get("/add-to-cart", status_code=status.HTTP_200_OK)
async def add_to_cart():
    auth_token = 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI0MDAwYTY1OS1iM2Y1LTQ4YjItOWYwMi0zZGYzNjkwMmU2NWUiLCJpc3MiOiJNSTYiLCJleHAiOjE3MDIwNzA0MDQsImlhdCI6MTcwMTk4NDAwNCwianRpIjoiVEdULjUwMmZiZDNhMzFjOTRkNTZiMjQ1ZjIzOTk5YmM0M2E4LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjAwQTg2MkFGLTAwQkUtNDgwNC1BNDk4LUE2NEQ5MTlFNjMwMyIsInNjbyI6ImVjb20ubm9uZSxvcGVuaWQiLCJjbGkiOiJlY29tLWlvcy0xLjAuMCIsImFzbCI6IkwifQ.dU0CLJJRm4SRIwFD_yNdJwqEPf03B0YmoyNz4QvKqsn_Fpj4YY8HUSRDHDvBZ43jC8plvKnNmVwoycsrJHZPCC5H1sW4GAGSOxicYWX5NvjV0uI_oboohHybNxXW6XwZ76lFVVrWfzxQPb6FZFpAic88-TxCN22v6XzBk8C2jmV1jSNJP-2SZI55OJOXIIe4wc4198sl-bo6eQe46pxrYWy1bTsabABguiHSxTTabSOZWxgac13KLHZSRJwSJAFDG8Fps-USh3fIGtvnRi4iJoIsdCabdqIN_XcEgPq818bIrc9Rjgq9XtjfFJo6vyaVgnaCgh7_ZNBoHatj2DIe7g'

    headers = {'Authorization': f'Bearer {auth_token}'}
    data = {"cart_item": {"tcin": "14772934", "quantity": 1},
            "fulfillment": {"ship_method": "STORE_PICKUP", "type": "PICKUP", "location_id": "664"},
            "cart_type": "REGULAR", "channel_id": "91"}

    url = 'https://carts.target.com/web_checkouts/v1/cart_items?iOSAppVersion=2023.49.0&key=3d4d4435710335df6435c68e19a7cf67c635a01d'
    response = requests.post(url, json=data, headers=headers)

    return response
