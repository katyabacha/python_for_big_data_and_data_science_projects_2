import pandas as pd


def input_text_console():
    """
        Function to input text from the console.

        Returns:
            str: The text input from the console.
    """
    text = input("Input text: ")
    return text


def read_file_builtin(file_path):
    """
        Function to read from a file using Python's built-in capabilities.

        Parameters:
            file_path (str): The path to the file to be read.

        Returns:
            str: The content of the file.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def read_file_pandas(file_path):
    """
    Function to read from a file using the 'pandas' library.

    Parameters:
        file_path (str): The path to the CSV file to be read.

    Returns:
        pandas.DataFrame or None: The DataFrame containing the data read from the CSV file,
        or None if the file cannot be found or is empty.
    """
    try:
        dataframe = pd.read_csv(file_path)
        return dataframe
    except FileNotFoundError:
        print(f'CSV file with path {file_path} can\'t be found')
        return None
    except pd.errors.EmptyDataError:
        print(f'CSV file with path {file_path} is empty')
        return None
