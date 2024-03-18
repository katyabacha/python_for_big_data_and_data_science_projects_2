from app.io.input import input_text_console, read_file_builtin, read_file_pandas
from app.io.output import output_text_console, write_file_builtin


def main():
    # Get text from console
    input_text = input_text_console()

    # Read text from a file
    file_text_builtin = read_file_builtin("data/file.txt")

    # Read text from a CSV file
    file_text_pandas = read_file_pandas("data/file.csv")

    # Output text from console
    output_text_console(input_text)
    output_text_console(file_text_builtin)
    output_text_console(file_text_pandas)

    # Write text to file using built-in capabilities
    write_file_builtin(input_text, "data/output.txt")
    write_file_builtin(file_text_builtin, "data/output_builtin.txt")
    write_file_builtin(file_text_pandas, "data/output_pandas.txt")


if __name__ == "__main__":
    main()
