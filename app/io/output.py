def output_text_console(text):
    print("Output text: ", text)


def write_file_builtin(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)
