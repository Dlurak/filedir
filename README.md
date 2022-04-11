# Filedir

Filedir is a python module to work with files and directories.

## Installation

It's strongly recommended to install the package via pip

```bash
pip3 install filedir
```

## File

This is a class to work with files. You can define an instance with

```python
File('full or relative path to your file')
```

If the path doesn't exist it will raise a *FileNotFoundError* if the path points to a directory or to a symbolic link it will also raise a *FileNotFoundError* 

### Basic data

To get the Basic data of the file call the variable that is in the table descriped.

| Variable name       | data                                                         |
| ------------------- | ------------------------------------------------------------ |
| File.fullpath       | Get the full path of the file.                               |
| File.name           | Get the name of the file(e.g. *README.md*)                   |
| File.basename       | Get the name of the file without the file extension(e.g. *README*) |
| File.ext            | Get the extension of the file(e.g. *.md*)                    |
| File.dir            | Get the directory where the file is in                       |
| File.size_b         | Get the size of the file in byte                             |
| File.size_kb        | Get the size of the file in kilo byte. You can replace the kb with the following abbreviations: *b*, *kb*, *mb*, *gb*, *tb*, *pb*, *eb*, *zb*, *yb* |
| File.size_preffered | Get the size of the file in the preffered size. It's a string containing the size + the unit(e.g. 100kb) |
| File.is_readable    | A boolean that shows if the file is readable, also works for: *is_writable*, *is_executable*, *is_hidden* |

### Methods

There are various methods on the file object, all of which are explained in more detail in the table below.

| Method name                    | description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| File.move(destination)         | To move the file you can run this the destination parameter must be a string or a Directory object. |
| File.copy(destination)         | To copy the file you can run this the destination parameter must be a string or a Directory object |
| File.delete()                  | This method will delete the file, the variable in which the object was contained is set to None. |
| File.read(lines, binary)       | This method will read the content of a file, lines and binary are bools, when set to true lines will return the content of the file in a array instead of a string, when binary is set to true the file get readed in binary mode |
| File.append(text)              | This method will append a text which must be a string to the file |
| File.rename(new_name)          | This method will rename the file to the *new_name* which must be a string |
| File.sort(destination, rename) | This method will sort the file, in the *extensions.json* file are all the paths described(e.g. test.txt -> text/text_files/test.txt), by default destination is the current directory of the file, this parameter describe where the base folder of the sorting is. The rename parameter indicates whether the file will be renamed if a file with the same name already exists at the destination (e.g. test.txt -> test(6).txt). |

### Operators

The File Object supports this operators:

| Operator | Description                                                  |
| -------- | ------------------------------------------------------------ |
| ==       | Compares the object with the other one, if the other one is not a File object it raises an error. |
| !=       | The same as above but inverted                               |
| <        | Compares the size of the file with the size of the other file, if the other object isn't a file it raises an error |
| >        | The same as above but inverted                               |
| >=       | Compares the size of the file with the size of the other file if the other object isn't a file it raises an error |
| <=       | The same as above but again inverted                         |

### Other methods

The following built in methods work also on this object:

| Method | Description                                               |
| ------ | --------------------------------------------------------- |
| str    | Converts the object into a string, it return the fullpath |
| repr   | Same as above                                             |
| hash   | It returns the hash of the fullpath                       |

## Directory

This is the class for Directories.

```python
Directory('The full or the relative path to a Directory')
```

### Basic data

| Variable name            | description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| Directory.fullpath       | The full path of the directory                               |
| Directory.name           | The name of the directory                                    |
| Directory.dir            | The directory where the directory is located                 |
| Directory.size_b         | The size of the directory in byte. You can replace the b with the following abbreviations: *b*, *kb*, *mb*, *gb*, *tb*, *pb*, *eb*, *zb*, *yb*. When it don't have the rights for an subfolder it will ignore that one, this is the reason why it isn't 100% correct in evry folder. |
| Directory.size_preferred | A string of a number + the abbreviations of the preferred size, it will be the unit where the the number is the biggest but still smaller than 1024 |

### Methods

| Method                               | description                                                  |
| ------------------------------------ | ------------------------------------------------------------ |
| Directory.move(desination)           | This will move the Directory to the destination, which must be a string or a directory object. |
| Directory.rename(name)               | This will rename the Directory to *name* which must be a string |
| Directory.copy(destination)          | This will copy the Directory to the destination which must be a string or a directory object. |
| Directory.delete()                   | This will delete the Directory, also evrything inside it will be deleted. |
| Directory.create_file(name, content) | This will create a file with the *name* and with *content*. By default *content* is set to none both arguments must be a string. |
| Directory.create_directory(name)     | This will create a directory. *Name* must be a string        |
| Directory.get_files()                | This will return a list of *File* objects                    |
| Directory.get_directories()          | Same as above but with Directories                           |

### Operators

| Operator | description                                                  |
| -------- | ------------------------------------------------------------ |
| ==       | Compares the full path of it selfs with the full path of the other directory if the other one isn't a directory it raises an error |
| !=       | Same as above but inverted                                   |
| <        | Compares the size of the Directory with the size of the other one |
| >        | Same as above but again inverted                             |
| =>       | Compares the size of the Directory with the size of the other one |
| =<       | Again the same thing but inverted                            |

### get item

With the [] operator you can get the items of a directory(similar to a dictionary). It will return a *File* or a *Directory* object, as shown in the code block under this text.

```python
#test_folder
#	-test.txt
#	-test_folder2
#		-test2.txt
Directory('test_folder')['test_folder2']['test2.txt']
```

### Other methods

| Method  | description                                                  |
| ------- | ------------------------------------------------------------ |
| str     | This will convert it to a string. It returns the fullpath    |
| repr    | Same as above                                                |
| iter    | This allows to loop though it in a loop with *for i in Directory('sth')* i will be the elements in the directory |
| len     | It will return the number of elements in the Directory       |
| contain | This allows to do something like this: *boolean = File(path) in Directory(path)* |
| hash    | This will return the hash value of the fullpath              |

