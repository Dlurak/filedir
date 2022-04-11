import os
import json
import shutil
with open(os.path.join(os.path.dirname(__file__), 'extensions.json'), 'r') as f:
    extensions = json.load(f)

class File:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        if not os.path.isfile(path):
            raise FileNotFoundError(f"{path} is not a file")
        self.fullpath = os.path.abspath(path)
        self.name = os.path.basename(self.fullpath)
        self.basename = os.path.splitext(self.fullpath)[0]
        self.ext = os.path.splitext(self.fullpath)[1]
        self.dir = os.path.dirname(self.fullpath)
        self.size_b = os.path.getsize(self.fullpath)
        self.size_kb = self.size_b / 1024
        self.size_mb = self.size_kb / 1024
        self.size_gb = self.size_mb / 1024
        self.size_tb = self.size_gb / 1024
        self.size_pb = self.size_tb / 1024
        self.size_eb = self.size_pb / 1024
        self.size_zb = self.size_eb / 1024
        self.size_yb = self.size_zb / 1024
        self.size_preferred = '0b'
        size = self.size_b
        for i in ["b", "kb", "mb", "gb", "tb", "pb", "eb", "zb", "yb"]:
            if size > 1024:
                size = size / 1024
            else:
                self.size_preferred = f"{size:.3f}{i}"
                break
        self.is_readable = os.access(self.fullpath, os.R_OK)
        self.is_writable = os.access(self.fullpath, os.W_OK)
        self.is_executable = os.access(self.fullpath, os.X_OK)
        self.is_hidden = self.name.startswith('.')
    def __str__(self):
        return self.fullpath
    def __repr__(self):
        return self.fullpath
    def __eq__(self, other):
        if not isinstance(other, File):
            raise TypeError(f"{other} is not a File object")
        return self.fullpath == other.fullpath
    def __hash__(self):
        return hash(self.fullpath)
    def __lt__(self, other):
        if not isinstance(other, File):
            raise TypeError(f"{other} is not a File object")
        self.size_b < other.size_b 
    def __le__(self, other):
        if not isinstance(other, File):
            raise TypeError(f"{other} is not a File object")
        return self.size_b <= other.size_b 
    def __gt__(self, other):
        if not isinstance(other, File):
            raise TypeError(f"{other} is not a File object")
        return self.size_b > other.size_b 
    def __ge__(self, other):
        if not isinstance(other, File):
            raise TypeError(f"{other} is not a File object")
        return self.size_b >= other.size_b 
    def __ne__(self, other):
        if not isinstance(other, File):
            raise TypeError(f"{other} is not a File object")
        return self.fullpath != other.fullpath
    def move(self, destination):
        if not os.path.exists(destination):
            raise FileNotFoundError(destination)
        if not os.path.isdir(destination):
            raise NotADirectoryError(f"{destination} is not a directory")
        if os.path.exists(os.path.join(destination, self.name)):
            raise FileExistsError(f"{os.path.join(destination, self.name)} already exists")
        if not os.access(destination, self.is_writable):
            raise PermissionError(f"{destination} is not writable")
        if not isinstance(destination, (str, Directory)):
            raise TypeError(f"{destination} is not a string or Directory object")
        if isinstance(destination, Directory):
            destination = destination.fullpath
        os.rename(self.fullpath, os.path.join(destination, self.name))
        self.fullpath = os.path.join(destination, self.name)
        self.dir = os.path.abspath(destination)
    def copy(self, destination):
        if not os.path.exists(destination):
            raise FileNotFoundError(destination)
        if not os.path.isdir(destination):
            raise NotADirectoryError(f"{destination} is not a directory")
        if os.path.exists(os.path.join(destination, self.name)):
            raise FileExistsError(f"{os.path.join(destination, self.name)} already exists")
        if not os.access(destination, self.is_writable):
            raise PermissionError(f"{destination} is not writable")
        if not isinstance(destination, (str, Directory)):
            raise TypeError(f"{destination} is not a string or Directory object")
        if isinstance(destination, Directory):
            destination = destination.fullpath
        os.copy(self.fullpath, os.path.join(destination, self.name))
        self.fullpath = os.path.join(destination, self.name)
        self.dir = os.path.abspath(destination)
    def delete(self):
        if not os.access(self.fullpath, self.is_writable):
            raise PermissionError(f"{self.fullpath} is not writable")
        os.remove(self.fullpath)
        self = None
    def read(self, lines=False, binary=False):
        if not self.is_readable:
            raise PermissionError(f"{self.fullpath} is not readable")
        mode = 'r'
        if bynary:
            mode += 'b'
        with open(self.fullpath, mode) as f:
            text = f.read()
            if lines:
                return text.split('\n')
            else:
                return text
    def write(self, text):
        if not self.is_writable:
            raise PermissionError(f"{self.fullpath} is not writable")
        if not isinstance(text, str):
            raise TypeError(f"{text} is not a string")
        with open(self.fullpath, 'w') as f:
            f.write(text)
        self.size_b = os.path.getsize(self.fullpath)
        self.size_kb = self.size_b / 1024
        self.size_mb = self.size_kb / 1024
        self.size_gb = self.size_mb / 1024
        self.size_tb = self.size_gb / 1024
        self.size_pb = self.size_tb / 1024
        self.size_eb = self.size_pb / 1024
        self.size_zb = self.size_eb / 1024
        self.size_yb = self.size_zb / 1024
        self.size_preferred = '0b'
        for i in ["b", "kb", "mb", "gb", "tb", "pb", "eb", "zb", "yb"]:
            if size > 1024:
                size = size / 1024
            else:
                self.size_prefferred = f"{size:.3f}{i}"
    def append(self, text):
        if not self.is_writable:
            raise PermissionError(f"{self.fullpath} is not writable")
        if not isinstance(text, str):
            raise TypeError(f"{text} is not a string")
        with open(self.fullpath, 'a') as f:
            f.write(text)
        self.size_b = os.path.getsize(self.fullpath)
        self.size_kb = self.size_b / 1024
        self.size_mb = self.size_kb / 1024
        self.size_gb = self.size_mb / 1024
        self.size_tb = self.size_gb / 1024
        self.size_pb = self.size_tb / 1024
        self.size_eb = self.size_pb / 1024
        self.size_zb = self.size_eb / 1024
        self.size_yb = self.size_zb / 1024
        self.size_preferred = '0b'
        for i in ["b", "kb", "mb", "gb", "tb", "pb", "eb", "zb", "yb"]:
            if size > 1024:
                size = size / 1024
            else:
                self.size_prefferred = f"{size:.3f}{i}"
    def rename(self, new_name):
        if not self.is_writable:
            raise PermissionError(f"{self.fullpath} is not writable")
        os.rename(self.fullpath, os.path.join(self.dir, new_name))
        self.name = new_name
        self.fullpath = os.path.join(self.dir, new_name)
    def sort(self, destination=None, rename=False):
        if destination is None:
            destination = self.dir
        if not self.is_writable:
            raise PermissionError(f"{self.fullpath} is not writable")
        if not isinstance(destination, (str, Directory)):
            raise TypeError(f"{destination} is not a string or Directory object")
        if not isinstance(rename, bool):
            raise TypeError(f"{rename} is not a boolean")
        if isinstance(destination, Directory):
            destination = destination.fullpath
        if not os.path.exists(destination):
            raise FileNotFoundError(destination)
        folders=[]
        try:
            folders = extensions[self.ext].split('/')
        except KeyError:
            folders = extensions['noname'].split('/')
        for folder in folders:
            if not os.path.exists(os.path.join(destination, folder)):
                os.mkdir(os.path.join(destination, folder))
            destination = os.path.join(destination, folder)
        if not rename or not os.path.exists(os.path.join(destination, self.name)):
            os.rename(self.fullpath, os.path.join(destination, self.name))
            self.fullpath = os.path.join(destination, self.name)
            self.dir = os.path.abspath(destination)
        elif rename:
            count = 1
            while os.path.exists(os.path.join(destination, self.name)):
                self.name = f'{self.basename}({count}).{self.ext}'
                count += 1
            os.rename(self.fullpath, os.path.join(destination, self.name))
            self.fullpath = os.path.join(destination, self.name)
            self.dir = os.path.abspath(destination)


