from fastapi iport FastAPI
from  scraper import scrape

app = FastAPI()
@app.get("/{list}")
async def read_item():
  return
