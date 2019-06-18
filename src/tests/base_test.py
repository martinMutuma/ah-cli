from click.testing import CliRunner

import unittest
from unittest import mock


class BaseTest(unittest.TestCase):
    runner = CliRunner()

    def mock_get(self, methodObj,  many=False):
        """Moking api call for get articles

        Arguments:
            methodObj {[type]} -- [Method instance from the test]

        Returns:
            [unittest.mock] -- [mocked with added returns
            ]
        """
        methodObj.return_value = mock.Mock(ok=True)
        if many:
            methodObj.return_value.json.return_value = {'articles': [{
                "title": "Test article", "slug": "test-article"},
                {"title": "Test article2", "slug": "test-article2"}]}
        else:
            methodObj.return_value.json.return_value = {'article': {
                "title": "Test article", "slug": "test-article"}}

        return methodObj
