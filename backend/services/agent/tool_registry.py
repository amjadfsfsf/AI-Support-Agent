TOOLS = {
    "calculator": {
        "name": "calculator",
        "description": "Perform mathematical calculations.",

        "required": [
            "operation",
            "a",
            "b"
        ],

        "arguments": {
            "operation": "",
            "a": "",
            "b": ""
        },

        "examples": [
            "Calculate 5 + 10",
            "What is 20 / 4?"
        ]
    },

    "create_support_ticket": {
        "name": "create_support_ticket",
        "description": "Create a customer support ticket.",

        "required": [
            "name",
            "email",
            "issue"
        ],

        "arguments": {
            "name": "",
            "email": "",
            "issue": ""
        },

        "examples": [
            "Create a support ticket",
            "I can't login",
            "Report a bug"
        ]
    },

    "get_order_status": {
        "name": "get_order_status",
        "description": "Retrieve the status of a customer order.",

        "required": [
            "order_id"
        ],

        "arguments": {
            "order_id": ""
        },

        "examples": [
            "Where is my order?",
            "Track order 12345"
        ]
    }
}