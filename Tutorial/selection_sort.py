'''
선택정렬
'''
def sel_sort(arr):
  n = len(arr)
  for i in range(0, n - 1):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)     # 정렬 과정 출력하기
 
arr = [1,10,8,3,6,9,7,4,5,2]
sel_sort(arr)
print('결과',arr)