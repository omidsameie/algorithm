def merge_sort(list):
  m = len(list)
  if m==1:
    return list
  mid = m//2
  left = merge_sort(list[:mid])
  right = merge_sort(list[mid:])
  return merge(left, right)
def merge(left, right):
  output = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      output.append(left[i])
      i +=1
    else:
      output.append(right[j])
      j +=1
  output.extend(left[i:])
  output.extend(right[j:])
  return output
def run_merge_sort():
  unsorted_list = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
  print(unsorted_list)
  sorted_list = merge_sort(unsorted_list)
  print(sorted_list)
run_merge_sort()
