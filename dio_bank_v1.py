from abc import ABC, abstractmethod
from datetime import date
from typing import List


class Transacao(ABC):
    @abstractmethod
    def registrar_conta(self, conta: "Conta"): ...


class Deposito(Transacao): ...


class Saque(Transacao): ...


class Historico:
    def adicionar_transacao(self, transacao: Transacao): ...


class Conta:
    _saldo: float
    _numero: int
    _agencia: str
    _cliente: "Cliente"
    _historico: Historico

    def saldo(self) -> float: ...
    @classmethod
    def nova_conta(cls, cliente: "Cliente", numero: int) -> "Conta": ...
    def sacar(self, valor: float) -> bool: ...


class ContaCorrente(Conta):
    _limite: float
    _limite_saques: int


class Cliente:
    _endereco: str
    _contas: List[Conta]

    def realizar_transacao(self,conta: Conta, transacao: Transacao): ...
    def adicionar_conta(self, conta: Conta): ...


class PessoaFisica(Cliente):
    _cpf: str
    _nome: str
    _data_nascimento: date
