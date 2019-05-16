import sys
sys.path.append('D:\\git\\RDES')
import RDES as rd
import argparse

def main():
    path=parse_arguments().path
    text=rd.read_txt(path)
    print(text)
    s=rd.chr_to_bin(text)
    x10=int(rd.gpsc(rd.min_key),2)
    x20=1
    a=7
    b=13
    res=algoritm(s, x10, x20, a, b, 'key.txt')
    
def algoritm(text,x10,x20,a,b, path):
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
    rd.write_txt(result_text, 'res.txt')
    return(result_text)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()

