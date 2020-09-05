import sys
import json

def read_original_file(filename):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
        
    pass

def build_graph():
    pass

def write_to_json(data, filename):
    json.dumps(data)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_original_file(input_file)
    data = build_graph(data)
    write_to_json(data, output_file)
