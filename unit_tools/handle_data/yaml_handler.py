import os
import yaml
from configs.setting import FILE_PATH
from unit_tools.log_util.recordlog import logs

def read_yaml(yaml_path):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    file_path = os.path.join(base_path, "data", yaml_path)
    print("尝试读取 YAML 文件:", file_path)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        if not isinstance(data, list):
            data = [data]
        return data
    except Exception as e:
        logs.error(f"读取 YAML 文件 {file_path} 失败: {e}")
        return None
