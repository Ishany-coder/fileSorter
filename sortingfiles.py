class sortfiles:
    def __init__(self, files, json, folderpath):
        self.files = files
        self.json = json
        self.folderpath = folderpath
    def sort(self):
        import os, shutil
        files = self.files
        print("******FILEs*******" + str(files))
        json = self.json
        i = 0
        PicsArray, TextArray, AppsArray, otherArray = [], [], [], []
        while(i<len(files)):
            print("file cleaning " + files[i])
            FilesFileType = os.path.splitext(self.folderpath + "/" + files[i])[1]
            j = 0
            while(j<len(self.json)):
                print(json[j]["fileType"])
                if(FilesFileType in json[j]["fileType"]):
                    if(json[j]["foldername"] == "/pictures"):
                        try:
                            PicsArray.append(files[i])
                            destination_path = "/Users/ishanghosh/Downloads/pictures/" + files[i]
                            sourcePath = "/Users/ishanghosh/Downloads/" + files[i]
                            print("destination path: " + destination_path)
                            shutil.move(sourcePath, destination_path)
                        except FileNotFoundError:
                            print("file not found " + files[i])
                    elif(json[j]["foldername"] == "/TextDocuments"):
                        TextArray.append(files[i])
                    elif(json[j]["foldername"] == "/apps"):
                        AppsArray.append(files[i])
                    else:
                        otherArray.append(files[i])
                j += 1
            i += 1
        return PicsArray, TextArray, AppsArray, otherArray