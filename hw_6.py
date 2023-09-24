def bubble_sort(num):
  n = len(num)

  for i in range(n):
    for j in range(0, n - i - 1):
      if num[j] > num[j + 1]:
        num[j], num[j + 1] = num[j + 1], num[j]
  return num

num = [6, 9, 5, 2, 8, 4, 3, 7, 1]
bubble_sort(num)
print("отсортированный список", bubble_sort(num))


def bubble_sort(val, a):
  resultOk = False
  first = 0
  last = len(a) - 1
  pos = -1
  while first < last:
    mid = (first + last) // 2
    if val == a[mid]:
      first = mid
      last = mid
      resultOk = True
      pos = mid
    elif val > a[mid]:
      first = mid + 1
    else:
      last = mid - 1
  if(resultOk):
    print("Элемент найден")
    print(pos)
  else:
    print("Элемент не найден")

bubble_sort(2, [1, 3, 4, 5, 6, 7, 8])
