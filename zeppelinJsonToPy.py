#!/usr/bin/env


import os
import json

fileInput = "C:/"
fileBaseName = os.path.splitext(fileInput)[0]
fileOutput = fileBaseName + ".py"

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
