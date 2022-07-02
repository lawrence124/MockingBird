import pycantonese
import re
import csv


if __name__ == "__main__":
    rx = re.compile(r'(?<=\d)(?=[^\d\s])')
    english_check = re.compile(r'[a-z]')


    with open("c://hft//validated.tsv", encoding="utf8") as file:
        
        tsv_file = csv.reader(file, delimiter="\t")
        with open('c://hft//out.tsv', 'w', encoding="utf8") as out_file:
        
            # printing data line by line
            for line in tsv_file:

                #ignore if line[2] has english
                if(english_check.search(line[2]) == None):
                    pys=pycantonese.characters_to_jyutping(line[2])
                    
                    out_line=""
                    finalLine=""
                    for x in pys:
                        if(len(x)==2 and x[1]!=None):
                            out_line=out_line+"^ "+x[1]
                        else:
                            out_line=out_line+"^ "+x[0]
                    out_line = rx.sub( ' ', out_line)
                    print(line[1],'',out_line)
                    finalLine = line[1]+'\t'+out_line+"\n"
                    out_file.write(finalLine)
