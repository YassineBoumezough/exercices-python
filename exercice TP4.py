
def ecrire_tables(fichier="Table_de_multiplication.txt"):
    with open(fichier, "w", encoding="utf-8") as f:
        for n in range(1, 11):

            f.write(f"La table de multiplication de {n:02d}\n")

            for i in range(1, 11):

                f.write(f"{n:02d} X {i:02d} = {n*i:>3d}\n")
            f.write("\n")

if __name__ == "__main__":
    ecrire_tables()