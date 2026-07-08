from .llm_client import client
from .config import PromptConfig, ClassificationOutput
import sys

def classify_email(email: str, config: PromptConfig | None = None) -> ClassificationOutput:
    prompt = """
    You are a customer support email classifier. You will be given an email by the user that you must classify. Your task is to return a simple classification of the email, the classification can be of the following categories: "Billing", "Technical", "Account", or "General", and as well returning a 2-5 sentence summary of the email.
    """

    response = client.responses.parse(
        model="gpt-5.5",
        input=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": email}
        ],
        text_format=ClassificationOutput
    )

    if not response.output_parsed:
        sys.exit(1)

    return response.output_parsed