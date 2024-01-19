import datetime
import time
import sys
import os


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
    files = [os.path.join(root, file) for root, dirs, files in os.walk(sys.argv[1]) for file in files]
    for name in files:
        read_file(name)
    print(datetime.datetime.now() - begin)

main()


