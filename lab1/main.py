from park import Park
from counter import Counter
from datetime import datetime
from quick_sort import Quicksort
from bubblesort import Bubblesort
import csv


def read_data_from_file():
    parks_list = []
    try:
        with open('parks.csv') as csvin:
            reader = csv.reader(csvin)
            for row in reader:
                new_park = Park(row[0], int(row[1]), int(row[2]))
                parks_list.append(new_park)
    except FileNotFoundError:
        print("File with data does not exist!")
    return parks_list


def work_time(start_time, finish_time):
    return finish_time - start_time


def print_answer(algo_name, work_time, compare_num, swap_num, sorted_list):
    print(str(algo_name) + "\nWork time: " + str(work_time) + "\nNumber of comparisons: " + str(compare_num) +
          "\nNumber of swaps: " + str(swap_num) + "\nResult: \n" + str(sorted_list))


if __name__ == "__main__":
    parks_list = read_data_from_file()

    bubblesort = Bubblesort()
    start = datetime.now().microsecond
    result = bubblesort.bubble_sort(parks_list)
    end = datetime.now().microsecond
    print("Bubblesort")
    print("Work time=" + str(end - start))
    print("Number of comparisons:" + str(bubblesort.compareCount))
    print("Number of swaps:" + str(bubblesort.swap))
    print("Result:")
    for i in result:
        print(i)
    print("\n\n")

    Counter.count_reset()
    sorted_list_quicksort = Quicksort(parks_list)
    start_time = datetime.now().microsecond
    sorted_list_quicksort.quick_sort(0, len(parks_list) - 1)
    finish_time = datetime.now().microsecond
    print_answer("Quicksort", work_time(start_time, finish_time), Counter.compare_num, Counter.exchange_num,
                 sorted_list_quicksort.sort_list)
    print("\n\n")
