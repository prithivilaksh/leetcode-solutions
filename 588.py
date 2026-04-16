# Design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

# FileSystem() Initializes the object of the system.
# List<String> ls(String path)
# If path is a file path, returns a list that only contains this file's name.
# If path is a directory path, returns the list of file and directory names in this directory.
# The answer should in lexicographic order.
# void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
# void addContentToFile(String filePath, String content)
# If filePath does not exist, creates that file containing given content.
# If filePath already exists, appends the given content to original content.
# String readContentFromFile(String filePath) Returns the content in the file at filePath.


from collections import defaultdict
class FileSystem:
    def __init__(self):
        Trie=lambda:defaultdict(Trie)
        self.root=Trie()
        self.root['']=self.root
    
    @staticmethod
    def splitPath(path):
        return path.split("/")[1:]
    
    def iteratePath(self,path):
        node=self.root
        for x in self.splitPath(path):
            node=node[x]
        return node   

    def ls(self, path: str) -> List[str]:
        node=self.iteratePath(path)
        if "#content#" in node.keys(): return self.splitPath(path)[-1:]
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        self.iteratePath(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node=self.iteratePath(filePath)
        node["#content#"]=node.get("#content#","")+content

    def readContentFromFile(self, filePath: str) -> str:
        node=self.iteratePath(filePath)
        return node.get("#content#","")

    


    

class Trie:
    def __init__(self):
        self.name = None
        self.isFile = False
        self.content = []
        self.children = {}

    def insert(self, path, isFile):
        node = self
        ps = path.split('/')
        for p in ps[1:]:
            if p not in node.children:
                node.children[p] = Trie()
            node = node.children[p]
        node.isFile = isFile
        if isFile:
            node.name = ps[-1]
        return node

    def search(self, path):
        node = self
        if path == '/':
            return node
        ps = path.split('/')
        for p in ps[1:]:
            if p not in node.children:
                return None
            node = node.children[p]
        return node


class FileSystem:
    def __init__(self):
        self.root = Trie()

    def ls(self, path: str) -> List[str]:
        node = self.root.search(path)
        if node is None:
            return []
        if node.isFile:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.root.insert(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root.insert(filePath, True)
        node.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root.search(filePath)
        return ''.join(node.content)
