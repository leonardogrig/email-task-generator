import json
from typing import Any, Dict, List

from openai import OpenAI
from prompts import EMAIL_ANALYSIS_TOOL, SYSTEM_MESSAGE, USER_MESSAGE_TEMPLATE


def analyze_emails(
    emails: List[Dict[str, str]], client: OpenAI
) -> List[Dict[str, Any]]:
    analyzed_emails = []

    for email in emails:
        completion = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": SYSTEM_MESSAGE},
                {
                    "role": "user",
                    "content": USER_MESSAGE_TEMPLATE.format(
                        subject=email["subject"],
                        from_=email["from"],
                        date=email["date"],
                        snippet=email["snippet"],
                        body=email["body"],
                    ),
                },
            ],
            tools=[EMAIL_ANALYSIS_TOOL],
            tool_choice={"type": "function", "function": {"name": "analyze_email"}},
        )

        analysis = json.loads(
            completion.choices[0].message.tool_calls[0].function.arguments
        )

        analyzed_email = {"original_email": email, "ai_analysis": analysis}
        analyzed_emails.append(analyzed_email)

    return analyzed_emails
