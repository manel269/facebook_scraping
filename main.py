from fastapi iport FastAPI
from  scraper import scrape
#Enter your facebook's email id and password here 
	email = ""
	password = ""
	login(email,password)

	        

app = FastAPI()
@app.get("/{list}")
async def read_item():
  	scrape()
	driver.close()
if __name__ == "__main__":
    uvicorn.run(app='main:app')
