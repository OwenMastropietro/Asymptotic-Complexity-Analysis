import sys
import numpy as np
import matplotlib.pyplot as plt
sys.setrecursionlimit(900000)

# ---------------------------------------------
# Task 1: Fibonacci Sequence and GCD ----------

# Return greatest common divisor of m and n: Θ(n) --> Θ(2^b)
def euclid_GCD(m, n):
    if n == 0: return m, 0
    if n == 1: return 1, 0
    else:
        val, basic_operation_count = euclid_GCD(n, m % n)
        return val, basic_operation_count + 1

# Return the kth number in the Fibonacci Sequence: Θ(phi^k) or Θ(phi^2^b)
def fib(k):
    if k == 0: return 0, 0
    if k == 1: return 1, 0
    else:
        val1, basic_operation_count1 = fib(k-1)   # where val1 = fib(k-1)[0] and basic_operation_count1 = fib(k-1)[1]
        val2, basic_operation_count2 = fib(k-2)
        return val1 + val2, basic_operation_count1 + basic_operation_count2 + 1

# ---------------------------------------------
# Task 2: Exponentiation ----------------------

# Decrease by One:
def exp_1(a, n):
    if n == 0: return 1, 0     # Note: a^0 = 1 for all values of a.
    if n == 1: return a, 0     # Note: a^1 = a for all values of a.
    else:
        val, basic_operation_count = exp_1(a, n-1)
        return a * val, basic_operation_count + 1
"""
Basic operation: Addition/Subtraction.
Recurrence Relation: A(n) = A(n-1) + 1
Time Complexity: Θ(n)
* Proof:
* Note the 'A(n-1)' represents the number of basic operations in computing exp_1(a, n-1).
* Note the '+ 1' represents the additional basic operation/multiplication in computing exp_1(a, n-1) * a.
* Since the basic operation is not activated on A(1), we rely on A(1) = 0 for solving our recurrence relation.
* A(n) = A(n - 1) + 1
*      = [A(n - 2) + 1] + 1
*      = [A(n - 3) + 1] + 2
*      = A(n - 3) + 3
* Given the pattern, we assume the i'th instance of this relation can be expressed as follows:
* A(n) = A(n - i) + i where i = n - 1
*      = A(1) + n - 1
*      = n - 1
* A(n) = n - 1 exists in Θ(n) -- Θ(2^b)
"""

# Decrease by Constant Factor:
def exp_2(a, n):
    if n == 0: return 1, 0      # Note: a^0 = 1 for all values of a.
    if n == 1: return a, 0      # Note: a^1 = a for all values of a.
    elif n % 2 == 0:            # If n is even:
        val, basic_operation_count = exp_2(a, n/2)
        return val ** 2, basic_operation_count + 1     # Increment basic_operation_count by one due to squaring.
    else:                       # If n is odd:
        val, basic_operation_count = exp_2(a, (n-1) / 2)
        return a * val ** 2, basic_operation_count + 2 # Increment basic_operation_count by two due to squaring and multiplying.
"""
Basic operation: Multiplication.
Recurrence Relation: M(n) = M(n/2) + 1
Time Complexity: Θ(log n)
* Proof:
* Since the basic operation is not activated on M(1), we rely on M(1) = 0 for solving our recurrence relation.
* Let n = 2^k such that 2^k / 2 = 2^(k-1).
* M(2^k) = M(2^(k-1)) + 1
*        = [M(2^(k-2)) + 1] + 1
*        = [M(2(k-3)) + 1] + 2
*        = M(2^(k-3)) + 3
* Given the pattern, we assume the i'th instance of this relation can be expressed as follows:
* M(2^k) = M(2^(k-i)) + i where i = k
*        = M(1) + k
* M(2^k) = k
* M(n)   = log n exists in Θ(n) -- Θ(2^b)
"""

# Divide and Conquer: Θ(n)
def exp_3(a, n):
    if n == 0: return 1, 0              # Note: a^0 = 1 for all values of a.
    if n == 1: return a, 0              # Note: a^1 = a for all values of a.
    elif n % 2 == 0:    # If n is even:
        val, basic_operation_count = exp_3(a, n/2)
        return val * val, basic_operation_count + 1       # Increment basic_operation_count by one due to single multiplication of val * val
    else:               # If n is odd:
        val, basic_operation_count = exp_3(a, (n-1)/2)    # According to the project page, (n-1)/2. However, everywhere online uses n/2 and it does not seem to effect the result.
        return a * val * val, basic_operation_count + 2   # Increment basic_operation_count by two due to two multiplications of a * val * val.
