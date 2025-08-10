import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):

    def test_get_files_info_current_directory(self):
        result = get_files_info("calculator", ".")
        self.assertIn("- main.py: file_size=565 bytes, is_dir=False", result)
        self.assertIn("- tests.py: file_size=1331 bytes, is_dir=False", result)
        self.assertIn("- pkg: file_size=4096 bytes, is_dir=True", result)
        print("Result for current directory:")
        print(result)

    def test_get_files_info_pkg_directory(self):
        result = get_files_info("calculator", "pkg")
        self.assertIn("- calculator.py: file_size=1721 bytes, is_dir=False", result)
        self.assertIn("- render.py: file_size=754 bytes, is_dir=False", result)
        print("Result for 'pkg' directory:")
        print(result)

    def test_get_files_info_outside_directory_bin(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(
            result,
            'Error: Cannot list "/bin" as it is outside the permitted working directory',
        )
        print("Result for '/bin' directory:")
        print(result)

    def test_get_files_info_outside_directory_parent(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(
            result,
            'Error: Cannot list "../" as it is outside the permitted working directory',
        )
        print("Result for '../' directory:")
        print(result)


if __name__ == "__main__":
    unittest.main()
