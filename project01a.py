import sys
import numpy as np
import matplotlib.pyplot as plt
sys.setrecursionlimit(900000)

# ---------------------------------------------
# Task 1: Fibonacci Sequence and GCD ----------

# Return the kth number in the Fibonacci Sequence: Θ(phi^k) or Θ(phi^2^b)
def fib(k):
    if k == 0: return 0, 0
    if k == 1: return 1, 0
    else:
        val1, ops1 = fib(k-1)   # where val1 = fib(k-1)[0] and ops1 = fib(k-1)[1]
        val2, ops2 = fib(k-2)
        return val1 + val2, ops1 + ops2 + 1

# Return gcd(m, n): Θ(n) --> Θ(2^b)
def euclidGCD(m, n):
    if n == 0: return m, 0
    if n == 1: return 1, 0
    else:
        val, ops = euclidGCD(n, m % n)
        return val, ops + 1

# ---------------------------------------------
# Task 2: Exponentiation ----------------------

# Decrease by One: Θ(n) or Θ(2^b)
def exp1(a, n):
    if n == 0: return 1, 0     # Note: a^0 = 1 for all values of a.
    if n == 1: return a, 0     # Note: a^1 = a for all values of a.
    else:
        val, ops = exp1(a, n-1)
        return a * val, ops + 1
"""
Basic operation: multiplication.
Thus, M(n) = M(n-1) + 1
* The 'M(n-1)' represents the number of basic operations/multiplications in computing exp1(a, n-1)
* The '+ 1' represents the additional basic operation/multiplication in computing exp1(a, n-1) * a
After solving the recurrence relation, we find M(n) = n.
Therefore, exp1 is in Θ(n).
"""

# Decrease by Constant Factor: Θ(log n)
def exp2(a, n):
    if n == 0: return 1, 0      # Note: a^0 = 1 for all values of a.
    if n == 1: return a, 0      # Note: a^1 = a for all values of a.
    elif n % 2 == 0:            # If n is even:
        val, ops = exp2(a, n/2)
        return val ** 2, ops + 1     # Increment ops by one due to squaring.
    else:                       # If n is odd:
        val, ops = exp2(a, (n-1) / 2)
        return a * val ** 2, ops + 2 # Increment ops by two due to squaring and multiplying.
"""
As per the textbook, on page 133, we are reducing the problem size by about half at the expense of one or two multiplications.
This suggests that this algorithm is in Θ(log n).
"""

# Divide and Conquer: Θ(log n) ==> Θ(n log n)?

def exp3(a, n):
    if n == 0: return 1, 0              # Note: a^0 = 1 for all values of a.
    if n == 1: return a, 0              # Note: a^1 = a for all values of a.
    elif n % 2 == 0:    # If n is even:
        val, ops = exp3(a, n/2)
        return val * val, ops + 1       # Increment ops by one due to single multiplication of val * val
    else:               # If n is odd:
        val, ops = exp3(a, (n-1)/2)         # According to the project page, (n-1)/2. However, everywhere online uses n/2 and it does not seem to effect the result.
        return a * val * val, ops + 2   # Increment ops by two due to two multiplications of a * val * val.
"""
Recurrence Relation:
M(n)    =   M(n/2) + 1
        =   M(n/4) + 1
        =   M(n/8) + 1
"""
# ---------------------------------------------
# Task 3: Sorting------------------------------

def selectionSort(arr_in, n):
    ops=0
    arr = arr_in.copy()
    i = 0
    while i < n-1:
        bigIdx = 0
        j = 1
        while j < n-i:
            if arr[j] > arr[bigIdx]:
                bigIdx = j
            ops+=1
            j = j + 1
        arr[bigIdx], arr[n-i-1] = arr[n-i-1], arr[bigIdx]   # swap(arr, bigIdx, n-i-1)
        i = i + 1
    return arr, ops

def insertionSort(arr_in, n):
    ops=0
    arr = arr_in.copy()
    i = 0
    while i < n:
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            ops+=1
            j = j - 1
        ops+=1
        i = i + 1
    return arr, ops


# Loads the randomly sorted datasets
def load_dataset(n):
    dataset_values = []
    dataset = "data/testSet/data" + str(n) + ".txt"
    open_dataset = open(dataset, 'r')
    for line in open_dataset:
        dataset_values.append(int(line.strip()))
    return dataset_values

def load_rsorted_dataset(n):
    dataset_values = []
    dataset = "data/testSet/data" + str(n) + "_rSorted.txt"
    open_dataset = open(dataset, 'r')
    for line in open_dataset:
        dataset_values.append(int(line.strip()))
    return dataset_values

def load_sorted_dataset(n):
    dataset_values = []
    dataset = "data/testSet/data" + str(n) + "_sorted.txt"
    open_dataset = open(dataset, 'r')
    for line in open_dataset:
        dataset_values.append(int(line.strip()))
    return dataset_values

