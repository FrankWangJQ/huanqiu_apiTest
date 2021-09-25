# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases\externalInterface\patient\getPatient.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGetpatient(HttpRunner):

    config = (
        Config("通过患者ID（身份证号）查询患者在院内系统建立的档案信息")
        .base_url("${ENV(baseUrl_dongHua)}")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("通过患者ID（身份证号）查询患者在院内系统建立的档案信息")
            .get("/patient")
            .with_params(**{"type": 3, "patientId": 130633199001036815})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseGetpatient().test_start()