sessions = {}


def get_session(session_id: str):

    if session_id not in sessions:

        sessions[session_id] = {

            "current_tool": None,

            "arguments": {},

            "planner": None

        }

    return sessions[session_id]


def clear_session(session_id: str):

    sessions[session_id] = {

        "current_tool": None,

        "arguments": {},

        "planner": None

    }