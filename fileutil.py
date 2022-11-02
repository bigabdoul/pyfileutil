import os
from typing import Iterable
from string import whitespace, punctuation

class File:
    """Provide static methods for the creation, copying, deletion,
    moving, and opening of a single file, and aid in the creation
    of IOTextWrapper objects.
    """

    @staticmethod
    def enumerate(callback, dirname: str = None):
        """Recursively list directories and pass each file to the
        callback.

        :param callback function: A function to call back each time
        a file is found.
        :param dirname str: The name of the directory to search. If
        None, the current working directory is used.
        """
        if not dirname: dirname = os.getcwd()
        for name in os.listdir(dirname):
            path = os.path.join(dirname, name)
            if os.path.isfile(path):
                callback(path)
            else:
                File.enumerate(callback, path)

    @staticmethod
    def append_all_lines(path: str, contents: Iterable[str], encoding: str = None):
        """Append lines to a file by using a specified encoding, and 
        then close the file. If the specified file does not exist,
        this method creates a file, writes the specified lines to the
        file, and then closes the file.

        :param path str: The file to append the lines to. The file is
        created if it doesn't already exist.
        :param contents Iterable[str]: The lines to append to the file.
        :param encoding str: The character encoding to use.
        """
        with open(path, 'a', encoding=encoding) as f:
            f.writelines(contents)
    
    @staticmethod
    def append_all_text(path: str, contents: str, encoding: str = None):
        """Append the specified string to the file using the 
        specified encoding, creating the file if it does not already
        exist.

        :param path str: The file to append the specified string to.
        :param contents str: The string to append to the file.
        :param encoding str: The character encoding to use.
        """
        with open(path, 'a', encoding=encoding) as f:
            return f.write(contents)
    
    @staticmethod
    def openread(path: str, encoding: str = None):
        """Open a TextIOWrapper on the specified path in read mode.
        
        :param path str: The file to open.
        :param encoding str: The character encoding to use.
        """
        return open(path, 'r', encoding=encoding)

    @staticmethod
    def open_read_binary(path: str):
        """Open a TextIOWrapper on the specified path in binary read mode.
        
        :param path str: The file to open.
        """
        return open(path, 'rb')

    @staticmethod
    def openwrite(path: str, encoding: str = None):
        """Open an existing file or create a new file for writing.
        
        :param path str: The file to be opened for writing.
        :param encoding str: The character encoding to use.
        """
        return open(path, 'w', encoding=encoding)
    
    @staticmethod
    def openwrite_binary(path: str, encoding: str = None):
        """Open an existing file or create a new file for writing in
        binary mode.
        
        :param path str: The file to be opened for writing.
        :param encoding str: The character encoding to use.
        """
        return open(path, 'wb', encoding=encoding)

    @staticmethod
    def read_all_bytes(path: str) -> bytes:
        """Open a binary file, read the contents of the file into a
        byte array, and then close the file.

        :param path str: The file to open for reading.
        """
        with File.open_read_binary(path) as f:
            return f.read()

    @staticmethod
    def read_all_text(path: str, encoding: str = None):
        """Open a file, read all text in the file with the specified
        encoding, and then close the file.

        :param path str: The file to open for reading.
        :param encoding str: The encoding applied to the contents of the file.
        """
        with open(path, 'r', encoding=encoding) as f:
            return f.read()

    @staticmethod
    def readlines(path: str, encoding: str = None):
        """Open a file, read all lines of the file with the specified
        encoding, and then close the file.

        :param path str: The file to open for reading.
        :param encoding str: The encoding applied to the contents of the file.
        """
        with open(path, 'r', encoding=encoding) as f:
            return f.readlines()

    @staticmethod
    def write_all_bytes(path: str, contents: bytes):
        """Create a new file, write the specified byte array to the
        file, and then close the file. If the target file already
        exists, it is overwritten.

        :param path str: The file to write to.
        :param content bytes: The bytes to write to the file.
        """
        with open(path, 'wb') as f:
            return f.write(contents)

    @staticmethod
    def write_all_text(path: str, contents: str, encoding: str = None):
        """Create a new file, write the specified string to the file
        using the specified encoding, and then close the file. If the
        target file already exists, it is overwritten.

        :param path str: The file to write to.
        :param contents str: The string to write to the file.
        :param encoding str: The encoding to apply to the string.
        """
        with open(path, 'w', encoding=encoding) as f:
            return f.write(contents)

    @staticmethod
    def write_all_lines(path: str,  contents: Iterable[str], encoding: str = None):
        """Create a new file by using the specified encoding, write a
        collection of strings to the file, and then close the file.

        :param path str: The file to write to.
        :param contents Iterable[str]: The lines to write to the file.
        :param encoding str: The character encoding to use.
        """
        with open(path, 'w', encoding=encoding) as f:
            return f.writelines(contents)

    @staticmethod    
    def delete(*files):
        """Delete the specified file.
        
        :param files tuple: The name(s) of the file(s) to be deleted.
        """
        if isinstance(files, str):
            os.remove(files)
        else:
            for name in files: os.remove(name)

    @staticmethod
    def exists(path: str):
        """Determine whether the specified file exists.
        
        :param path str: The file to check.
        """
        return os.path.exists(path)
    
    @staticmethod
    def copy(srcpath: str, destpath: str, overwrite = False):
        """Copie an existing file to a new file. Overwriting a file
        of the same name is allowed.
        
        :param srcpath str: The file to copy.
        :param destpath str: The name of the destination file. This cannot be a directory.
        :param overwrite bool: True if the destination file can be overwritten; otherwise, False.
        """
        File._enforce_constraints_(srcpath, destpath, overwrite)

        with File.open_read_binary(srcpath) as fsrc:
            with File.openwrite_binary(destpath) as fdest:
                chunk_size = 512
                chunks_read = fsrc.read(chunk_size)
                while len(chunks_read):
                    fdest.write(chunks_read)
                    chunks_read = fsrc.read(chunk_size)

    @staticmethod
    def move(srcpath: str, destpath: str, overwrite = False):
        """Move a specified file to a new location, providing the
        options to specify a new file name and to overwrite the
        destination file if it already exists.

        :param srcpath str: The name of the file to move. Can include
        a relative or absolute path.
        :param destpath str: The new path and name for the file.
        :param overwrite bool: True to overwrite the destination file
        if it already exists; False otherwise.
        """
        File._enforce_constraints_(srcpath, destpath, overwrite)
        
        File.copy(srcpath, destpath, overwrite)
        File.delete(srcpath)

    @staticmethod
    def histogram(path:str):
        """Open the specified file in read mode, count the
        occurrence of each word it contains, and return a dictionary.
        
        :param path str: The file to read.
        """
        with open(path) as fin:
            dic = dict()
            for line in fin:
                for w in line.replace('-', ' ').split():
                    word = w.strip(punctuation + whitespace).lower()
                    if word: dic[word] = dic.get(word, 0) + 1
            return dic
        
    @staticmethod
    def words(path: str):
        """Open the specified file in read mode, add each word it
        contains to a dictionary, and return it.
        
        :param path str: The file to read.
        """
        with open(path) as fin:
            dic = dict()
            for line in fin:
                word = line.strip()
                if word: dic[word] = len(word)
            return dic

    @staticmethod
    def _enforce_constraints_(srcpath: str, destpath: str, overwrite: bool):
        """Make sure the source and destination paths are distinct, 
        and an existing file matching the destination path is not
        overwritten.

        :param srcpath str: The path to the source file.
        :param destpath str: The path to the destination file.
        :param overwrite bool: True to overwrite the destination file
        if it already exists; False otherwise.
        """
        if srcpath == destpath:
            raise IOError('Source and destination files cannot be identical.')

        if not overwrite and os.path.exists(destpath):
            raise IOError(f"The file '{destpath}' exists and cannot be overwritten.")