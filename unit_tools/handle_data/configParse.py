import os
import configparser


import os

class ConfigParse:
    def __init__(self, file_path=None):
        print("📂 pytest 当前工作目录:", os.getcwd())  # 输出当前工作目录
        if file_path is None:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "configs", "config.ini"))
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.read_config()


    def read_config(self):
        print("读取配置文件路径:", self.file_path)
        if not os.path.exists(self.file_path):
            print("❌ 配置文件不存在！请检查路径:", self.file_path)
            return

        with open(self.file_path, "r", encoding="utf-8") as f:
            content = f.read()
            print("📄 读取的配置文件内容：\n", content)  # 输出文件内容

        self.config.read(self.file_path, encoding="utf-8")
        print("读取到的配置段落:", self.config.sections())

    def get_value(self, section, option):
        return self.config.get(section, option)

    def get_host(self):
        return self.get_value("Host", "url")
