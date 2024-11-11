#!/usr/bin/env python3
import re


def replace_all(str_pattern, str_replace, file1, file2):
    with open(file1, 'r') as fp1, open(file2, 'w') as fp2:
        for line in fp1:
            line = re.sub(str_pattern, str_replace, line)
            fp2.write(line)

def main():
    replace_all(r'photos', 'images', 'photos/notes.txt', 'output/new_notes.txt')

if __name__ == '__main__':
    main()