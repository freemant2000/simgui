def prepare(b):
  b.title="python"
  b.price=24
  a=Author()
  a.name="John"
  b.author=a

def use(b):
  print(b.author.name)

class Book:
  pass

class Author:
  pass

b1=Book()
prepare(b1)
use(b1)
