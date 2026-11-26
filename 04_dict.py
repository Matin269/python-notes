# مجموعه ای از کلید مقدار ها
# کلید ها نمیتوانند تکراری باشند
# اگر کلید تکراری داشته باشیم مقدار کلید اخرین مقدار داده شده است
# کلید باید تغییر ناپذیر باشه مثل رشته عدد و تاپل

# ---------------------------------------------------Make and read
from collections import Counter
from collections import defaultdict
import copy
student = {
    "name": "Matin",
    "age": 19,
    "city": "Tehran",
    "job": "Programmer"
}

print(student["name"])  # اگر کلید وجود نداشته باشه ارور میدهد
print(student.get("age"))  # اگر کلید وجود نداشته باشد ارور نمیدهد و None میدهد
# اگر کلید نباشد متن وارد شده را نمایش میدهد
print(student.get("x", "Key Invalid"))
# ---------------------------------------------------Add, Change, Delete
student["family"] = "Babakhani"  # یک کلید و مقدار جدید اضافه میشود
student["age"] += 1  # به مقدار سن یکی اضافه میشود
del student["family"]  # کلید مقدار رو حذف میکند
# مقدار کلید وارد شده را از دیکشنری حذف و خروجی میدهد
one = student.pop("city")
# اگر کلید داده شده وجود نداشته باشد متن داده شده را برمیگرداند
example = student.pop("s", "nadarad")
last = student.popitem()  # اخرین ردیفی که اضافه شده را حذف و برمیگرداند
# student.clear() کل مقادیر رو پاک میکنه و خود دیکشنری خالی باقی میماند
# ---------------------------------------------------Scroll and Loop
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, "->", value)
# ---------------------------------------------------Key and Values in list
keys = student.keys()  # فقط کلید ها
values = student.values()  # فقط مقدار ها
print(type(keys))

keys_list = list(student.keys())  # لیست کلید ها
values_list = list(student.values())  # لیست مقدار ها
print(type(keys_list))
# ---------------------------------------------------Key Check
key_exist = "name" in student
value_exist = "Matin" in values_list
# ---------------------------------------------------Update
new_student = {"age": 23, "favorite_movie": "Naruto"}
student.update(new_student)
student.update(name="MohammadMatin")  # روش کوتاه تر
print(student)  # کلید های موجود مقدار جدید کلید مقدار های جدید اضافه میشوند
# ---------------------------------------------------SetDefault
user = {"name": "Matin"}
# اگر کلید و مقدار وجود داشته باشد مقدار اصلی را نمایش میدهد
print(user.setdefault("name", "User"))
# اگر کلید و مقدار نباشد آن را اضافه میکند و نمایش میدهد
print(user.setdefault("job", "Programmer"))
# ---------------------------------------------------Nested Dict
users = {
    "Ali": {"age": 20, "city": "Hamedan"},
    "Matin": {"age": 19, "city": "Tehran"},
    "Parsa": {"age": 26, "city": "Tehran"}
}
print(users["Matin"]["age"])
users["Ali"]["age"] -= 1
users["Reza"] = {"age": 16, "city": "Mashhad"}
# ---------------------------------------------------Dict Comprehension
squares = {}
for x in range(1, 4):
    squares[x] = x ** 2
#  |
#  |
#  V
squares2 = {i: i ** 2 for i in range(1, 4)}
# ----
score = {"Math": 18, "Physics": 13, "English": 17}
good = {k: v for k, v in score.items() if v > 15}
# ---------------------------------------------------Copy
a = {"name": "Ali", "Score": [1, 2]}
b = a.copy()
b["name"] = "Sara"
b["Score"].append(3)

print(a)
print(b)


c = copy.deepcopy(a)
c["Score"].append(4)

print(c)
# ---------------------------------------------------DefaultDict
# تعیین میکنه مقادیر این دیکشنری همه از نوع اینت هستند
count = defaultdict(int)
for ch in "banana":
    count[ch] += 1
print(dict(count))
# ----
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
group = defaultdict(list)
for w in words:
    group[w[0]].append(w)
print(dict(group))
# Note!
d = defaultdict(int)
print(d["x"])     # 0
print(d)          # defaultdict(<class 'int'>, {'x': 0})
# حتی یک بار خواندن مقدار اون رو میسازه پس از in استفاده میکنیم
# ---------------------------------------------------Counter
f = Counter("banana")
print(f)
print(f["v"])  # خطا نمیدهد
print(f.most_common(2))  # بیشترین تکرار را برمیگرداند
# -----
votes = ["ali", "sara", "ali", "reza", "ali", "sara"]
result = Counter(votes)
print(result.most_common(1))    # [('ali', 3)]
# ---------------------------------------------------Error
# d["b"] -> KeyError (کلید وجود ندارد)
# d.pop("b") -> KeyError (کلید وجود ندارد)
# {[1, 2]: "x"} -> TypeError (unhashable)
# {{1: 2}: "x"} -> TypeError (unhashable)
# {}.popitem() -> KeyError (دیکشنری خالی)
# d.keys()[0] -> TypeError (ایندکس ندارد)
# for k in d: del d[k] -> RuntimeError (تغییر اندازه وسط حلقه)
# d("name") -> TypeError (not callable. باید d["name"] باشه)
# d[name] -> NameError (کوتیشن فراموش شده)
# d = d.update({"a": 1}) -> d میشه None (update چیزی برنمیگردونه)
# s = {} -> دیکشنری است، نه ست
# b = a -> کپی نشده و فقط دو اسم به یک دیکشنری اشاره میکنند
# b = a.copy() -> کپی سطحی. لیست داخلی هنوز مشترکه
# {"a": 1, "a": 2} -> {'a': 2} (خطا نمیده و بی صدا بازنویسی میشه)
# defaultdict(int()) -> TypeError
# defaultdict(0) -> TypeError (باید defaultdict(int) باشه)
# d = defaultdict(int); d["x"] -> کلید x ساخته میشه (از in استفاده کن)
# sum = 0 / dict = {} / list = [] -> توابع آماده خراب میشن
# from collaction import Counter -> ModuleNotFoundError
# user.setDefault(...) -> AttributeError (حساس به حروف بزرگ و کوچک)
# Counter("abc")  بدون import -> NameError
