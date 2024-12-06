class sortfiles:
    def __init__(self, files, json, folderpath):
        self.files = files
        self.json = json
        self.folderpath = folderpath
    def sort(self):
        import os
        files = self.files
        json = self.json
        i = 0
        PicsArray, TextArray, AppsArray = [], [], []
        while(i<len(files)):
            FilesFileType = os.path.splitext(self.folderpath + "/" + files[i])[1]
            j = 0
            while(j<len(self.json)):
                print(json[j]["fileType"])
                if(FilesFileType in json[j]["fileType"]):
                    if(json[j]["foldername"] == "/pictures"):
                        PicsArray.append(files[i])
                    elif(json[j]["foldername"] == "/TextDocuments"):
                        TextArray.append(files[i])
                    elif(json[j]["foldername"] == "/apps"):
                        AppsArray.append(files[i])
                j += 1
            i += 1
        return PicsArray, TextArray, AppsArray