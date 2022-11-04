# rename_files.py
import argparse
from ast import arg
import os
def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--dir", help="dir of files name need to be sorted")
    parser.add_argument("--start_num", help="start number of rename files")
    # parser.add_argument("--labels", help="labels file", required=True)
    # parser.add_argument("--noviz", help="no visualization", action="store_true")
    args = parser.parse_args()

    file_list = os.listdir(args.dir)
    print(file_list)

if __name__ == '__main__':
    main()
