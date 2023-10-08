import asyncio
import aiohttp
import sys

# Replace with your Alphavantage API key
API_KEY = "YOUR_ALPHAVANTAGE_API_KEY"

async def fetch_exchange_rate(session, source_currency, target_currency):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source_currency}&to_currency={target_currency}&apikey={API_KEY}"

    try:
        async with session.get(url) as response:
            data = await response.json()
            exchange_rate = data.get("Realtime Currency Exchange Rate", {}).get("5. Exchange Rate")
            if exchange_rate:
                return f"{source_currency} to {target_currency}: {exchange_rate}"
            else:
                return f"Failed to fetch {source_currency} to {target_currency} rate"
    except aiohttp.ClientError as e:
        return f"Error while fetching {source_currency} to {target_currency} rate: {e}"

async def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <source_currency1> <source_currency2> --target <target_currency>")
        return

    source_currencies = sys.argv[1:-2]
    target_currency = sys.argv[-1]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_exchange_rate(session, source_currency, target_currency) for source_currency in source_currencies]
        exchange_rates = await asyncio.gather(*tasks)

    for rate in exchange_rates:
        print(rate)

if __name__ == "__main__":
    asyncio.run(main())
