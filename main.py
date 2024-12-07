from flask import Flask,request,jsonify
import os
from sortingfiles import sortfiles
app = Flask(__name__)
fileTypes = [
            {
                "foldername": "/pictures",
                "fileType": [
                    ".png", ".jpg", ".jpeg", ".webp"
                ]
            },
            {
                "foldername": "/apps",
                "fileType": [
                    ".dmg"
                ]
            },
            {
                "foldername": "/TextDocuments",
                "fileType": [
                    ".pptx", ".txt", ".docx", ".pdf"
                ]
            }
        ]
@app.route("/fetchfiles/<folder>")
def fetchfiles(folder):
    cleanFolder = "/Users/ishanghosh/" + folder + "/"
    files = os.listdir("/Users/ishanghosh/" + folder + "/")
    print("*****files in API*****" + str(files))
    sr = sortfiles(files, fileTypes, cleanFolder)
    PicsArray = sr.sort()[0]
    TextArray = sr.sort()[1]
    AppsArray = sr.sort()[2]
    OtherArray = sr.sort()[3]
    filesToReturn = {
        "files": files,
        "Pics": PicsArray,
        "Text": TextArray,
        "Apps": AppsArray,
        "other": OtherArray
    }
    return jsonify(filesToReturn), 200

if __name__ == "__main__":
    app.run(debug=True)