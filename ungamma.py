import argparse

import sys
sys.path.append('D:\\git\\RDES')
import RDES as rd
import numpy as np


def main():
    path=parse_arguments().path
    s=rd.read_txt(path)
    temp=rd.read_txt('key.txt')
    mt=temp.split('\n')
    x10,x20,a,b=int(mt[0]),int(mt[1]),int(mt[2]),int(mt[3])
    res=algo(s, x10, x20, a, b, 'key.txt')
    
def algo(text,x10,x20,a,b, path):
    j=0
    txt_file = open(path, "w")
    txt_file.write(str(x10)+"\n")
    txt_file.write(str(x20)+"\n")
    txt_file.write(str(a)+"\n")
    txt_file.write(str(b)+"\n")
    txt_file.close()
    result_text=''
    while j<(len(text)/64):
        text64=text[j*64:64*(j+1)]
        i=0
        tmp='{0:b}'.format(x10)
        while len(tmp)<64:
            tmp='0'+tmp
        res64=''
        while i<64:
            if text64[i]==tmp[i]:
                res64+='0'
            else:
                res64+='1'
            i+=1
        result_text+=res64
        x10=x10*a+x20*b
        j+=1
    rd.write_txt(result_text, 'unres.txt')
    return(result_text)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()