def print_sets():
    j=0
    n_range = list(range(100, 10001, 1000))
    avg_lists = [[]] * (len(n_range))
    sorted_lists =[[]] * (len(n_range))
    rsorted_lists =[[]] * (len(n_range))

    selectionsort_avg_ops_list = []
    insertionsort_avg_ops_list = []

    selectionsort_sorted_ops_list = []
    insertionsort_sorted_ops_list = []

    selectionsort_rsorted_ops_list = []
    insertionsort_rsorted_ops_list = []
    
    for i in n_range:
        avg_lists[j] = load_dataset(i)
        selectionsort_avg_ops_list.append(selectionSort(avg_lists[j], i)[1])
        insertionsort_avg_ops_list.append(insertionSort(avg_lists[j], i)[1])
    
        sorted_lists[j] = load_sorted_dataset(i)
        selectionsort_sorted_ops_list.append(selectionSort(sorted_lists[j], i)[1])
        insertionsort_sorted_ops_list.append(insertionSort(sorted_lists[j], i)[1])

        rsorted_lists[j] = load_rsorted_dataset(i)
        selectionsort_rsorted_ops_list.append(selectionSort(rsorted_lists[j], i)[1])
        insertionsort_rsorted_ops_list.append(insertionSort(rsorted_lists[j], i)[1])
        j+=1

    print("average-case cost:")
    # print("selection: {}".format(selectionsort_avg_ops_list))#;print(selectionsort_avg_ops_list)
    # print("insertion: {}".format(insertionsort_avg_ops_list))#;print(insertionsort_avg_ops_list)
    # -- scatter for avg-case
    plt.title("Average-Case")
    plt.xlabel("size n")
    plt.ylabel("operations")
    plt.scatter(n_range, selectionsort_avg_ops_list, c=(1, 0, 0), alpha=.5, marker="<",label = "selection")
    plt.scatter(n_range, insertionsort_avg_ops_list, c=(0, 1, 0), alpha=1, marker="o", label="insertion") 
    plt.legend(loc='upper left', shadow=True, fontsize='x-large')
    plt.show()
    # ----

    print("\nbest-case cost:")
    # print("selection: {}".format(selectionsort_sorted_ops_list))#;print(selectionsort_sorted_ops_list)
    # print("insertion: {}".format(insertionsort_sorted_ops_list))#;print(insertionsort_sorted_ops_list)
    # -- scatter for best-case
    plt.title("Best-Case")
    plt.xlabel("size n")
    plt.ylabel("operations")
    plt.scatter(n_range, selectionsort_sorted_ops_list, c=(1, 0, 0), alpha=.5, marker="<",label = "selection")
    plt.scatter(n_range, insertionsort_sorted_ops_list, c=(0, 1, 0), alpha=1, marker="o", label="insertion") 
    plt.legend(loc='upper left', shadow=True, fontsize='x-large')
    plt.show()
    # ----

    print("\nworst-case cost")
    # print("selection: {}".format(selectionsort_rsorted_ops_list)) 
    # print("insertion: {}".format(insertionsort_rsorted_ops_list)) 
    # -- scatter for worst-case
    plt.title("Worst-Case")
    plt.xlabel("size n")
    plt.ylabel("operations")
    plt.scatter(n_range, selectionsort_rsorted_ops_list, c=(1, 0, 0), alpha=.5, marker="<",label = "selection")
    plt.scatter(n_range, insertionsort_rsorted_ops_list, c=(0, 1, 0), alpha=1, marker="o", label="insertion") 
    plt.legend(loc='upper left', shadow=True, fontsize='x-large')
    plt.show()
    # ----

