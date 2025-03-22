# 接口自动化测试框架

## 项目背景
为电商平台核心接口设计的自动化测试框架，替代手工回归测试，提升效率和准确性。

## 技术栈
- Python 3.8 + Pytest
- Requests + YAML 数据驱动
- Allure 测试报告（待集成）

## 快速运行
```bash
# 安装依赖
pip install -r requirements.txt

# 执行测试并生成报告
pytest --alluredir=./reports
allure serve ./reports
