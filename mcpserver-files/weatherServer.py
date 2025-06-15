from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def getWeather(location: str):
    """A function to show weather condition"""
    return "It's always cloudy in banglore"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")