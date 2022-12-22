# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int
import random
nums1 = [1,2,3,4,5]
print(nums1)
nums2 = nums1
for i in range(0, len(nums1)-1):
    index = random.randint(0, len(nums1)-1)
    temp = nums1[i]
    nums1[i] = nums2[index]
    nums2[index] = temp
print(nums2)