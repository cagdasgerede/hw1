def sum(array):
  """Computes the total sum of elements of given array."""
  if array is None:
    return 0
 
  total = 0
  for i in array:
    total = total + i
  return total
