import asyncio
import aiohttp

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Failed to retrieve {url}: HTTP Status {response.status}")
                return None
    except aiohttp.ClientError as e:
        print(f"Error while fetching {url}: {e}")
        return None

async def scrape_and_save(url, output_file):
    async with aiohttp.ClientSession() as session:
        html = await fetch_url(session, url)
        if html:
            # You can save the data to a file or database here.
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Saved {url} to {output_file}")

async def main():
    urls = ["https://example.com", "https://example.org"]  # List of URLs to scrape
    output_dir = "output/"  # Directory to save scraped data

    tasks = []
    for url in urls:
        output_file = f"{output_dir}{url.split('//')[1].replace('/', '-')}.html"
        tasks.append(scrape_and_save(url, output_file))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
