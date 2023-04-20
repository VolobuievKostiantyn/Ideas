import argparse
import os
import string
import random

PREFIX_SPLITTER = "000 - "
PREFIX_LEN = 7
DEFAULT_SRC_DIR = "./"
EXT_DOT = "."
DEFAULT_FILE_EXT = "mp3"


def prefix_generator(size=PREFIX_LEN, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size)) + PREFIX_SPLITTER


def main():
    parser = argparse.ArgumentParser(
        description='''Shuffle_file_names v0.1. Run inside source directory or set the directory''')
    parser.add_argument("-e", "--extention", type=str, default=DEFAULT_FILE_EXT, help='Source directory')
    args = parser.parse_args()
    curr_file_extension = EXT_DOT + args.extention

    for filename in os.listdir(DEFAULT_SRC_DIR):
        is_find = filename.find(PREFIX_SPLITTER)
        if filename.endswith(curr_file_extension):
            curr_prefix = prefix_generator()
            if is_find == -1:  # add new prefix
                new_file_name = curr_prefix + filename
            else:  # change old prefix
                new_file_name = filename[:0] + curr_prefix[:PREFIX_LEN] + filename[PREFIX_LEN:]

            print(new_file_name)
            os.rename(filename, new_file_name)


if __name__ == '__main__':
    main()