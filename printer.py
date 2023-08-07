from pydantic import BaseModel

class Printer(BaseModel):
    id: int
    brand: str
    type: str
    price: int
    