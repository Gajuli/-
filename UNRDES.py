import libcrypt as lc
import RDES as rd
import argparse


def main():
	path=parse_arguments().path
	shifr=rd.read_txt(path)
	key=rd.read_txt('key.txt')
	unshifr=rd.un_algoritm(shifr,key)
	bin_to_txt(unshifr)

def bin_to_txt(text):
    res=''
    i=0
    tmp_txt=text
    while len(tmp_txt)!=0:
        tmp_ord_bin=tmp_txt[(len(tmp_txt)-11):len(tmp_txt)]
        tmp_txt=tmp_txt[0:(len(tmp_txt)-11)]
        tmp_ord=int(tmp_ord_bin,2)
        if tmp_ord!=0:
            res=chr(tmp_ord)+res
        i+=1
    rd.write_txt(res, 'un_shifr.txt')
    return(res)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()