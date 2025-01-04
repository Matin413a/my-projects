#باز نویسی دستور print and input
import time
import builtins

# ذخیره توابع اصلی
original_print = builtins.print
original_input = builtins.input

# بازنویسی print
def slow_print(*args, sep=' ', end='\n', delay=0.05, **kwargs):
    text = sep.join(map(str, args))
    for char in text:
        original_print(char, end='', flush=True)
        time.sleep(delay)
    original_print(end=end, flush=True)

# بازنویسی input
def slow_input(prompt='', delay=0.05):
    for char in prompt:
        original_print(char, end='', flush=True)
        time.sleep(delay)
    return original_input()

# جایگزینی توابع اصلی
builtins.print = slow_print
builtins.input = slow_input

# برنامه نمونه
name = input("نام خود را وارد کنید: ")
print(f"سلام، {name}!", delay=0.1)