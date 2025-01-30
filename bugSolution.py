def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... operations on file f ...
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File is closed") #Check whether the file is closed or not