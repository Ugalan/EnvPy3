# EnvPy3
一个测试用例，只要预置条件（setup）或者测试步骤（test_step）执行失败那么恢复环境（teardown）下的所有方法都会执行，即使teardown有方法抛出异常。特别的如果设置了标识TEST_RESULT = 0，那么特定的方法会根据此标识决定是否执行。
