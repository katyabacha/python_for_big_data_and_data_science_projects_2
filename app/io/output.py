import pandas as pd


def output_text_console(text):
    """
        Function to output text to the console.

        Parameters:
            text (str): The text to be output.

        Returns:
            None
    """
    print("Output text: ", text)


def write_file_builtin(text, file_path):
    """
    Function to write to a file using Python's built-in capabilities.

    Parameters:
        text (str or pandas.DataFrame): The text or DataFrame to be written to the file.
        file_path (str): The path to the file to be written.

    Returns:
        None
    """
    if isinstance(text, str):
        with open(file_path, 'w', newline='') as file:
            file.write(text)
    elif isinstance(text, pd.DataFrame):
        with open(file_path, 'w', newline='') as file:
            column_names = text.columns.tolist()
            file.write(','.join(column_names) + '\n')

            for index, row in text.iterrows():
                file.write(','.join(map(str, row)) + '\n')
    else:
        raise ValueError("Unsupported type for text. Supported types are str and pandas.DataFrame.")
