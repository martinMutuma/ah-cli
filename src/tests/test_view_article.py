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

    def test_view_article(self, mocked_method):
        """ Test view article """
        mocked_method.get = self.mock_get(mocked_method)
        result = self.runner.invoke(ah, ['view'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("title", result.output)

    def test_export_article_to_json(self, mocked_method):
        """Test view article with export to json

        Arguments:
            mocked_method {[type]} -- [description]
        """
        mocked_method.get = self.mock_get(mocked_method)
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(
                ah, ['view', '--export', 'test-article', '--json'])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.isfile('./imports/test-article.json'))

    def test_export_article_to_csv(self, mocked_method):
        """Test view article with export to csv

        Arguments:
            mocked_method {[type]} -- [description]
        """
        mocked_method.get = self.mock_get(mocked_method)
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(
                ah, ['view', '--export', 'test-article', '--csv'])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.isfile('./imports/test-article.csv'))

    def test_export_article_to_csv_and_json(self, mocked_method):
        """Test view article with export to json and csv

        Arguments:
            mocked_method {[type]} -- [description]
        """
        mocked_method.get = self.mock_get(mocked_method)
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(
                ah, ['view', '--export', 'test-article', '--csv', '--json'])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.isfile('./imports/test-article.csv'))
            self.assertTrue(os.path.isfile('./imports/test-article.json'))
