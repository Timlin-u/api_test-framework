# configs/setting.py

FILE_PATH = {
    'ini': 'configs/config.ini',
    'extract': 'data/extract.yaml'  # 如果你有数据提取需求，可用这个文件保存提取结果
}

# 钉钉配置（如不使用，可忽略）
is_dd_msg = False
secret = "your_dingtalk_secret_here"
webhook = "https://oapi.dingtalk.com/robot/send?access_token=your_token_here"
