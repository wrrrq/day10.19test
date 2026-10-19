from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

# 加载 .env 文件到环境变量中
load_dotenv()


class Settings(BaseModel):
    # 如果 .env 里没配 SECRET_KEY，Pydantic 会直接报错拒绝启动（Fail Fast）
    secret_key: str = Field(..., alias="SECRET_KEY")
    # 读取 THRESHOLD，默认值为 0.5，且强制要求是浮点数
    threshold: float = Field(0.5, alias="THRESHOLD")


def get_settings() -> Settings:
    # 将操作系统的环境变量直接注入模型
    return Settings(**os.environ)
