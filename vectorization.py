##import numpy as np
###
f = open("sequenceinput.fasta")
g = open('vetor.fasta',"w")
h = open('label.fasta',"w")
#i = open('texte.txt', "w")

###
d = { "A":('70'),
      "C":('58'),
      "T":('66'),
      "G":('78'),
      "N":('0')
}

###
contador = 0
for linha in f:
    salvarAqui = []
    if linha[0] != ">":
        for caracter in linha:
            contador = contador + 1
            if caracter != "\n":
              ##g.write(str(d[caracter][0]))
              salvarAqui.append(d[caracter])
            else:
              g.write(str.join(',',salvarAqui))
              g.write(caracter)
        contador = 0
    else:
        h.write(linha.split('>')[-1]+'\n')
            

###
f.close()
g.close()
h.close()
#i.close()


with open('vetor.csv', 'w') as file3:
    with open('vetor.fasta', 'r') as file1:
        with open('label.fasta', 'r') as file2:
            for line1, line2 in zip(file1, file2):
                if len(line1) == 1:
                    pass
                else:
                    print(line1.strip().replace('\n',''),',',line2.strip().replace('\n',''), file=file3)
                
