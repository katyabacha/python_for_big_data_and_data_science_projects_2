import pandas as pd


def input_text_console():
    text = input("Input text: ")
    return text


def read_file_builtin(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def read_file_pandas(file_path):
    data = pd.read_csv(file_path)
    text = ' '.join(data.values.flatten())
    return text
