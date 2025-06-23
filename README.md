# 🏦 Sistema Bancário POO em Python — Versão 1 (Somente Abstrações)

Este projeto é a **versão 1** de um sistema bancário orientado a objetos em Python.  
O objetivo desta etapa é **definir a estrutura das classes** usando princípios de POO, sem implementar nenhuma lógica.

---

## 📚 Índice

- [🎯 Objetivo](#🎯-objetivo)
- [🏗️ Estrutura do Projeto](#🏗️-estrutura-do-projeto)
- [💻 Tecnologias Utilizadas](#💻-tecnologias-utilizadas)
- [🧱 Organização de Classes](#🧱-organização-de-classes)
- [🚧 Próxima Etapa](#🚧-próxima-etapa)
- [🤝 Contribuição](#🤝-contribuição)

---

## 🎯 Objetivo

Definir a base de um sistema bancário com foco em:

- Abstração com `ABC` e métodos abstratos
- Herança (ex: `ContaCorrente` herda `Conta`)
- Composição (ex: `Conta` tem `Historico`)
- Encapsulamento com atributos protegidos
- Tipagem com `typing`

> Nenhuma função está implementada nesta versão.  
> Apenas as **assinaturas e estrutura POO** foram definidas.

---

## 🏗️ Estrutura do Projeto

As classes e relações seguem a modelagem típica de um sistema bancário OO:

- **Sem métodos implementados**
- **Tipagem explícita em atributos e parâmetros**
- **Organização limpa e preparada para expansão futura**

---

## 💻 Tecnologias Utilizadas

- Python `3.10+`
- Módulos:
  - `abc` — classes/métodos abstratos
  - `typing` — tipagem genérica (`List`, `Union`, etc.)
  - `datetime` — datas de nascimento

---

## 🧱 Organização de Classes

```python
class Transacao(ABC):
    def registrar_conta(conta): ...

class Deposito(Transacao)
class Saque(Transacao)

class Conta:
    _cliente: "Cliente"
    _historico: Historico

class ContaCorrente(Conta)

class Historico:
    def adicionar_transacao(transacao): ...

class Cliente:
    _contas: List[Conta]
    def realizar_transacao(conta, transacao): ...
    def adicionar_conta(conta): ...

class PessoaFisica(Cliente):
    _cpf: str
    _nome: str
    _data_nascimento: date
```

---

## 🚧 Próxima Etapa

Na **versão 2**, será feita a implementação dos métodos:

- Execução de depósitos e saques
- Validação de saldo, limites e histórico
- Menu CLI ou testes unitários para interagir com o sistema

---

## 🤝 Contribuição

Contribuições são bem-vindas! Para colaborar:

```bash
# Faça fork e clone o projeto
git checkout -b melhoria/estrutura
git commit -m "Melhoria na estrutura de classes"
git push origin melhoria/estrutura
```

Abra um Pull Request e envie sua sugestão 👍

---

📌 Projeto criado como exercício de estruturação de código orientado a objetos com Python — **Versão 1: Somente Abstrações**
