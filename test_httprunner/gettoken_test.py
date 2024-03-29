# NOTE: Generated By HttpRunner v3.1.6
# FROM: gettoken.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGettoken(HttpRunner):

    config = Config("获取token接口")

    teststeps = [
        Step(
            RunRequest("/cgi-bin/token")
            .get("https://api.weixin.qq.com/cgi-bin/token")
            .with_params(
                **{
                    "appid": "wx97f31b7d58806a46",
                    "grant_type": "client_credential",
                    "secret": "ac16be0a8b36a0ebd596c041300869ae",
                }
            )
            .with_headers(
                **{
                    "Postman-Token": "df1bf99c-e213-42a3-b763-80d87896faf3",
                    "User-Agent": "PostmanRuntime/7.29.0",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json; encoding=utf-8")
            .assert_equal("body.expires_in", 7200)
        ),
    ]


if __name__ == "__main__":
    TestCaseGettoken().test_start()
