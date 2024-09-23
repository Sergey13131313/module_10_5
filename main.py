from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as f:
        all_data = [line.strip() for line in f]


if __name__ == '__main__':
    list_file = ['file {}.txt'.format(i) for i in range(1, 5)]

    # start = datetime.now()
    # for file in list_file:
    #     read_info(file)
    # end = datetime.now()
    # print(end - start)
    # 0: 00:05.381242

    start = datetime.now()
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(read_info, list_file)
    end = datetime.now()
    print(end - start)
    # 0:00:02.529619


