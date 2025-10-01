
adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

print("1. Première adresse :", adresses_ip[0])
print("2. Dernière adresse :", adresses_ip[-1])
print("3. Troisième adresse :", adresses_ip[2])

adresses_ip.append("172.31.0.1")
print("4. Après ajout :", adresses_ip)

adresses_ip.remove("200.100.50.1")
print("5. Après suppression :", adresses_ip)

print("6. Nombre d’adresses restantes :", len(adresses_ip))

print("7. '192.168.0.1' est présente ? :", "192.168.0.1" in adresses_ip)

premier_octet = int("10.0.0.1".split(".")[0])
if 0 <= premier_octet <= 127:
    print("8. Classe de 10.0.0.1 : Classe A")
elif 128 <= premier_octet <= 191:
    print("8. Classe de 10.0.0.1 : Classe B")
elif 192 <= premier_octet <= 223:
    print("8. Classe de 10.0.0.1 : Classe C")

adresses_ip.sort()
print("9. Liste triée :", adresses_ip)

toutes_classe_c = True
for ip in adresses_ip:
    premier = int(ip.split(".")[0])
    if not (192 <= premier <= 223):
        toutes_classe_c = False
print("10. Toutes en classe C ? :", toutes_classe_c)

nb_publiques = 0
for ip in adresses_ip:
    premier, deuxieme, *_ = map(int, ip.split("."))
    if premier == 10:
        continue
    elif premier == 172 and 16 <= deuxieme <= 31:
        continue
    elif premier == 192 and deuxieme == 168:
        continue
    elif premier == 169 and deuxieme == 254:
        continue
    else:
        nb_publiques += 1
print("11. Nombre d’adresses publiques :", nb_publiques)
