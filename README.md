# pyfileutil
A Python file utility for the creation, copying, deletion, moving, and opening of 
a single file, and aid in the creation of IOTextWrapper objects.

## Inspired by the .NET Framework

Inspired by the .NET Framework's System.IO.File static class, this Python module
provides a class with static methods for the creation, copying, deletion, moving,
and opening of a single file, and aids in the creation of IOTextWrapper objects.

Furthermore, it provides more utility methods for enumerating files in directories
and transforming the contents of files to Python dictionaries.

## An object-oriented approach to file management

The `fileutil` module aims to adopt an object-oriented approach to file management
within Python and further leverage the open function by eliminating the use of 
literal open modes.

## The File class

It contains 19 public static methods and one "private" static helper method to 
ensure internal constraints' enforcement.

### Static Methods

The class's interface exposes the following static methods:

- `enumerate`: Recursively list directories and pass each file to the callback.
- `append_all_lines`: Append lines to a file by using a specified encoding, and 
        then close the file. If the specified file does not exist,
        this method creates a file, writes the specified lines to the
        file, and then closes the file.
- `append_all_text`: Append the specified string to the file using the 
        specified encoding, creating the file if it does not already
        exist.
- `openread`: Open a TextIOWrapper on the specified path in read mode.
- `openread_binary`: Open a TextIOWrapper on the specified path in binary read mode.
- `openwrite_binary`: Open an existing file or create a new file for writing in
        binary mode.
- `read_all_bytes`: Open a binary file, read the contents of the file into a
        byte array, and then close the file.
- `read_all_text`: Open a file, read all text in the file with the specified
        encoding, and then close the file.
- `readlines`: Open a file, read all lines of the file with the specified
        encoding, and then close the file.
- `write_all_bytes`: Create a new file, write the specified byte array to the
        file, and then close the file. If the target file already exists, it is 
        overwritten.
- `write_all_text`: Create a new file, write the specified string to the file
        using the specified encoding, and then close the file. If the
        target file already exists, it is overwritten.
- `write_all_lines`: Create a new file by using the specified encoding, write a
        collection of strings to the file, and then close the file.
- `delete`: Delete the specified file.
- `exists`: Determine whether the specified file exists.
- `copy`: Copy an existing file to a new file. Overwriting a file of the same name
        is allowed.
- `move`: Move a specified file to a new location, providing the
        options to specify a new file name and to overwrite the
        destination file if it already exists.
- `histogram`: Open the specified file in read mode, count the
        occurrence of each word it contains, and return a dictionary.
- `words`: Open the specified file in read mode, add each word it
        contains to a dictionary, and return it.


