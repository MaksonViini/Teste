import pytest
from httpx import get

url_base = "http://localhost:5000/api/"


class TestBooks:

    # def test_books_retorna_200_se_tiver_um_id_registrado(self):
    #     response = get('{}books/1'.format(url_base))
    #     assert response.status_code == 200

    def test_books_retorna_404_se_nao_tiver_um_id_registrado(self):
        response = get('{}books/1'.format(url_base))
        assert response.status_code == 404


class TestHome:

    def test_home_retorna_200_se_tiver_conteudo_na_home(self):
        response = get('{}home/'.format(url_base))
        assert response.status_code == 200

