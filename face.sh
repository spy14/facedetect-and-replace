#!/bin/bash
JPG=`find ./ -name "*.jpg" -print`

printf %s "$JPG" | while IFS= read -r line
do
   echo "$line"|awk '{printf("%s", $0)}' | /home/spy/facedetect-and-replace/face.py
done
