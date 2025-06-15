step 1: install uv
  ‵ pip install uv ‵

step 2: initialize uv
  ‵ uv init ‵

step 3: add a virtual environment
   ‵ uv venv python --3.12 ‵ #or 3.13

step 4: add all the neccessary modules
    ‵ uv add -r requirments.txt ‵

step 5: Run the myserver.py and weatherserver.py in the cmd
    ‵ python myserver.py ‵  # it's a 'stdio' tcp so no response is show but your server is running locall
    ‵ python weatherserver.py ‵ # it's 'Streamable-http' tcp , you will  get the url for local run

step 6: run the myClient.py in the cmd
    ‵ python myClient.py ‵

mcpConfig.py file contains all the mcp server connections

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