class Directory:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        if not os.path.isdir(path):
            raise NotADirectoryError(f"{path} is not a directory")
        self.fullpath = os.path.abspath(path)
        self.name = os.path.basename(self.fullpath)
        self.dir = os.path.dirname(self.fullpath)
        self.size_b = 0
        try:
            for i in os.scandir(self.fullpath):
                if i.is_file():
                    self.size_b += i.stat().st_size
                elif i.is_dir():
                    self.size_b += Directory(i.path).size_b
        except PermissionError:
            self.size_b = 0
        except Exception:
            self.size_b = 0
        self.size_kb = self.size_b / 1024
        self.size_mb = self.size_kb / 1024
        self.size_gb = self.size_mb / 1024
        self.size_tb = self.size_gb / 1024
        self.size_pb = self.size_tb / 1024
        self.size_eb = self.size_pb / 1024
        self.size_zb = self.size_eb / 1024
        self.size_yb = self.size_zb / 1024
        self.size_preferred = '0b'
        size = self.size_b
        for i in ["b", "kb", "mb", "gb", "tb", "pb", "eb", "zb", "yb"]:
            if size > 1024:
                size = size / 1024
            else:
                self.size_prefferred = f"{size:.3f}{i}"
    def __str__(self):
        return self.fullpath
    def __repr__(self):
        return self.fullpath
    def __eq__(self, other):
        if isinstance(other, Directory):
            return self.fullpath == other.fullpath
        else:
            raise TypeError(f'{other} is not a Directory')
    def __ne__(self, other):
        if isinstance(other, Directory):
            return self.fullpath != other.fullpath
        else:
            raise TypeError(f'{other} is not a Directory')
    def __lt__(self, other):
        if isinstance(other, Directory):
            return self.size_b < other.size_b
        else:
            raise TypeError(f'{other} is not a Directory')
    def __le__(self, other):
        if isinstance(other, Directory):
            return self.size_b <= other.size_b
        else:
            raise TypeError(f'{other} is not a Directory')
    def __gt__(self, other):
        if isinstance(other, Directory):
            return self.size_b > other.size_b
        else:
            raise TypeError(f'{other} is not a Directory')
    def __ge__(self, other):
        if isinstance(other, Directory):
            return self.size_b >= other.size_b
        else:
            raise TypeError(f'{other} is not a Directory')
    def __getitem__(self, key):
        if isinstance(key, str):
            if os.path.exists(os.path.join(self.fullpath, key)):
                if os.path.isfile(os.path.join(self.fullpath, key)):
                    return File(os.path.join(self.fullpath, key))
                elif os.path.isdir(os.path.join(self.fullpath, key)):
                    return Directory(os.path.join(self.fullpath, key))
                else:
                    raise NotADirectoryError(f"{key} is not a file or directory")
            else:
                raise FileNotFoundError(f"{key} does not exist")
        else:
            raise TypeError(f'{key} is not a string')
    def __iter__(self):
        for i in os.scandir(self.fullpath):
            if i.is_file():
                yield File(i.path)
            elif i.is_dir():
                yield Directory(i.path)
    def __len__(self):
        count = 0
        for i in os.scandir(self.fullpath):
            if i.is_file():
                count += 1
            elif i.is_dir():
                count += len(Directory(i.path))
        return count
    def __contains__(self, other):
        if isinstance(other, File):
            return self.fullpath in other.fullpath
        elif isinstance(other, Directory):
            return self.fullpath in other.fullpath
        else:
            raise TypeError(f'{other} is not a File or Directory')
    def __hash__(self):
        return hash(self.fullpath)
    def move(self, destination):
        if isinstance(destination, Directory):
            destination = destination.fullpath
        if not os.path.exists(destination):
            raise FileNotFoundError(destination)
        if not os.path.isdir(destination):
            raise NotADirectoryError(f"{destination} is not a directory")
        if os.path.exists(os.path.join(destination, self.name)):
            raise FileExistsError(f"{os.path.join(destination, self.name)} already exists")

        os.rename(self.fullpath, os.path.join(destination, self.name))
        self.fullpath = os.path.join(destination, self.name)
        self.dir = os.path.abspath(destination)
    def rename(self, name):
        if os.path.exists(os.path.join(self.dir, name)):
            raise FileExistsError(f"{os.path.join(self.dir, name)} already exists")
        os.rename(self.fullpath, os.path.join(self.dir, name))
        self.name = name
        self.fullpath = os.path.join(self.dir, name)
    def copy(self, destination):
        if isinstance(destination, Directory):
            destination = destination.fullpath
        if not os.path.exists(destination):
            raise FileNotFoundError(destination)
        if not os.path.isdir(destination):
            raise NotADirectoryError(f"{destination} is not a directory")
        if os.path.exists(os.path.join(destination, self.name)):
            raise FileExistsError(f"{os.path.join(destination, self.name)} already exists")

        shutil.copytree(self.fullpath, os.path.join(destination, self.name))
        self.dir = os.path.abspath(destination)
        self.fullpath = os.path.join(self.dir, self.name)
    def delete(self):
        shutil.rmtree(self.fullpath)
        self = None
    def create_file(self, name, content=None):
        if name is None:
            raise ValueError("name cannot be None")
        if os.path.exists(os.path.join(self.fullpath, name)):
            raise FileExistsError(f"{os.path.join(self.fullpath, name)} already exists")
        with open(os.path.join(self.fullpath, name), 'w') as f:
            if content:
                f.write(content)
        
        self.size_b = 0
        try:
            for i in os.scandir(self.fullpath):
                if i.is_file():
                    self.size_b += i.stat().st_size
                elif i.is_dir():
                    self.size_b += Directory(i.path).size_b
        except PermissionError:
            self.size_b = 0
        except Exception:
            self.size_b = 0
        self.size_kb = self.size_b / 1024
        self.size_mb = self.size_kb / 1024
        self.size_gb = self.size_mb / 1024
        self.size_tb = self.size_gb / 1024
        self.size_pb = self.size_tb / 1024
        self.size_eb = self.size_pb / 1024
        self.size_zb = self.size_eb / 1024
        self.size_yb = self.size_zb / 1024
        self.size_preferred = '0b'
        size = self.size_b
        for i in ["b", "kb", "mb", "gb", "tb", "pb", "eb", "zb", "yb"]:
            if size > 1024:
                size = size / 1024
            else:
                self.size_prefferred = f"{size:.3f}{i}"
    def create_directory(self, name):
        if name is None:
            raise ValueError("name cannot be None")
        if os.path.exists(os.path.join(self.fullpath, name)):
            raise FileExistsError(f"{os.path.join(self.fullpath, name)} already exists")
        os.mkdir(os.path.join(self.fullpath, name))

        self.size_b = 0
        try:
            for i in os.scandir(self.fullpath):
                if i.is_file():
                    self.size_b += i.stat().st_size
                elif i.is_dir():
                    self.size_b += Directory(i.path).size_b
        except PermissionError:
            self.size_b = 0
        except Exception:
            self.size_b = 0
        self.size_kb = self.size_b / 1024
        self.size_mb = self.size_kb / 1024
        self.size_gb = self.size_mb / 1024
        self.size_tb = self.size_gb / 1024
        self.size_pb = self.size_tb / 1024
        self.size_eb = self.size_pb / 1024
        self.size_zb = self.size_eb / 1024
        self.size_yb = self.size_zb / 1024
        self.size_preferred = '0b'
        size = self.size_b
        for i in ["b", "kb", "mb", "gb", "tb", "pb", "eb", "zb", "yb"]:
            if size > 1024:
                size = size / 1024
            else:
                self.size_prefferred = f"{size:.3f}{i}"
    def get_files(self):
        files = []
        for i in os.scandir(self.fullpath):
            if i.is_file():
                files.append(File(i.path))
        return files
    def get_directories(self):
        directories = []
        for i in os.scandir(self.fullpath):
            if i.is_dir():
                directories.append(Directory(i.path))
        return directories
    
