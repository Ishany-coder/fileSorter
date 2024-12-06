from flask import Flask,request,jsonify
import os
from sortingfiles import sortfiles
app = Flask(__name__)
fileTypes = [
            {
                "foldername": "/pictures",
                "fileType": [
                    ".png", ".jpg", ".jpeg"
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
    sr = sortfiles(files, fileTypes, cleanFolder)
    PicsArray = sr.sort()[0]
    filesToReturn = {
        "files": files,
        "Pics": PicsArray
    }
    return jsonify(filesToReturn), 200

if __name__ == "__main__":
    app.run(debug=True)