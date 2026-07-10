system_prompt = """You are a customer support email classifier. You will be given an email by the user that you must classify. Your task is to return a simple classification of the email, the classification can be of the following categories: "Billing", "Technical", "Account", or "General", and as well returning a 2-5 sentence summary of the email."""

emails = [
    {
        "role": "user",
        "content": "I am unable to reset my password and never received the recovery email."
    },
    {
        "role": "assistant",
        "content": "{\"category\": \"Account\", \"summary\": \"User cannot access their account because they did not receive the password reset email.\"}"
    },

    {
        "role": "user",
        "content": "The application crashes every time I upload a large file."
    },
    {
        "role": "assistant",
        "content": "{\"category\": \"Technical\", \"summary\": \"User is experiencing application crashes when uploading large files.\"}"
    },

    {
        "role": "user",
        "content": "Can you send me a copy of my invoice from last month?"
    },
    {
        "role": "assistant",
        "content": "{\"category\": \"Billing\", \"summary\": \"User is requesting a copy of a previous invoice for billing records.\"}"
    },

    {
        "role": "user",
        "content": "I would like to learn more about the features included in your platform."
    },
    {
        "role": "assistant",
        "content": "{\"category\": \"General\", \"summary\": \"User is requesting general information about available platform features.\"}"
    },

    {
        "role": "user",
        "content": "The API is returning a 500 error whenever I send a request."
    },
    {
        "role": "assistant",
        "content": "{\"category\": \"Technical\", \"summary\": \"User is encountering server errors when making API requests.\"}"
    },

    {
        "role": "user",
        "content": "I want to update the email address associated with my account."
    },
    {
        "role": "assistant",
        "content": "{\"category\": \"Account\", \"summary\": \"User wants to change their account email address.\"}"
    },

    {
        "role": "user",
        "content": "I was charged twice for my subscription this month."
    },
    {
        "role": "assistant",
        "content": "{\"category\": \"Billing\", \"summary\": \"User reports a duplicate charge on their subscription payment.\"}"
    },

    {
        "role": "user",
        "content": "Do you offer integrations with other software tools?"
    },
    {
        "role": "assistant",
        "content": "{\"category\": \"General\", \"summary\": \"User is asking whether the platform supports integrations with external tools.\"}"
    }
]