from typing import Literal
from pydantic import BaseModel, Field


Category = Literal["billing", "technical", "account", "general"]


class ClassificationOutput(BaseModel):
    category: Category
    summary: str


class FewShotExample(BaseModel):
    input: str
    output: ClassificationOutput


class PromptConfig(BaseModel):
    version_id: str
    created_at: str
    model: str
    system_prompt: str
    few_shot_examples: list[FewShotExample] = Field(default_factory=list)
