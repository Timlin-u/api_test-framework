import pytest
import shutil
import os

if __name__ == '__main__':
    pytest.main(['--alluredir=./report/temp'])
    if os.path.exists('./environment.xml'):
        shutil.copy('./environment.xml', './report/temp')
    os.system('allure serve ./report/temp')
