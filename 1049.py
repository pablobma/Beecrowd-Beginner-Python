first = str(input())
sec = str(input())
third = str(input())

if first == "vertebrado":
    if sec == "ave":
        if third == "carnivoro":
            print("aguia")
        elif third == "onivoro":
            print("pomba")
    elif sec == "mamifero":
        if third == "onivoro":
            print("homem")
        elif third == "herbivoro":
            print("vaca")


if first == "invertebrado":
    if sec == "inseto":
        if third == "hematofago":
            print("pulga")
        elif third == "herbivoro":
            print("lagarta")
    if sec == "anelideo":
        if third == "hematofago":
            print("sanguessuga")
        elif third == "onivoro":
            print("minhoca")
