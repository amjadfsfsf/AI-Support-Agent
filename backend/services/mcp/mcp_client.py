from fastmcp import Client

client = Client("mcp/servers/support/server.py") 
import asyncio
async def call_tool(tool_name: str, **kwargs):

    async with client:

        result = await client.call_tool(
            tool_name,
            kwargs
        )

        return result