import unittest
import pandas as pd
from pathlib import Path
from app.io.input import read_file_builtin, read_file_pandas


class TestReadInputFile(unittest.TestCase):
    def setUp(self):
        self.tmp_text_file_content = "Line 1\nLine 2\nLine 3"
        self.tmp_csv_file_data = {'A': [1, 2, 3], 'B': [4, 5, 6]}

    def test_read_input_file_file_exists(self):
        tmp_text_file = self.create_tmp_text_file(self.tmp_text_file_content)
        expected = "Line 1\nLine 2\nLine 3"
        self.assertEqual(read_file_builtin(tmp_text_file), expected)

    def test_read_input_file_file_not_found(self):
        file_path = "../data/non_existent_file.txt"
        expected = None
        self.assertEqual(read_file_builtin(file_path), expected)

    def test_read_input_file_empty_file(self):
        tmp_path = "../data/empty_file.txt"
        Path(tmp_path).touch()
        expected = ""
        self.assertEqual(read_file_builtin(tmp_path), expected)

    def test_read_input_file_pandas_file_exists(self):
        tmp_csv_file = self.create_tmp_csv_file(self.tmp_csv_file_data)
        df = pd.DataFrame(self.tmp_csv_file_data)
        self.assertTrue(read_file_pandas(tmp_csv_file).equals(df))

    def test_read_input_file_pandas_file_not_found(self):
        file_path = "../data/non_existent_file.csv"
        self.assertIsNone(read_file_pandas(file_path))

    def test_read_input_file_pandas_empty_file(self):
        tmp_path = "../data/empty_file.csv"
        Path(tmp_path).touch()
        self.assertIsNone(read_file_pandas(tmp_path))

    @staticmethod
    def create_tmp_text_file(content):
        tmp_text_file = "../data/tmp_text_file.txt"
        with open(tmp_text_file, "w") as file:
            file.write(content)
        return tmp_text_file

    @staticmethod
    def create_tmp_csv_file(data):
        tmp_csv_file = "../data/tmp_csv_file.csv"
        df = pd.DataFrame(data)
        df.to_csv(tmp_csv_file, index=False)
        return tmp_csv_file


if __name__ == '__main__':
    unittest.main()
