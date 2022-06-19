#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022-06-19 12:22:30
# @Author : 朱宏玉


import allure
import pytest
from common.setting import ConfigHandler
from utils.readFilesUtils.get_yaml_data_analysis import CaseData
from utils.assertUtils.assertControl import Assert
from utils.requestsUtils.requestControl import RequestControl
from utils.readFilesUtils.regularControl import regular
from utils.requestsUtils.teardownControl import TearDownHandler


TestData = CaseData(ConfigHandler.data_path + r'Attendance/get_attendance_record.yaml').case_process()
re_data = regular(str(TestData))


@allure.epic("云业务平台接口")
@allure.feature("考勤管理模块")
class TestGetAttendanceRecord:

    @allure.story("考勤台账-管理员")
    @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
    def test_get_attendance_record(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl().http_request(in_data)
        TearDownHandler().teardown_handle(res)
        Assert(in_data['assert']).assert_equality(response_data=res['response_data'], 
                                                  sql_data=res['sql_data'], status_code=res['status_code'])


if __name__ == '__main__':
    pytest.main(['test_get_attendance_record.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
