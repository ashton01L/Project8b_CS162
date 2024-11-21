# Author: Ashton Lee
# Github User: ashton01L
# Date: 11/20/2024
# Description: For this project, you will import the time and random modules.
import time
import random
from functools import wraps
from matplotlib import pyplot as plt


# Decorator to time functions
def sort_timer(func):
    """
    A decorator used to measure the amount of time a function takes to execute.
    :param:
     func (callable):  The function that will be timed.
    :return:
        callable: A wrapper function that returns the time elapsed time in seconds
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        return end - start

    return wrapper


@sort_timer
def bubble_sort(arr):
    """
    Implementation of the bubble sort algorithm.

    :param:
        arr (list): The list that is to be sorted
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


@sort_timer
def insertion_sort(arr):
    """
    Implementation of the insertion sort algorithm.

    :param:
        arr (list): The list that is to be sorted
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def make_lists_of_sort_times(sort1, sort2, lengths):
    """
    Creates randomized lists of varying lengths, then times the sorting functions

    :param:
        sort1 (callable): The 1st sorting function.
        sort2 (callable): The 2nd sorting function.
        lengths (list of int): List of lengths for the random lists.
    :return:
        tuple: Two lists which each respectively hold the sorting times for each algorithm.
    """
    sort1_times = []  # List to store times of 1st sort function
    sort2_times = []  # List to store times of 2nd sort function

    for length in lengths:
        # Generates a random list of integers
        random_list = [random.randint(1, 10000) for _ in range(length)]

        # Create separate copies to be used for each sort
        list_1 = list(random_list)
        list_2 = list(random_list)

        # Record the times taken for the sorting for both algorithms
        sort1_times.append(sort1(list_1))
        sort2_times.append(sort2(list_2))

    return sort1_times, sort2_times


def compare_sorts(sort1, sort2):
    """
    Compares the two sorting algorithms by timing each and plotting them by performance (time in seconds)
    :param:
        sort1 (callable): The 1st sorting function
        sort2 (callable): The 2nd sorting function
    """
    lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    sort1_times, sort2_times = make_lists_of_sort_times(sort1, sort2, lengths)

    # Plot the results
    plt.plot(lengths, sort1_times, 'ro--', linewidth=2, label='Bubble Sort')
    plt.plot(lengths, sort2_times, 'go--', linewidth=2, label='Insertion Sort')

    # Add title, labels and legend
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.legend(loc='upper left')
    plt.title("Sorting Algorithm Comparison")
    plt.show()


def main():
    """
    Main function to execute the application and sort the algorithms, generate graph

    :return: pop-up gui graph
    """
    compare_sorts(bubble_sort, insertion_sort)


if __name__ == "__main__":
    main()
