from typing import Literal

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Literal["pending", "doing", "done"] = "pending"

