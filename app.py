
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from providers.picknpay import PickNPayAPI

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="pages")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/search/product/picknpay")
async def search_product_picknpay(term: str = 'Milk', max_suggestions: int = 5, max_products: int = 5, store_code: str = "WC44", language: str = "en", currency: str = "ZAR"):
    api = PickNPayAPI(
        "https://www.pnp.co.za/pnphybris/v2/pnp-spa", store_code, language, currency)

    suggestions = api.get_product_suggestions(
        term, max_suggestions, max_products)
    return suggestions


@app.get('/get/stores/picknpay')
async def get_stores_picknpay(latitude: float = -33.92584, longitude: float = 18.42322, store_code: str = "WC44", language: str = "en", currency: str = "ZAR"):
    api = PickNPayAPI(
        "https://www.pnp.co.za/pnphybris/v2/pnp-spa", store_code, language, currency)

    stores = api.get_stores(latitude, longitude)
    return stores
