from fastapi import APIRouter, Depends

from src.api.dependencies.api_key import verify_api_key
from src.services.stock_service import StockService

router = APIRouter(prefix="/stocks", tags=["stocks"])


@router.get("/{symbol}")
def get_stock_price(symbol: str, _: bool = Depends(verify_api_key)):
    """Get stock price from Finnhub"""
    return StockService.get_stock_data(symbol)
