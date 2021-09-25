# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases\externalInterface\basicInformation\getOrganizationUnitList.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGetorganizationunitlist(HttpRunner):

    config = Config("获取医院基础科室信息接口").base_url("${ENV(baseUrl_dongHua)}").verify(False)

    teststeps = [
        Step(
            RunRequest("获取医院科室信息接口")
            .get("/organizationUnit/list")
            .extract()
            .with_jmespath("body.data[1].parentId", "parentId")
            .validate()
            .assert_equal("body.responseCode", "0")
            .assert_equal("body.data[0].levelId", 4)
            .assert_equal("body.data[1].levelId", 5)
            .assert_equal("body.data[6].levelId", 6)
            .assert_equal("body.data[0].organizationUnitId", "$parentId")
        ),
    ]


if __name__ == "__main__":
    TestCaseGetorganizationunitlist().test_start()