# -*- coding:utf-8 -*-
import pytest

TEST_RESULT = 0
class TestCase:
    def preshell(self):
        print("\033[1;31;40m" + "preshell" + "\033[0m")
        # assert 2 == 1 + 2

    def sufshell(self, msg):
        print("\033[1;31;40m" + msg + "\033[0m")

    @pytest.fixture(scope="module")
    def setup_module(self, request):
        matrix = [
            lambda: self.sufshell("sufshell_01"),
            lambda: self.sufshell("sufshell_02" if TEST_RESULT == 0 else ()),
            lambda: self.sufshell("sufshell_03")]

        for item in reversed(matrix):
            request.addfinalizer(item)

        self.preshell()

    def test_step(self, setup_module):
        print("\033[1;31;40m" + "test_step" + "\033[0m")
        assert 2 == 1 + 2

        global TEST_RESULT
        TEST_RESULT = 1
"""
        def teardown_module():
            print("\033[1;31;40m" + "teardown_module_01" + "\033[0m")
        request.addfinalizer(teardown_module)
"""
"""
    def setup_class(self):
        print("\033[1;31;40m" + "setup_class" + "\033[0m")

    def teardown_class(self):
        print("\033[1;31;40m" + "teardown_class_01" + "\033[0m")
        assert 2 == 1 + 1
        print("\033[1;31;40m" + "teardown_class_02" + "\033[0m")
        assert 2 == 1 + 2
        print("\033[1;31;40m" + "teardown_class_03" + "\033[0m")

    @pytest.mark.maintain_mng
    def test_step(self):
        print("\033[1;31;40m" + "test_step" + "\033[0m")
        assert 2 == 1 + 1
"""
