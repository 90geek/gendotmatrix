# gendotmatrix

**Gendotmatrix**: a tool to extract dot matrix font from vector font.

## Install:

```
pip install gendotmatrix
```

## Usage:

```
gendotmatrix.py --help
```

example:

    gendotmatrix.py -o ubuntu-c.font  -s "32x32" "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-C.ttf"

--------------------------------------------------------------------------------------------------------------

I recommend using python3.Because python2 generated Chinese is not aligned.

```
pip3 install gendotmatrix
```

This is the Chinese generated script I use.`ttf_to_16_19_py3_pro.py`
```
sudo python3 ttf_to_16_19_py3_pro.py ttffile > file
```

This is the English generated script I used.`ttf_to_8_19_py3.py`
```
sudo python3 ttf_to_8_19_py3.py ttffile > file
```


