from src.index import ah
from .base_test import BaseTest
from unittest import mock
import os


@mock.patch("utils.fetch.get")
class TestViewArticle(BaseTest):
    """Tests for view Article endpoint consumer
    Arguments:
        BaseTest {[unittestt.testcase]}
    """

    def test_list_articles(self, mocked_method):
        """ Test view article """
        mocked_method.get = self.mock_get(mocked_method, many=True)
        result = self.runner.invoke(ah, ['list'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("title", result.output)

    def test_export_articles_to_json(self, mocked_method):
        """Test view article with export to json

        Arguments:
            mocked_method {[type]} -- [description]
        """
        mocked_method.get = self.mock_get(mocked_method,  many=True)
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(
                ah, ['list', '--export', '--json'])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.isfile('./imports/all_articles.json'))

    def test_export_articles_to_csv(self, mocked_method):
        """Test view article with export to csv

        Arguments:
            mocked_method {[type]} -- [description]
        """
        mocked_method.get = self.mock_get(mocked_method,  many=True)
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(
                ah, ['list', '--export',  '--csv'])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.isfile('./imports/all_articles.csv'))

    def test_export_articles_to_csv_and_json(self, mocked_method):
        """Test view article with export to json and csv

        Arguments:
            mocked_method {[type]} -- [description]
        """
        mocked_method.get = self.mock_get(mocked_method, many=True)
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(
                ah, ['list', '--export', '--csv', '--json'])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.isfile('./imports/all_articles.csv'))
            self.assertTrue(os.path.isfile('./imports/all_articles.json'))
