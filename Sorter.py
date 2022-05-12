
# import sys

# to_sort = sys.argv[1]


from tempfile import tempdir


list1 = [5,1,3,6,5,4,200,7,50]
expectation = sorted(list1)
list2 = []


def sorter(to_sort) -> list:

  temp = int

  for i in range(len(to_sort)):

    for index, number in enumerate(to_sort):

      if to_sort[i] > number:

        temp = number
        i = index
    to_sort.pop(temp)

    list2.append(temp)

  return list2


if __name__ == "__main__":
  print(sorter(list1))
  print(expectation)
