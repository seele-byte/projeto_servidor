from pathlib import Path
from palavras_importantes import *

caminho = Path("/home/gabriel/servidor/logs/var/log/auth.log")


logs_logins_autenticacao = []
logs_escalonamento_de_privilegio = []
logs_ataque_automatizado = []
logs_rede_conexao_firewall = []

with open(caminho, "r") as arquivo:
    for linha in arquivo:
        if any(p in linha.lower() for p in logins_autenticacao):
            logs_logins_autenticacao.append(linha)
        if any (q in linha.lower() for q in escalonamento_de_privilegio):
            logs_escalonamento_de_privilegio.append(linha)
        if any (r in linha.lower() for r in ataque_automatizado):
            logs_ataque_automatizado.append(linha)
        if any (s in linha.lower() for s in rede_conexao_firewall):
            logs_rede_conexao_firewall.append(linha)

with open ("textos/logins.txt", "w") as f1:
    for item in logs_logins_autenticacao:
        f1.write(item + "\n")

with open("textos/escalacao_de_privilegio.txt", "w") as f2:
    for item in logs_escalonamento_de_privilegio:
        f2.write(item + "\n")

with open("textos/ataque_automatizado.txt","w") as f3:
    for item in logs_ataque_automatizado:
        f3.write(item + "\n")

with open("textos/rede_conexao_firewall.txt","w") as f4:
    for item in logs_rede_conexao_firewall:
        f4.write(item + "\n")
