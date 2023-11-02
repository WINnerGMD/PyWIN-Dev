from fastapi import FastAPI
import os
import sys







app = FastAPI()
base_path = "/Users/409/Desktop/Projects/PyWIN Dev/servers/"
for i in os.listdir("servers"):
    sys.path.append(os.path.abspath(base_path + i))
    exec(f"import servers.{i}.core as core")

    # core.app bug because wrapper use execute
    app.mount(f"/database/{i}",core.app)




@app.get('/')
async def welcome():
    return "Hello, Hosting is started🔥"
