import pathlib
import shutil
from unittest import TestCase

from vocabulary.config.initialize import init_config_dir


class ConfigTestCase(TestCase):

    def setUp(self):
        self.default_config_dir_path = pathlib.Path.home() / '.pyvocabulary'

        self._delete_config_dir()

    def _delete_config_dir(self):
        if self.default_config_dir_path.exists():
            shutil.rmtree(self.default_config_dir_path)

    def test_config_dir_initialization(self):
        config_dir_path = init_config_dir()

        self.assertEqual(config_dir_path, pathlib.Path.home() / '.pyvocabulary')
        self.assertTrue(config_dir_path.exists())


if __name__ == '__main__':
    unittest.main()
