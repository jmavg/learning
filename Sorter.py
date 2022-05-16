
# import sys

# to_sort = sys.argv[1]


list1 = [5,1,3,6,5,4,200,7,50]
expectation = sorted(list1)
list2 = []


def sorter(to_sort) -> list:

  holder = int

  while len(to_sort) > 0:

    holder = to_sort[0]

    for number in to_sort:

      if holder > number:

        holder = number

    to_sort.pop(to_sort.index(holder))

    list2.append(holder)

  return list2


if __name__ == "__main__":
  print(sorter(list1))
  print(expectation)
