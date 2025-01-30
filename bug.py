def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some operations on file f ... 
    # Missing f.close() call