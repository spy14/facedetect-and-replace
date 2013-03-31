#!/bin/bash
JPG=`find ./ -iname "*.jpg" -iname "*.JPG" -print| awk '!/thumb/'`

printf %s "$JPG" | while IFS= read -r line
do
   echo "$line" |awk '{printf("%s", $0)}' | /home/spy/facedetect-and-replace/face.py
done
