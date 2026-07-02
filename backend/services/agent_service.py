import asyncio

from services.agent.planner_service import plan
from services.agent.tool_router import execute_tool
from services.rag.rag_service import ask_rag
from services.session_service import get_session, clear_session
from services.agent.response_service import generate_response
from services.agent.argument_extractor import extract_arguments
from services.agent.argument_service import collect_arguments


def ask_agent(session_id: str, question: str):

    session = get_session(session_id)

    # =========================================================
    # Continue existing tool conversation
    # =========================================================

    if session["current_tool"]:

        updated = extract_arguments(
            session["arguments"],
            question
        )

        session["arguments"].update(updated)

        check = collect_arguments(
            session["current_tool"],
            session["arguments"]
        )

        print(check)

        if check["status"] == "missing":

            return {
                "type": "conversation",
                "answer": check["message"]
            }

        tool_result = asyncio.run(
            execute_tool(
                {
                    "tool": session["current_tool"],
                    "arguments": session["arguments"]
                }
            )
        )

        answer = generate_response(
            question,
            tool_result
        )

        clear_session(session_id)

        return {
            "type": "conversation",
            "answer": answer
        }

    # =========================================================
    # Planner
    # =========================================================

    planner = plan(question)

    print(planner)


     # =========================================================
    # RAG
    # =========================================================

    if planner["action"] == "answer":

        rag = ask_rag(question)

        answer = generate_response(
            question,
            rag["answer"]
        )

        return {
            "type": "rag",
            "answer": {
                "answer": answer,
                "sources": rag["sources"]
            }
        }

    # =========================================================
    # New Tool Conversation
    # =========================================================

    session["current_tool"] = planner["tool"]

    session["arguments"] = planner.get("arguments", {})

    check = collect_arguments(
        session["current_tool"],
        session["arguments"]
    )

    print(check)

    if check["status"] == "missing":

        return {
            "type": "conversation",
            "answer": check["message"]
        }
    


        # =========================================================
    # Execute Tool
    # =========================================================

    tool_result = asyncio.run(
        execute_tool(
            {
                "tool": session["current_tool"],
                "arguments": session["arguments"]
            }
        )
    )

    # =========================================================
    # Generate Natural Response
    # =========================================================

    answer = generate_response(
        question,
        tool_result
    )

    # =========================================================
    # Clear Session
    # =========================================================

    clear_session(session_id)

    return {
        "type": "conversation",
        "answer": answer
    }