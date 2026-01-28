import finnhub

from src.core.config import settings

finnhub_client = finnhub.Client(api_key=settings.finnhub_api_key)


class StockService:
    @staticmethod
    def get_stock_data(symbol: str):
        return finnhub_client.stock_candles(symbol, "D", 1590988249, 1591852249)

    pass