"""
Recurrence Relation:
M(n)    =   M(n/2) + 1
        =   M(n/4) + 1
        =   M(n/8) + 1
"""
# ---------------------------------------------
# Task 3: Sorting------------------------------

def selectionSort(arr_in, n):
    basic_operation_count=0
    arr = arr_in.copy()
    i = 0
    while i < n-1:
        bigIdx = 0
        j = 1
        while j < n-i:
            if arr[j] > arr[bigIdx]:
                bigIdx = j
            basic_operation_count+=1
            j = j + 1
        arr[bigIdx], arr[n-i-1] = arr[n-i-1], arr[bigIdx]   # swap(arr, bigIdx, n-i-1)
        i = i + 1
    return arr, basic_operation_count

def insertionSort(arr_in, n):
    basic_operation_count=0
    arr = arr_in.copy()
    i = 0
    while i < n:
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            basic_operation_count+=1
            j = j - 1
        basic_operation_count+=1
        i = i + 1
    return arr, basic_operation_count


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

    selectionsort_avg_basic_operation_count_list = []
    insertionsort_avg_basic_operation_count_list = []

    selectionsort_sorted_basic_operation_count_list = []
    insertionsort_sorted_basic_operation_count_list = []

    selectionsort_rsorted_basic_operation_count_list = []
    insertionsort_rsorted_basic_operation_count_list = []
    
    for i in n_range:
        avg_lists[j] = load_dataset(i)
        selectionsort_avg_basic_operation_count_list.append(selectionSort(avg_lists[j], i)[1])
        insertionsort_avg_basic_operation_count_list.append(insertionSort(avg_lists[j], i)[1])
    
        sorted_lists[j] = load_sorted_dataset(i)
        selectionsort_sorted_basic_operation_count_list.append(selectionSort(sorted_lists[j], i)[1])
        insertionsort_sorted_basic_operation_count_list.append(insertionSort(sorted_lists[j], i)[1])

        rsorted_lists[j] = load_rsorted_dataset(i)
        selectionsort_rsorted_basic_operation_count_list.append(selectionSort(rsorted_lists[j], i)[1])
        insertionsort_rsorted_basic_operation_count_list.append(insertionSort(rsorted_lists[j], i)[1])
        j+=1

    print("average-case cost:")
    # print("selection: {}".format(selectionsort_avg_basic_operation_count_list))#;print(selectionsort_avg_basic_operation_count_list)
    # print("insertion: {}".format(insertionsort_avg_basic_operation_count_list))#;print(insertionsort_avg_basic_operation_count_list)
    # -- scatter for avg-case
    plt.title("Average-Case")
    plt.xlabel("size n")
    plt.ylabel("operations")
    plt.scatter(n_range, selectionsort_avg_basic_operation_count_list, c=(1, 0, 0), alpha=.5, marker="<",label = "selection")
    plt.scatter(n_range, insertionsort_avg_basic_operation_count_list, c=(0, 1, 0), alpha=1, marker="o", label="insertion") 
    plt.legend(loc='upper left', shadow=True, fontsize='x-large')
    plt.show()
    # ----

    print("\nbest-case cost:")
    # print("selection: {}".format(selectionsort_sorted_basic_operation_count_list))#;print(selectionsort_sorted_basic_operation_count_list)
    # print("insertion: {}".format(insertionsort_sorted_basic_operation_count_list))#;print(insertionsort_sorted_basic_operation_count_list)
    # -- scatter for best-case
    plt.title("Best-Case")
    plt.xlabel("size n")
    plt.ylabel("operations")
    plt.scatter(n_range, selectionsort_sorted_basic_operation_count_list, c=(1, 0, 0), alpha=.5, marker="<",label = "selection")
    plt.scatter(n_range, insertionsort_sorted_basic_operation_count_list, c=(0, 1, 0), alpha=1, marker="o", label="insertion") 
    plt.legend(loc='upper left', shadow=True, fontsize='x-large')
    plt.show()
    # ----

    print("\nworst-case cost")
    # print("selection: {}".format(selectionsort_rsorted_basic_operation_count_list)) 
    # print("insertion: {}".format(insertionsort_rsorted_basic_operation_count_list)) 
    # -- scatter for worst-case
    plt.title("Worst-Case")
    plt.xlabel("size n")
    plt.ylabel("operations")
    plt.scatter(n_range, selectionsort_rsorted_basic_operation_count_list, c=(1, 0, 0), alpha=.5, marker="<",label = "selection")
    plt.scatter(n_range, insertionsort_rsorted_basic_operation_count_list, c=(0, 1, 0), alpha=1, marker="o", label="insertion") 
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
                print("euclid_GCD(m, n) where m(fib(k+1)) is %d and n(fib(k)) is %d equals %d" %(fib(k+1)[0], fib(k)[0], euclid_GCD(fib(k+1)[0], fib(k)[0])[0])) #; print(euclid_GCD(fib(k+1)[0], fib(k)[0]))
                print("Task 1 Completed!")
            if task == 2:
                a = int(input(" --\nPlease enter a value for a: "))
                n = int(input("Please enter a value for n: "))
                print("exp_1: %d" %exp_1(a, n)[0])
                print("exp_2: %d" %exp_2(a, n)[0])
                print("exp_3: %d" %exp_3(a, n)[0])
                # print("exp_1:"); print(exp_1(a, n)[0])
                # print("exp_2:"); print(exp_2(a, n)[0])
                # print("exp_3:"); print(exp_3(a, n)[0])
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
                    A_of_k.append(euclid_GCD(fib(k[i] + 1)[0], fib(k[i])[0])[1])
                    '''
                k_range = list(range(0, 25))
                fib_basic_operation_count_list = []
                list_of_fibs = []
                for i in range(0,25):
                    fib_basic_operation_count_list.append(fib(i)[1])
                    list_of_fibs.append(fib(i)[0])
                # Plot
                plt.scatter(k_range, fib_basic_operation_count_list, s = np.pi * 35, c = (1, 0, 0), alpha = 1, marker="o")
                plt.title("Fibonacci Sequence")
                plt.xlabel("Input Size K")
                plt.ylabel("Number of Operations")
                plt.show()

                #ecluid
                gcd_basic_operation_count_list = []
                i = 0
                while i < len(list_of_fibs)-1:
                    gcd_basic_operation_count_list.append(euclid_GCD(list_of_fibs[i], list_of_fibs[i+1])[1])
                    i+=1
                print(len(gcd_basic_operation_count_list))
                print(len)
                # Plot
                euclid_range = list(range(0, len(gcd_basic_operation_count_list)))
                plt.scatter(euclid_range, gcd_basic_operation_count_list, s = np.pi * 35, c = (1, 0, 0), alpha = 1, marker="o")
                plt.title("Euclids algorithm asymptotic complexity".title())
                plt.xlabel("Input Size N")
                plt.ylabel("Number of Operations")
                plt.show()
                # --
            if task == 2:
                # Create Data
                a = 2                                       # Choose value for a. I chose 2 because it is most prevelant in my education.
                n = list(range(1, 24))            # Initialize a list containing values for n that will be shown on the x-axis.
                exp_1_a_to_n = []                 # Initialize an empty list the same size as n representing the y-axis.
                exp_2_a_to_n = []
                exp_3_a_to_n = []
                
                for i in range(len(n)):                     # Populate empty list with the number of operations for each of the values for n... for each method of exponentiation.
                    exp_1_a_to_n.append(exp_1(a, n[i])[1])       # Method 1: exp_1(a, n)
                    exp_2_a_to_n.append(exp_2(a, n[i])[1])       # Method 2: exp_2(a, n)
                    exp_3_a_to_n.append(exp_3(a, n[i])[1])       # Method 3: exp_3(a, n)
                # Plot
                plt.title("Computing a^n")
                plt.xlabel("Input Size n")
                plt.ylabel("Number of Operations")
                # s=np.pi * 100, ... s=np.pi * 25, ...  s=np.pi * 100
                plt.scatter(n, exp_1_a_to_n, s=np.pi * 100, color = "green", alpha=1, marker="<", label="exp_1")   # plot / scatter for method 1 (exp_1)
                plt.scatter(n, exp_2_a_to_n, s=np.pi * 25, color = 'red', alpha=1, marker="o", label="exp_2")     # plot / scatter for method 2 (exp_2)
                plt.scatter(n, exp_3_a_to_n, s=np.pi * 100, color = 'blue', alpha=.20, marker=">", label="exp_3")   # plot / scatter for method 3 (exp_3)
                plt.legend(loc='upper left', shadow=True, fontsize='x-large')
                plt.show()
            if task == 3:
                # plot scatter graphs
                print_sets()
                ## ----
            task = int(input(task_prompt))
    mode = int(input(mode_prompt))
