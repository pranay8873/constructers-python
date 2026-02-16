def hifr(fun):
  def hfun(*args,**kwargs):
    print("HI FRIENDS")
    fun(*args,**kwargs)
    print("BYE FRIENDS")
  return hfun
@hifr
def add(a,b):
  print(f"SUM OF {a} AND {b} IS {a+b}")
add(1,2)
add(5,7)