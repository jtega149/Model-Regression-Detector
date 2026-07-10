from .llm_client import client
from .config import PromptConfig, ClassificationOutput
import sys
import yaml
from datetime import datetime
from openai.types.responses import ResponseInputParam
from typing import cast

def classify_email(email: str, config: PromptConfig) -> ClassificationOutput:

    # Adding system prompt, few shot examples, and finally actual email to input for llm
    inputs = [{"role": "system", "content": config.system_prompt}]
    inputs.extend(config.few_shot_examples)
    inputs.append({"role": "user", "content": email})

    response = client.responses.parse(
        model="gpt-5.5",
        input=cast(ResponseInputParam, inputs),
        text_format=ClassificationOutput
    )

    if not response.output_parsed:
        sys.exit(1)

    yaml_file = {
        'version': config.version,
        'timestamp': datetime.now().isoformat(),
        'system_prompt': config.system_prompt,
        'few_shot_examples': config.few_shot_examples
    }

    return response.output_parsed