"""
20250828ClassDemo.py
====================================
This demonstrates built in data structures and control commands in Python

| Author: Seth McNeill
| Date: 2025 August 28
"""

def myUpperCase(myString):
    """
    This converts a string to all uppercase

    Parameters
    --------
    myString : str
      A string to be made all uppercase
    
    Returns
    --------
    str
      An uppercase version of myString
    """
    return myString.upper()


if __name__ == "__main__":
    """
    Code inside this if statement will only run if called as a script
    not if it is imported
    """
    print("hello world")

    mStr = "This is 3 my test 5 String."
    print(mStr)
    uStr = myUpperCase(mStr)
    print(uStr)

    mySet = set(mStr)
    myList = list(mySet)
    type(mySet)
    type(myList)

    for n in range(len(mStr)):
      if n%2:  # odd numbered indexes
        print(mStr[n].lower(), end='')
      else:
        print(mStr[n].upper(), end='')
    print()

    for letter in mStr:
      if letter in 'aeiou':
        print(letter.upper(), end='')
      else:
        print(letter.lower(), end='')
    print()

    for letter in mStr:
      if letter in 'aeiou':
        print(letter.upper(), end='')
      elif letter in '1234567890':
        print('#', end='')
      else:
        print(letter.lower(), end='')
    print()
