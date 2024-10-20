############################################
# Learn Commad Line
# https://www.youtube.com/watch?v=JVs2Ywy7wGQ&list=PLDoPjvoNmBAxzNO8ixW83Sf8FnLy_MkUT
############################################
print(type([1, 2, 3, 4, 5, 6]))  # list => List

print(type((1, 2, 3, 4, 5, 6)))  # tuple => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict =>Dictionary

#################################################
# Escape Sequences Characters
# \b => Back Space
# \newline  = > Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value
#################################################


# Back space
print("Hello\bWorld")  # Will Remove o

# Escape New Line + \
print(
    "Hallo \
      I love \
      Python"
)

# Escape Back Slash
print("I love Back Slash \\")

# Escape Single Quotes
print("I love Back Slash 'Test' ")

# Escape Double Quotes
print('I love Back Slash "Test" ')

# Line Feed
print("Hallo Welt\nSecond Line")

# Carriage Return
print("123456\rAbcd")

# Horizontal Tab
print("Hallo\tPython")

# \xhh => Character Hex Value
print("\x4F\x73")
