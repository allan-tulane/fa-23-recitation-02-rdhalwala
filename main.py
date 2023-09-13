"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
  #base
  if n <= 1:
    return 1
    
  #recall and assign to work untill it hits 1. Also make sure I return integers and not something like 2.5
  else:
    rec_work = a * simple_work_calc(n//b, a, b) + n
  #this should factor in integerness
    return rec_work
	
  """Compute the value of the recurrence W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
  #what does pass mean
	#pass

def work_calc(n, a, b, f):
  #base
  if n == 1: 
    return 1

  # n > 1
  return a * work_calc(n // b, a, b, f) + f(n)
    

  
  """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	#pass

def span_calc(n, a, b, f):
  #base
  if n == 1: 
    return 1

  # n > 1
  return span_calc(n // b, a, b, f) + f(n)
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""




def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):

	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result
  
  """
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
  #call work_calc for work_fn1 and 2 
  #use 2 for a and b
  #write for loop for different sizes
  #work_calc()


#Write a compare_span function
def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):

  result = []
	for n in sizes:
		#compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
	return result
  
  """
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
  def work_fn1(n):
    work_calc(n, 2, 2, lambda n: n)
	# create work_fn2
  def work_fn2(n):
    work_calc(n,2,2, lambda n: n*n)


  #Make two functions

  res = compare_work(work_fn1, work_fn2)
  print(res)

def test_compare_span():
  # span_fn2
  def span_fn1(n):
    span_calc(n, 2, 2, lambda n: n)
	# create span_fn2
  def span_fn2(n):
    span_calc(n,2,2, lambda n: n*n)

  res = compare_span(span_fn1, span_fn2)
  print(res)

