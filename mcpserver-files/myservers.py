from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)->int:
    """Returns multiplication of two numbers a and b"""
    return a + b

@mcp.tool()
def multiply(a:int, b:int)->int:
    """A function that multiplies two numbers a and b"""
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")
