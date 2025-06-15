connections = {
            "math": {
                "command": "python",
                "args": ["D:\\Projects\\MCP_Folder\\mcpserver-files\\myservers.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        }