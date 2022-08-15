from fastapi iport FastAPI
from  scraper import scrape
#Enter your facebook's email id and password here 
	email = ""
	password = ""
	login(email,password)
	scrape()
	driver.close()
	        

app = FastAPI()
@app.get("/{list}")
async def read_item():
  	scrape()
	  driver.close()
