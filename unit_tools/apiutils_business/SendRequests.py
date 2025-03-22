import requests
from unit_tools.log_util.recordlog import logs

class SendRequests:
    def send_request(self, url, method='GET', headers=None, data=None, cookies=None, files=None, **kwargs):
        try:
            # 防止重复传入 verify 参数
            if "verify" in kwargs:
                kwargs.pop("verify")
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                cookies=cookies,
                files=files,
                timeout=10,
                verify=False,  # 关闭证书验证
                **kwargs
            )
            logs.info(f"Response Status: {response.status_code}")
            return response
        except Exception as e:
            logs.error(f"请求异常：{e}")
            raise

    def execute_api_request(self, api_name, url, method, headers, case_name, cookies=None, files=None, **kwargs):
        logs.info(f"接口名称：{api_name}")
        logs.info(f"请求地址：{url}")
        logs.info(f"请求方式：{method.upper()}")
        logs.info(f"测试用例名称：{case_name}")
        logs.info(f"请求头：{headers}")
        logs.info(f"cookies：{cookies}")
        response = self.send_request(url, method, headers, **kwargs, cookies=cookies, files=files)
        return response
