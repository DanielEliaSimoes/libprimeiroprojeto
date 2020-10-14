import pytest

from libprimeiroprojeto.spam.enviador_de_email import Enviador, EmailInvalido


def test_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    "destinatario",
    ["daniel2013dani@gmail.com", "daniel.elias@fatec.sp.gov.br"]
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        "lucasimoelias@gmail.com",
        "email automatico para teste",
        "primeiro email enviado com o python"
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    "destinatario",
    ["", "email_teste.com"]
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            "lucasimoelias@gmail.com",
            "email automatico para teste",
            "primeiro email enviado com o python"
        )
