# import pprint as PrettyLogger
# import logging as log
# import sys
# import os
import config
import configparser
import testsuites
from enum import Enum

EnvironmentList = Enum('env', ['local', 'test', 'prod'])
InitBuildSetup = bool

config = configparser.ConfigParser()


def tests_init(env):
    tests_passed = []
    tests_failed = []
    exception_thrown = object()
    if env == 'local':
        # Built
        # Rendered
        # MeaningfulFirstPaint
        # Performance
        # if tests_passed:
        #     PrettyLogger(f'Tests  {tests_passed} PASSED.')
        #     PrettyLogger(f'Tests  {tests_failed} Failed spectacularly with {exception_thrown}')
        pass

    if env == 'test':
        # Run local test suites, handle for server-side Crypts
        # Ensure services communicate and resolve
        # Client <-> Server perf
        # Debug Auth

        # return test_suites(env)
        pass
    if env == 'prod':
        pass


def set_environment(Environment):
    # evaL if we have a real env set, if not just throw an exception instead of guessing
    if Environment in EnvironmentList:
        InitBuildSetup = config.Build(Environment.Success)
        with open('./data/config.ini', 'r') as configfile:
            if configfile is None or False:
                raise Exception("Did you build the INI")
        # log()
        return;


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tests_init()
    # local, test, prod
    Environment = 'local'
    set_environment(Environment)

    # Build(ENV)
    # TestSuites(ENV);
    pass
