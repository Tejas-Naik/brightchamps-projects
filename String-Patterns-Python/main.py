'''STAR TRIANGLE:'''
# n = int(input("Enter number of rows: "))
# for i in range(1, n + 1):
#   print("* " * i)


'''PYRAMID PATTERN'''
# n = int(input("Enter number of rows: "))
# for i in range(1, n + 1):
#   spaces = " " * (n - i)
#   asterisks = "* " * i
#   print(spaces + asterisks)


''' CHARACTER PRINTER '''
# for unicode in range(65,91):
#   print(chr(unicode))


''' ALPHABET ASCENDER '''
# n = int(input("Enter the number of rows: "))
# start_unicode = 65  # ASCII code for 'A'

# for i in range(1, n + 1):
#   for j in range(i):
#     letter = chr(start_unicode)
#     print(letter, end=" ")
#     start_unicode += 1
#   print()


''' SUBSTRING BUILDER '''
name = input("Enter a string: ")

for i in range(1, len(name) + 1):
  substring = name[:i]
  spaced_substring = ' '.join(substring)
  print(spaced_substring)


