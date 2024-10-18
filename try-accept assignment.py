#Christopher Kenny
#CS-175
#Try-Except

def read_file(file_path, search_term):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if search_term not in content:
                raise Exception(f"'{search_term}' not found in file content.")
        print(f"{search_term} found in file.")

    except FileNotFoundError:
        print(f"[Error]: No such file or directory: {file_path}")
        print("The file has been closed")

    except IsADirectoryError:
        print(f"{file_path} is a directory")

    except Exception as e:
        print(e)

#Enter 'file_path' and 'search term' in calling read_file
read_file('file_path.txt', 'John')
