

with open("all_sequence.fasta", "w") as file:

    # Percorre a lista de arquivos a serem lidos:
    for temp in ["Aethiopicajuntos.fas", "Arabicajuntos.fas", "Braziliensisjuntos.fas", "Donovanijuntos.fas", "Enriettiijuntos.fas", "Infantumjuntos.fas", "Majorjuntos.fas", "Mexicanajuntos.fas", "Panamensisjuntos.fas", "Peruvianiajuntos.fas"]:

        # Abre cada arquivo para leitura:
        with open(temp, "r") as t:

            # Escreve no arquivo o conteúdo:
            file.writelines(t)
            file.writelines('\n')
