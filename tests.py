import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


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


class TestGetFileContent(unittest.TestCase):

    def test_get_files_info_current_directory(self):
        result = get_file_content("calculator", "lorem.txt")
        self.assertIn('[...File /home/jk/src/ai-agent/calculator/lorem.txt truncated at 10000 characters]', result)
        self.assertTrue(len(result) < 10085)
        print("Result for 'calculator/lorem.txt' file:")
        print(result)

        result = get_file_content("calculator", "main.py")
        self.assertIn("from pkg.calculator import Calculator", result)
        self.assertIn("from pkg.render import render", result)
        self.assertIn("calculator = Calculator()", result)
        print("Result for 'calculator/main.py' file:")
        print(result)

    def test_get_files_info_pkg_directory(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        self.assertIn("class Calculator:", result)
        self.assertIn("def evaluate(self, expression):", result)
        self.assertIn("def _apply_operator(self, operators, values):", result)
        print("Result for 'pkg/calculator.py' file:")
        print(result)

    def test_get_files_info_outside_directory_bin(self):
        result = get_file_content("calculator", "/bin/cat")
        self.assertEqual(
            result,
            'Error: Cannot read "/bin/cat" as it is outside the permitted working directory',
        )
        print("Result for '/bin/cat' file:")
        print(result)

    def test_get_files_info_outside_directory_parent(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertEqual(
            result,
            'Error: File not found or is not a regular file: "pkg/does_not_exist.py"',
        )
        print("Result for 'pkg/does_not_exist.py' file:")
        print(result)


if __name__ == "__main__":
    unittest.main()
