import pytest
import yaml
import os

# 读取 YAML 配置文件
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "configs/config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

config = load_config()

@pytest.fixture(scope="session")
def base_url():
    return config["env"]["base_url"]
