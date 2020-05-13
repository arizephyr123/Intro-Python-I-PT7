"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# Note: If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it. If you don’t explicitly close a file, Python’s garbage collector will eventually destroy the object and close the open file for you, but the file may stay open for a while.
with open('foo.txt') as foo_file:
    read_foo = foo_file.read()
    print(read_foo)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar_file = open('bar.txt', 'w')
bar_file.write(
    "I fart in your general direction\nYour mother was a hamster and your father smelt of elderberries.\nTis' a flesh wound.")
bar_file.close()

# After a file object is closed, either by a with statement or by calling f.close(), attempts to use the file object will automatically fail. => ValueError: I/O operation on closed file.
bar_read = open('bar.txt', 'r')
print(bar_read.read())
