import datetime
import time
import os
import argparse


def read_file(filename):
    with open(filename, mode='rb') as f:
        print(filename)
        while True:
            time.sleep(0.001)
            data = f.read(1024)
            if not data:
                print(filename, "done ###############")
                break
def main():
    begin = datetime.datetime.now()
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str)
    args = parser.parse_args()
    files = [os.path.join(root, file) for root, dirs, files in os.walk(args.dir) for file in files]
    for name in files:
        read_file(name)
    print(datetime.datetime.now() - begin)

main()


