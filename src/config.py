from pydantic import BaseModel
from typing import Literal
from .data.llm_constants import emails, system_prompt

class PromptConfig(BaseModel):
    version: str
    system_prompt: str = system_prompt
    few_shot_examples: list[dict] = emails


class ClassificationOutput(BaseModel):
    category: Literal["Billing", "Technical", "Account", "General"]
    summary: str