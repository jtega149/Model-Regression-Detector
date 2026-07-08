from pydantic import BaseModel
from typing import Literal

class PromptConfig(BaseModel):
    version: str
    email_text: str

    

class ClassificationOutput(BaseModel):
    category: Literal["Billing", "Technical", "Account", "General"]
    summary: str