###############################################
# User Interface
# print("---------------------------------------------")
print("=============================================")
task_prompt = "---------------------------------------------\n1) Task 1: Fibonacci Sequence and GCD   \n2) Task 2: Exponentiation  \n3) Task 3: Sorting   \n4) Back to Mode Selection     \n\nPlease enter the number corresponding to your preffered task: "
mode_prompt = "User Testing Mode - (0)\nScatter Plot Mode - (1) \nQuit              - (2)\n\nPlease enter the number corresponding to your preferred mode of operation: "
# -------------------------------------
mode = int(input(mode_prompt))
while mode != 2:
    if mode == 0:
        task = int(input(task_prompt))
        while task != 4:
            if task == 1:
                k = int(input(" ----\nPlease enter a nonnegative integer, k: "))
                print("fib(%d): %d" %(k, fib(k)[0] )) #; print(fib(k)[0])
                print("euclidGCD(m, n) where m(fib(k+1)) is %d and n(fib(k)) is %d equals %d" %(fib(k+1)[0], fib(k)[0], euclidGCD(fib(k+1)[0], fib(k)[0])[0])) #; print(euclidGCD(fib(k+1)[0], fib(k)[0]))
                print("Task 1 Completed!")
            if task == 2:
                a = int(input(" --\nPlease enter a value for a: "))
                n = int(input("Please enter a value for n: "))
                print("exp1: %d" %exp1(a, n)[0])
                print("exp2: %d" %exp2(a, n)[0])
                print("exp3: %d" %exp3(a, n)[0])
                # print("exp1:"); print(exp1(a, n)[0])
                # print("exp2:"); print(exp2(a, n)[0])
                # print("exp3:"); print(exp3(a, n)[0])
                print("Task 2 Completed!")
            if task == 3:
                # int conversion mayb not be needed as were calling a file name... open("data<n>.txt")
                n = input("Please enter a value for the size of the list n (between 10-100, at an increment of 10): ")
                print("--- Task 3 ---")
                dataset_values = []
                dataset = "data/smallSet/data" + n + ".txt"
                open_dataset = open(dataset, 'r')
                for line in open_dataset:
                    dataset_values.append(int(line.strip()))
                print("Orginal list: ");print(dataset_values) 
                print("Selection sort: ");print(selectionSort(dataset_values, len(dataset_values))[0])
                print("Insertion sort: ");print(insertionSort(dataset_values, len(dataset_values))[0])
            task = int(input(task_prompt))
    if mode == 1:
        task = int(input(task_prompt))
        while task != 4:
            if task == 1:
                # Create Data
                '''
                k = [2, 4, 6, 8, 10, 12, 14, 16, 18]     # Initialize a list containing values for k representing the x-axis.
                A_of_k= []
                k = [2, 4, 6, 8, 10, 12, 14, 16, 18]     # Initialize a list containing values for k representing the x-axis.
                for i in range(len(k)):         # Populate empty list with A(k) = phi^k... TODO::Need to adjust this value.
                    A_of_k.append(euclidGCD(fib(k[i] + 1)[0], fib(k[i])[0])[1])
                    '''
                k_range = list(range(0, 25))
                fib_ops_list = []
                list_of_fibs = []
                for i in range(0,25):
                    fib_ops_list.append(fib(i)[1])
                    list_of_fibs.append(fib(i)[0])
                # Plot
                plt.scatter(k_range, fib_ops_list, s = np.pi * 35, c = (1, 0, 0), alpha = 1, marker="o")
                plt.title("Fibonacci Sequence")
                plt.xlabel("Input Size K")
                plt.ylabel("Number of Operations")
                plt.show()

                #ecluid
                gcd_ops_list = []
                i = 0
                while i < len(list_of_fibs)-1:
                    gcd_ops_list.append(euclidGCD(list_of_fibs[i], list_of_fibs[i+1])[1])
                    i+=1
                print(len(gcd_ops_list))
                print(len)
                # Plot
                euclid_range = list(range(0, len(gcd_ops_list)))
                plt.scatter(euclid_range, gcd_ops_list, s = np.pi * 35, c = (1, 0, 0), alpha = 1, marker="o")
                plt.title("Euclids algorithm asymptotic complexity".title())
                plt.xlabel("Input Size N")
                plt.ylabel("Number of Operations")
                plt.show()
                # --
            if task == 2:
                # Create Data
                a = 2                                       # Choose value for a. I chose 2 because it is most prevelant in my education.
                n = list(range(1, 24))            # Initialize a list containing values for n that will be shown on the x-axis.
                exp1_a_to_n = []                 # Initialize an empty list the same size as n representing the y-axis.
                exp2_a_to_n = []
                exp3_a_to_n = []
                
                for i in range(len(n)):                     # Populate empty list with the number of operations for each of the values for n... for each method of exponentiation.
                    exp1_a_to_n.append(exp1(a, n[i])[1])       # Method 1: exp1(a, n)
                    exp2_a_to_n.append(exp2(a, n[i])[1])       # Method 2: exp2(a, n)
                    exp3_a_to_n.append(exp3(a, n[i])[1])       # Method 3: exp3(a, n)
                # Plot
                plt.title("Computing a^n")
                plt.xlabel("Input Size n")
                plt.ylabel("Number of Operations")
                # s=np.pi * 100, ... s=np.pi * 25, ...  s=np.pi * 100
                plt.scatter(n, exp1_a_to_n, s=np.pi * 100, color = "green", alpha=1, marker="<", label="exp1")   # plot / scatter for method 1 (exp1)
                plt.scatter(n, exp2_a_to_n, s=np.pi * 25, color = 'red', alpha=1, marker="o", label="exp2")     # plot / scatter for method 2 (exp2)
                plt.scatter(n, exp3_a_to_n, s=np.pi * 100, color = 'blue', alpha=.20, marker=">", label="exp3")   # plot / scatter for method 3 (exp3)
                plt.legend(loc='upper left', shadow=True, fontsize='x-large')
                plt.show()
            if task == 3:
                # plot scatter graphs
                print_sets()
                ## ----
            task = int(input(task_prompt))
    mode = int(input(mode_prompt))
