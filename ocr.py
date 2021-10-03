#!/usr/bin/env python3

from model import  OcrHandle
from PIL import Image

import sys

ocrhandle = OcrHandle()

def do_ocr(p):
    print("=== %s ===" % p)
    img = Image.open(p)
    short_size = 960
    res = ocrhandle.text_predict(img, short_size)
    for x in res:
        print(x[1])

for x in sys.argv[1:]:
    do_ocr(x)
