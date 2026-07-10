from src.classifier import classify_email

TEST_BILLING = """
Subject: Cancel subscription renewal

Hello,
I would like to cancel my subscription before the next billing cycle. Please confirm that I will not be charged again.

Best regards.
"""
TEST_ACCOUNT = """
Subject: Cannot reset my password

Hello,
I forgot my password and attempted to use the password reset link, but I never received the email. Could you help me regain access to my account?

Thank you.
"""
TEST_TECHNICAL = """
Subject: Unable to connect to the API endpoint

Hello Support Team,
I am trying to connect my application to your API, but I keep receiving a 500 internal server error whenever I send a request. I have verified my API key and checked my configuration, but the issue still persists. Could you help me troubleshoot this?
"""
TEST_GENERAL = """
Subject: Request for product information

Hi,
Could you provide more information about your service and how it works? I would like to understand how your platform can help my team manage our workflow.

Thank you.
"""


def run_tests():
    config = load_prompt_config("prompts/classifier_v1.yaml")

    print("Billing Test:", classify_email(TEST_BILLING, config))
    print("Account Test:", classify_email(TEST_ACCOUNT, config))
    print("Technical Test:", classify_email(TEST_TECHNICAL, config))
    print("General Test:", classify_email(TEST_GENERAL, config))


if __name__ == "__main__":
    run_tests()
