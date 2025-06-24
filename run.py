import uvicorn


if __name__ == "__main__":
    host_ip = "0.0.0.0"
    host_port = 8000
    reload_on_code_change = True


    uvicorn.run("main:app", host=host_ip, port=host_port, reload=reload_on_code_change)

