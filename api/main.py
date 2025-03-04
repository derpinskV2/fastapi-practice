from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def hello():
    return "Hello World"

if __name__ == "__main__":
    import uvicorn

    uvicorn_configuration = {
        "host": "0.0.0.0",
        "port": 8000,
        "loop": "uvloop",
        "http": "auto",
        "ws": "websockets",
        "ws_max_size": 4 * 1024 * 1024,
        "ws_max_queue": 32,
        "ws_ping_interval": 20.0,
        "ws_ping_timeout": 20.0,
        "ws_per_message_deflate": True,
        "timeout_graceful_shutdown": 30,
        "lifespan": "auto",
        "timeout_keep_alive": 10,
        "interface": "asgi3",
        "reload": True,
        "reload_delay": 0.25,
        "workers": 1,
        "proxy_headers": True,
        "server_header": True,
        "date_header": True,
        "forwarded_allow_ips": ["*"],
        # "log_config": logging_config,
    }

    uvicorn.run(
        app="main:app",
        **uvicorn_configuration,
        reload_includes=["*.py, *.html"],
    )






