from fastapi import APIRouter
from starlette import status
import requests

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def search():

    response = requests.get("https://redsky.target.com/redsky_aggregations/v1/apps/unified_search_v2?app_version=2023.49.0&channel=APPS&count=20&default_purchasability_filter=true&include_sponsored=true&key=3f015bca9bce7dbb2b377638fa5de0f229713c78&keyword=bread&new_search=true&offset=0&os_family=iOS&page=/s/bread&pricing_context=digital&pricing_store_id=664&spellcheck=true&store_id=664&store_ids=664%2C664%2C2223%2C100%2C3%2C693&visitor_id=018c36577ef501041A1083BD1D3945F7")
    #response = requests.get("https://carts.target.com/web_checkouts/v1/cart_views?cart_type=REGULAR&field_groups=ADDRESSES,CART,CART_ITEMS,FINANCE_PROVIDERS,PROMOTION_CODES,SUMMARY&iOSAppVersion=2023.49.0&key=3d4d4435710335df6435c68e19a7cf67c635a01d")
    return {"status_code": response.status_code, "data": response.content}