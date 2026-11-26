# ترتیب ذخیره میشود
# ایندکس دارد
# قابل تغییر است - mutable
# مقدار تکراری مجاز است
# مقادیر با انواع نوع ها مجاز است

import copy  # for copy

our_list = ["Computer", "Laptop", "Hand", "Video", "Dog"]

# ---------------------------------------------------Add item to list
our_list.append("Car")  # یک آیتم به آخر لیست
our_list.insert(2, "Tablet")  # اضافه کردن یک عنصر در اندیس مشخص
# مقدار را در صورت iterable بود هر عنصر را جدا اضافه میکند
our_list.extend("Book")
# ^^^^^^^^^ -> 'B', 'o', 'o', 'k'
# our_list.extend(["Book"]) -> فقط Book را وارد میکند

# لیست ورودی به عنوان یک آبجکت به لیست قبل درجا اضافه میشود
our_list.append(["Mobile", "Tee"])
our_list.extend(["TV", "Fish"])  # هر آیتم به صورت یک عنصر جدا اضافه میشود

print(our_list)
# ---------------------------------------------------Change the value
our_list[3] = "Bus"

print(our_list)
# ---------------------------------------------------Remove item from list or delete list
our_list.remove("Car")  # حذف آیتم بر اساس مقدار
last_item = our_list.pop()  # آیتم آخر را حذف و برمی گرداند
one_item = our_list.pop(1)  # آیتم اندیس ورودی را حذف و برمی گرداند

del our_list[3]  # آیتم اندیس ورودی را پاک میکند
del our_list[2:4]  # حذف ایتم های بازه اندیس ورودی

print(our_list)

our_list.clear()  # تمام آیتم های لیست را پاک میکند و خالی میشود
del our_list  # به طور کلی لیست از بین میرود
# ---------------------------------------------------Information and Searching
nums = [5, 8, 6, 12, 8, 2, 1, 3, 4, 7, 9, 10, 18]

nums_length = len(nums)  # تعداد عناصر لیست را برمی گرداند
number_of_repeat = nums.count(8)  # تعداد تکرار آیتم ورودی را برمی گرداند
search = nums.index(6)  # دنبال اولی آيتم برابر با ورودی میگردد

nums_max = max(nums)  # بزرگ ترین عدد لیست را برمیگرداند
nums_min = min(nums)  # کوچک ترین عدد لیست را برمیگرداند
nums_sum = sum(nums)  # جمع مقادیر لیست را برمیگرداند

list_have_12 = 12 in nums  # برسی میکند آیا آيتم در لیست هست یا نه
# ---------------------------------------------------Slicing
start, stop, step = 1, 6, 1
my_slice = nums[start:stop:step]  # start <= x < stop with step

# زمان معکوس کردن باید شروع از پایان کوچک تر باشد
start, stop, step = len(nums), 1, 1
# با گام منفی لیست به صورت معکوس با گام ذکر شده در بازه مشخص شده جدا میشود
reverse_nums = nums[start: stop:-step]

start, stop, step = 0, 2, 1
nums_without_two_item_of_last = nums[start:-stop:step]
# ---------------------------------------------------Sorting and Reverse
sorted_nums = sorted(nums)  # مرتب شده لیست ورودی را برمیگرداند
nums.sort()  # مستقیم لیست را مرتب میکند

# مرتب و معکوس لیست ورودی را برمیگرداند
reversed_nums_with_sorted = sorted(nums, reverse=True)
nums.sort(reverse=True)  # لیست را مستقیم مرتب و معکوس میکند
nums.reverse()  # لیست را مستقیم فقط معکوس میکند و مرتب نمیکند
# ---------------------------------------------------Copy list
my_list = [1, 2, [1, 2], [1, 2]]
# کپی نمیشود. درواقع هر دو نام به یک مقدار اشاره میکنند. با تغییر هر یک دیگری هم تغییر میکند.
my_list2 = my_list
# به صورت shallow و مستقل کپی میشوند. اما اگر لیست تو در تو باشد. لیست های داخل همچنان یکی است
my_list2 = my_list.copy()

my_list2 = copy.deepcopy(my_list)  # کپی کاملا مستقل حتی با وجود لیست تو در تو

print(my_list is my_list2)  # برسی میکند که آيا هر دو اسم یکی هستند یا خیر
# ---------------------------------------------------Reference vs In-place
a = [1, 2, 3]
b = a  # هر دو به یک لیست اشاره میکنند

b += [4]  # لیست اشاره شده توسط هر دو نام درجا تغییر میکند
b.append(5)  # خود مقدار درجا به لیست اضافه میشود
b.append([1, 2])  # لیست درجا به لیست قبل اضافه میشود
# هر یک از عناصر را به صورت جدا یا تنها مقدار ورودی را درجا اضافه میکند
b.extend([6, 7])
b.insert(0, "x")    # اندیس 0، مقدار "x"
b[3] = 425  # مقدار درجا در لیست تغییر میکند
# ^^^^^^^^^^ -> هر دو لیست در حالت های بالا یکسان خواهد بود و باهم تغییر میکنند

b = b + [8]  # یک لیست جدید ساخته شده با نام b
b = b.copy()  # لیست به جز لیست های تو در تو  کاملا از هم مستقل میشوند
b = [586, 482]  # کاملا یک لیست دیگه وصل خواهد شد
# ^^^^^^^^^^ -> هر دو لیست در حالت های بالا کاملا مستقل از هم خواهند بود

# ---------------------------------------------------Errors

# list.remove() -> ValueError
# empty_list.pop() -> IndexError
# python is case-sensitive -> Computer != computer
# list_has_no_5.index(5) -> ValueError
# list_with_string_and_number.sort() -> TypeError
# sorted(list_with_string_and_number) -> TypeError
# list = list + (5, 4) -> TypeError    _    list += (4, 5) -> it's ok
# list.insert(0) -> TypeError
# list_with_3_object[100] -> IndexError
