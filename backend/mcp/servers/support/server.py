from fastmcp import FastMCP


from order_tool import get_order

from ticket_tool import (
    create_ticket,
    get_ticket,
    close_ticket,
    reopen_ticket,
    list_tickets
)

from calculator_tool import add, subtract, multiply, divide
mcp = FastMCP("AI Support Agent")


@mcp.tool()
def create_support_ticket(name: str, email: str, issue: str):

    return create_ticket(name, email, issue)


@mcp.tool()
def close_support_ticket(ticket_id: int):

    return close_ticket(ticket_id)


@mcp.tool()
def reopen_support_ticket(ticket_id: int):

    return reopen_ticket(ticket_id)


@mcp.tool()
def get_all_tickets():

    return list_tickets()

@mcp.tool()
def get_support_ticket(ticket_id: int):

    return get_ticket(ticket_id)


@mcp.tool()
def get_order_status(order_id: int):

    return get_order(order_id)


@mcp.tool()
def calculator(operation: str, a: float, b: float):

    if operation in ("add", "+"):
        return add(a, b)

    if operation in ("subtract", "-"):
        return subtract(a, b)

    if operation in ("multiply", "*"):
        return multiply(a, b)

    if operation in ("divide", "/"):
        return divide(a, b)

    return "Invalid operation."


if __name__ == "__main__":
    mcp.run()