from services.mcp.mcp_client import call_tool


async def execute_tool(plan):

    tool = plan["tool"]
    args = plan.get("arguments", {})

    result = await call_tool(tool, **args)

    return result.content[0].text