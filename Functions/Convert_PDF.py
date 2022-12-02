from tabula import convert_into

def Convert(diretorio):
    print("Covertendo...")

    convert_into(diretorio, "teste.csv", output_format="csv", pages="all")

    print("Finalizado...")