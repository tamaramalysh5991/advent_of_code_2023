def get_input(file_name):
    with open(file_name, 'r') as f:
        data = f.read().splitlines()
    return data