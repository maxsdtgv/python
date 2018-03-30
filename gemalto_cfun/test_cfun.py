#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from contextlib import suppress

import pytest
import time

from framework.at.atlib.atparser import ATException

from framework.at.atlib import atparser
from framework import cliparser
from framework.cliparser import CliException
from framework.fixtures import logger, test_config


test_config_file = "at_test.json"


@pytest.fixture()
def at_parser(logger, test_config):
    logger.setLevel(logging.DEBUG)
    at_parser = atparser.AtParser(test_config["serial"]["port"],
                                  test_config["serial"]["baud"],
                                  rcts=test_config["serial"]["rtscts"],
                                  timeout=test_config["serial"]["timeout"],
                                  bytesize=test_config["serial"]["bytesize"],
                                  parity=test_config["serial"]["parity"],
                                  stopbits=test_config["serial"]["stopbits"],
                                  logger=logger)
    yield at_parser


@pytest.fixture()
def cli_parser(logger, test_config):
    logger.setLevel(logging.DEBUG)
    cli_parser = cliparser.CliParser(test_config["cli_serial"]["port"],
                                    test_config["cli_serial"]["baud"],
                                    rcts=False, logger=logger)
    yield cli_parser


@pytest.fixture()
def execute_preconditions(at_parser: atparser.AtParser,
                          cli_parser: cliparser.CliParser):
    at_parser.sendAt('AT^RESET')
    cli_parser.waitUntil('[PSP] started', 100)
    pass


def test_at_cfun_cmd(logger, at_parser: atparser.AtParser,
                     cli_parser: cliparser.CliParser, execute_preconditions):
    it = 100000
    while it:
        it -= 1
        logger.info("ITERATION {}".format(100000 - it))
        at_parser.sendAt('AT+CFUN=0')
        at_parser.sendAt('AT+CFUN=1')
        res = ""
        while not "+CGACT: 3,1" in res:
            time.sleep(1)
            with suppress(ATException):
                res = at_parser.sendAt('AT+CGACT?')
        cli_parser.clean()
        cli_parser.writeCliLine("infoAllTask")
        cli_parser.readCliSuccess()