def say_hello(say_hi_func):
  print("Hello")
  
  say_hi_func()

def say_hi():
  print("Hi")
  
say_hello(say_hi)
