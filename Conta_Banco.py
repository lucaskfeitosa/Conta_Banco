from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        nome(str): Nome do Cliente
        cpf(str): CPF do Cliente. Deve ser inserido com pontos e traços
        agencia: Agencia responsável pela conta do cliente
        num_conta: Número da conta corrente do cliente
        transacoes: histórico de transações do cliente
    """
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f'Seu saldo atual é R${self._saldo:,.2f}')

    def depositar(self, valor):
        self._saldo += valor
        print(f"Você depositou R${valor:,.2f} e agora seu saldo é de R${self._saldo:,.2f}")
        self._transacoes.append((valor, f'Saldo:{self._saldo:,.2f}', ContaCorrente._data_hora()))

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente")
        else:
            self._saldo -= valor
            print(f"Você sacou R${valor:,.2f} e agora seu saldo é de R${self._saldo:,.2f}")
            self._transacoes.append((-valor, f'Saldo:{self._saldo:,.2f}', ContaCorrente._data_hora()))

    def consultar_historico_transacoes(self):
        print("Histórico de transações:")
        print("Valor, Saldo, Data/Hora")
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, f'Saldo:{self._saldo:,.2f}', ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        self._transacoes.append((+valor, f'Saldo:{self._saldo:,.2f}', ContaCorrente._data_hora()))

class CartaoCredito:
    
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titular, conta_corrente):
        self._titular = titular
        self._numero = randint(1000000000000000, 9999999999999999)
        self._validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self._cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self._limite = 1000
        self._conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


