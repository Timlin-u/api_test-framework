from unit_tools.log_util.recordlog import logs

class Assertions:
    @staticmethod
    def status_code_assert(expected, actual):
        if expected == actual:
            logs.info(f"状态码断言成功：{actual} == {expected}")
            return 0
        else:
            logs.error(f"状态码断言失败：{actual} != {expected}")
            return 1

    @staticmethod
    def contain_assert(expected, response_text):
        if expected in response_text:
            logs.info(f"包含断言成功：'{expected}' 存在于响应中")
            return 0
        else:
            logs.error(f"包含断言失败：'{expected}' 不存在于响应中")
            return 1

    @staticmethod
    def assert_result(expected_results, response, status_code):
        all_flag = 0
        for item in expected_results:
            for mode, expected in item.items():
                if mode == "code":
                    all_flag += Assertions.status_code_assert(expected, status_code)
                elif mode == "contain":
                    all_flag += Assertions.contain_assert(expected, response)
                else:
                    logs.error(f"不支持的断言模式: {mode}")
                    all_flag += 1
        assert all_flag == 0, "断言失败"
        logs.info("所有断言成功")
