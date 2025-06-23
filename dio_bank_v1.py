from abc import ABC, abstractmethod
from datetime import date
from typing import List


class Transacao(ABC):
    @abstractmethod
    def registrar_conta(conta): ...


class Deposito(Transacao):
    def registrar_conta(conta):
        raise NotImplementedError


class Saque(Transacao):
    def registrar_conta(conta):
        raise NotImplementedError


class Historico:
    def adicionar_transacao(trasnsacao: Transacao): ...


class Conta:
    _saldo: float
    _numero: int
    _agencia: str
    _cliente: "Cliente"
    _historico: Historico

    def saldo() -> float: ...
    def nova_conta(cliente: "Cliente", numero: int) -> "Conta": ...
    def sacar(valor: float) -> bool: ...


class ContaCorrente(Conta):
    _limite: float
    _limite_saques: int


class Cliente:
    _endereco: str
    _contas: List[Conta]

    def realizar_transacao(conta: Conta, transacao: Transacao): ...
    def adicionar_conta(conta: Conta): ...


class PessoaFisica(Cliente):
    _cpf: str
    _nome: str
    _data_nascimento: date
