from pydantic import BaseModel

class GetRamResponseSchema(BaseModel):
    id: int
    total: int
    available: int
    used: int
    percent: float