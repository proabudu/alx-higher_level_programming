def no_c(my_string):
   """Removes all characters 'c' and 'C' from a string without using imports or str.replace()."""

   result = ""
   for char in my_string:
       if char not in "cC":
           result += char
   return result
