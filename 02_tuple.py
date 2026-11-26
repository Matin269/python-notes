# ترتیب ذخیره میشود
# ایندکس دار هستند
# غیر قابل تغییر - immutable
# مقادیر تکراری مجاز است
# سریع و سبک تر از لیست ها
# تاپل میتواند کلید دیکشنری باشد - Hashable

our_tuple = ("Computer", "Laptop", "Phone", "Table", "Computer")

# ---------------------------------------------------Information
tuple_length = len(our_tuple)  # تعداد آیتم های تاپل
number_of_repeat = our_tuple.count("Computer")  # تعداد مقادیر تکراری
search = our_tuple.index("Computer")  # اولین عنصری که مقدارش با ورودی یکی است
our_tuple_have_phone = "Phone" in our_tuple  # ایا مقدار در تاپل است
# ---------------------------------------------------Single member
type((3))  # پرانتز با تک عضو برای گروه بندی کردن و اولویت محاسبات است
type((3,))  # کاما یک تاپل میسازد
t3 = 3,  # تاپل تک عضوی میشود
t4 = 3  # یک اینتیجر
# ---------------------------------------------------Slicing
start = 0
stop = 3
step = 1
our_tuple[start:stop:step]  # کاملا مشابه لیست است
# ---------------------------------------------------Change tuple value
our_tuple = list(our_tuple)
our_tuple[4] = "Fish"
our_tuple.append("Monitor")
our_tuple = tuple(our_tuple)
# تاپل جدید میسازد و تاپل را تغییر نمیدهد

# اول تاپل را به لیست تغییر میدهیم و مقادیر را تغییر میدهیم و سپس به تاپل تبدیل میکنیم
print(type(our_tuple))
# ---------------------------------------------------Combine tuples
t = (1, 2, 3, 4)

t = t * 2
new_tuple = our_tuple + t  # مجاز است چون یک تاپل جدید میسازد

print(new_tuple)
# ---------------------------------------------------Unpacking
x, y, w, v, g, h = our_tuple  # هر عضو به ترتیب جدا شده در یک متغییر
# سه عنصر اول در متغییر جدا و باقی مقادیر به صورت لیست در متغییر آخر
q, e, r, *i = new_tuple
p, *o, k = new_tuple  # عنصر اول و اخر جدا در متغییر و باقی در متغییر جدا به صورت لیست
# ---------------------------------------------------Swap
a = 1
b = 2
a, b = b, a  # مقادیر را جا به جا میکند
# ^^^^^^^ -> مقادیر سمت راست به یک تاپل تبدیل میشود و جدا جدا در متغییر سمت چپ قرار میگیرد
# ---------------------------------------------------+= in tuple
x1 = (1, 2)
x2 = x1
x2 += (5,)  # در تاپل += مانند + عمل میکند و تاپل جدید میسازد

print(x1, x2)
# ---------------------------------------------------Mutable object in tuple
t1 = ([1, 2], 4)
t1[0].append(3)  # لیست در تاپل قابل تغییر است

# ---------------------------------------------------Errors

# tuple_has_no_dog.index("dog") -> ValueError
# python is case-sensitive -> Computer != computer
# tuple.sort(),.pop(),.remove(),.insert(),.extend(),.append() -> AttributeError
# tuple[x] = y -> TypeError
# a, b = (1, 2, 3) -> ValueError
# del tuple[0] -> TypeError
