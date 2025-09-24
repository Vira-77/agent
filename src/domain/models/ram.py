from pydantic import BaseModel


# CPU data model

class Ram(BaseModel):
    """
    Pydantic data model for representing RAM information.

    Attributes:
        id (int): The ID of the RAM data (e.g., 0 for system RAM).
        total (int): Total RAM in bytes.
        available (int): Available RAM in bytes.
        used (int): Used RAM in bytes.
        percent (float): RAM usage percentage.
    """
    id: int
    total: int
    available: int
    used: int
    percent: float