from .config import PromptConfig, ClassificationOutput


def build_messages(email: str, config: PromptConfig) -> list[dict[str, str]]:
    messages = [
        {
            "role": "system",
            "content": config.system_prompt,
        }
    ]

    for example in config.few_shot_examples:
        messages.append(
            {
                "role": "user",
                "content": example.input,
            }
        )
        messages.append(
            {
                "role": "assistant",
                "content": example.output.model_dump_json(),
            }
        )

    messages.append(
        {
            "role": "user",
            "content": email,
        }
    )

    return messages


def classify_email(
    email: str,
    config: PromptConfig,
    llm_client=None,
) -> ClassificationOutput:
    if llm_client is None:
        from .llm_client import client as llm_client

    response = llm_client.responses.parse(
        model=config.model,
        input=build_messages(email, config),
        text_format=ClassificationOutput,
    )

    if not response.output_parsed:
        raise ValueError("Model did not return valid classification output.")

    return response.output_parsed
