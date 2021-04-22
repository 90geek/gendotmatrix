#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import bitarray
from bitarray import bitarray
import getopt
import sys
import re
from functools import reduce

def get_pix(image):
    pixel = image.load()
    width, height = image.size
    bitmap = bitarray()
    for h in range(height):
        for w in range(width):
            # if int(sum(pixel[w, h])) > (255 * 3 / 2):
            # print pixel[w,h]
            if pixel[w, h] > 0:
                bitmap.append(False)
            else:
                bitmap.append(True)
    return bitmap

def mem(num,arr):
    r =""
    left =""
    right =""
    for row in range(19):
        hv = hex(arr[2*row]).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        left += "0x"+hv
        if row <18:
            left += ",";
        hv = hex(arr[2*row+1]).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        right += "0x"+hv

        if row <18:
            right += ",";

    # print (left)
    # print (right)
    if ("0x00" not in left[10:15]):
        left = "0x00,"+left[0:-5]
        right = "0x00,"+right[0:-5]
    if ("0x00" not in right[10:15]):
        left = "0x00,"+left[0:-5]
        right = "0x00,"+right[0:-5]
    r += "{ "+str(hex(num))+", "+ "0x00, { " + left + "}, {" + right +"}, {0x00,0x00,0x00} },"
    print (r)

def main():
    help = 'Usage: %s [option] <truetype-file>' % sys.argv[0]
    help += '''\noption:
    -h | --help                                 display this information
    -s | --size geometry                        width and height of font
    -o | --output output-dot-matrix-font        specify output file
example:
    gendotmatrix.py -s 16x16 -o ubuntu-c.font "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-C.ttf"
    '''
    short_opts = 'hi:s:o:'
    opts = ['help', 'size=', 'output=']
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, opts)
    except getopt.GetoptError as err:
        print(err)
        print(help)
        sys.exit(1)

    font_width = 16
    font_height = 19
    outfilename = 'dot_matrix.font'
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help)
            sys.exit()
        elif opt in ('-s', '--size'):
            fontsize = re.split(r'\D', arg)
            font_width = int(fontsize[0])
            font_height = int(fontsize[1])
        elif opt in ('-o', '--output'):
            outfilename = arg
        else:
            print(help)
            sys.exit(1)

    if len(args) > 0:
        truetypefile = args[0]
    else:
        print(help)
        sys.exit(1)
    print ("#include <Protocol/HiiFont.h>")
    print ("#include <Protocol/SimpleTextOut.h>")
    print ("EFI_WIDE_GLYPH  gSimpleFontWideGlyphData[] = {")
    usr_font = ImageFont.truetype(truetypefile, 16)
    with open(outfilename, 'wb') as outfile:
        for i in range(0x4e00, 0x9fa5):
        # for i in range(0x51fa, 0x51ff):
            # image = Image.new("RGB", (font_width, h), (255, 255, 255))
            image = Image.new("1", (font_width, font_height), (1))
            d_usr = ImageDraw.Draw(image)
            unicode_code = chr(i)
            # d_usr.text((0, 0), unicode_code, (0,0,0), font=usr_font)
            d_usr.text((0, 0), unicode_code, (0), font=usr_font)
            # image.show()
            # name=""
            # name += "./image/"+str(hex(i))+"_test.jpeg"
            # image.save(name)
            data = get_pix(image)
            # print (data)
            # print (data.tobytes())
            # data.tofile(outfile)
            mem(i,data.tobytes())
    print ("{ 0x0000, 0x00, { 0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00}, {0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00}, {0x00,0x00,0x00} }")
    print ("};")
    print ("UINT32 gSimpleFontBytes=  sizeof (gSimpleFontWideGlyphData);")

if __name__ == '__main__':
    main()
