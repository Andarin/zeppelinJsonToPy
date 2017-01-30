#!/usr/bin/env

## AUTHOR: Lucas Tittmann
## LICENSE: Apache v 2.0
##
## DESCRIPTION
##   Script to transform Apache Zeppelin [https://zeppelin.apache.org/]
##   JSON files into Python Scripts

import os
import sys
import json

def zeppelinJsonToPy(fileInput, fileOutput):
    with open(fileInput, "r") as f:
        dataStr = f.readline()
        data = json.loads(dataStr.decode("utf-8-sig"), encoding = "utf-8")

    out = ""
    for paragraph in data["paragraphs"]:
        paragraphText = paragraph["text"]
        if paragraphText[0:len("%pyspark")] == "%pyspark":
            out += paragraphText[len("%pyspark"):]
            out += "\n"

    with open(fileOutput, "a") as f:
        f.write(out)

if __name__ == "__main__":
    fileInput = sys.argv[1]
    fileBaseName = os.path.splitext(fileInput)[0]
    fileOutput = fileBaseName + ".py"
    zeppelinJsonToPy(fileInput, fileOutput)
