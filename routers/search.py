from fastapi import APIRouter
from starlette import status
import requests

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def search():

    response = requests.get("https://redsky.target.com/redsky_aggregations/v1/apps/unified_search_v2?app_version=2023.49.0&channel=APPS&count=20&default_purchasability_filter=true&include_sponsored=true&keyword=bread&new_search=true&offset=0&os_family=iOS&page=/s/bread&pricing_context=digital&pricing_store_id=2766&spellcheck=true&store_id=2766&store_ids=2766%2C2766%2C2768%2C3264%2C2829%2C2767&visitor_id=018c36577ef501041A1083BD1D3945F7&key=1fc2d885b6a28c87af93e5818e382bef4ecda4dc")
    return response.status_code