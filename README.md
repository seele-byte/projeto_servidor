# Sistema de Monitoramento e Filtragem de Logs Linux

Projeto desenvolvido para coleta e análise de logs de autenticação em ambientes Linux utilizando Python, SSH e virtualização. O objetivo é automatizar a identificação de eventos relevantes relacionados a autenticação, brute force, escalonamento de privilégio e eventos de rede/firewall.

## Visão Geral

O projeto utiliza logs do arquivo `auth.log` de um servidor Ubuntu Server executado em máquina virtual Oracle VM. Os logs são coletados, compactados e transferidos via SSH para análise local.

O script em Python realiza a leitura e filtragem dos eventos utilizando palavras-chave associadas a diferentes categorias de segurança, separando automaticamente os resultados em arquivos específicos.

## Tecnologias Utilizadas

- Python
- Linux (Ubuntu Server)
- SSH
- Oracle VM VirtualBox
- Manipulação de logs Linux (`auth.log`)
- Compactação `.tar.gz`

## Funcionamento

1. Coleta do arquivo `auth.log` no servidor Linux
2. Compactação dos logs utilizando `tar`
3. Transferência do arquivo via SSH
4. Execução do script `logs.py`
5. Filtragem automática dos eventos
6. Separação dos resultados em categorias:
   - autenticação/login
   - escalonamento de privilégio
   - ataques automatizados/brute force
   - rede e firewall

## Estrutura do Projeto

.
├── logs.py  
├── palavras_importantes.py  
└── textos/  
&nbsp;&nbsp;&nbsp;&nbsp;├── ataque_automatizado.txt  
&nbsp;&nbsp;&nbsp;&nbsp;├── escalacao_de_privilegio.txt  
&nbsp;&nbsp;&nbsp;&nbsp;├── logins.txt  
&nbsp;&nbsp;&nbsp;&nbsp;└── rede_conexao_firewall.txt  

## Melhorias Planejadas

- Automação da transferência de arquivos via SSH
- Identificação automática do caminho do `auth.log`
- Script dedicado para coleta e compactação automática dos logs
- Expansão das palavras-chave e categorias de eventos
- Geração de relatórios automatizados

## Observações

O desenvolvimento do projeto foi realizado em colaboração utilizando um único computador durante parte da implementação. Por esse motivo, os commits do repositório podem aparecer quase todos associados a um único usuário.
