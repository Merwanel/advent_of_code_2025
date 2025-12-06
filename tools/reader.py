def read_lines(file_path, stripIt = True):
    """
    Reads a file line by line and yields each line stripped of leading/trailing whitespace.
    """
    with open(file_path, 'r') as f:
        for line in f:
            if stripIt :
                yield line.strip()
            else :
                yield line[:-1]