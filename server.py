from mcp.server.fastmcp import FastMCP

# mcp = FastMCP("server") # ,port=8000, host="0.0.0.0"
mcp = FastMCP("server", port=8000, host="0.0.0.0")
# mcp = FastMCP("server", port=80, host="0.0.0.0")
# mcp = FastMCP("server", port=8043, host="0.0.0.0")



@mcp.tool()
def find_in_hanna(name: str) -> str:
    "Query GLN data in Hanna"
    return f"Your entrance: [{name}]"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")



