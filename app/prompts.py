SYSTEM_MESSAGE = """You are an AI assistant that analyzes emails and provides structured information about them. The current date is August 20, 2024."""

USER_MESSAGE_TEMPLATE = """Analyze the following email:

Subject: {subject}
From: {from_}
Date: {date}
Snippet: {snippet}
Body: {body}"""

EMAIL_ANALYSIS_TOOL = {
    "type": "function",
    "function": {
        "name": "analyze_email",
        "description": "Analyze an email and provide structured information about it.",
        "parameters": {
            "type": "object",
            "properties": {
                "is_task": {
                    "type": "boolean",
                    "description": "Should this email become a task?",
                },
                "task_description": {
                    "type": "string",
                    "description": "A brief description of what should be done in the task",
                },
                "tags": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 3,
                    "maxItems": 3,
                    "description": "Tags that should be applied to this email",
                },
                "urgency": {
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 5,
                    "description": "How urgent is this email? (0-5)",
                },
                "estimated_task_time": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Estimated date and time to configure this task",
                },
            },
            "required": [
                "is_task",
                "task_description",
                "tags",
                "urgency",
                "estimated_task_time",
            ],
        },
    },
}
