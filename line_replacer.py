import sys
import getopt
import argparse


def replace_line_in_file(file_name, line_to_delete, line_to_insert):
    f = open(file_name, "r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i.startswith(line_to_delete):
            f.write(line_to_insert + '\n')
            print('\n\tReplaced line {i}\n\twith "{line_to_insert}" \n\tin file "{file_name}"\n\n.'.format(**locals()))
        else:
            f.write(i)
    f.truncate()
    f.close()


def parse_args():
    """ Parsed command line arguments """
    parser = argparse.ArgumentParser(
        description="Program used for replacing line in file")
    parser.add_argument(
        "--insert_line", help="line you want to insert (complete line)")
    parser.add_argument(
        "--delete_line", help="line you want to delete (starts with)")
    parser.add_argument(
        "--file_to_modify", help="full path to the file you want line to be modified")

    return parser.parse_args()


def main():
    parsed_args = parse_args()
    replace_line_in_file(parsed_args.file_to_modify,
                         parsed_args.delete_line, parsed_args.insert_line)


main()
