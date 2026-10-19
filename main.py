from fastapi import FastAPI, Depends
from config import get_settings, Settings

app = FastAPI()


@app.get("/info")
def get_info(settings: Settings = Depends(get_settings)):
    # 注意：绝不可以在生产环境返回真实的 secret_key，这里只是为了演示读取成功
    return {
        "status": "ok",
        "message": "配置读取成功！",
        "threshold_value": settings.threshold,
        "key_length": len(settings.secret_key),
    }
