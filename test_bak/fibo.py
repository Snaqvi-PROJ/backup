def fib(ran):
  """ 0,1,1,2,3,5,8 """
  result = [0]
  num = 0
  num2 = 1
  for start in range(num2, ran):
    num3 = num + num2
    num = num2
    num2 = num3
    result.append(num3)

  return(result)
