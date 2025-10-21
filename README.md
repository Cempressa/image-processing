# 🏞 Projeto: Pacote de Processamento de Imagens

## Autor do Projeto:  Karina Kato
### Desafio de projeto - Digital Innovation One
[(clique aqui para ver o meu perfil no GitHub)](https://github.com/Cempressa)
#### Tecnologia: Python
-----------------------------------------
### Descrição
O pacote "marcos-image-processing" é utilizado para:

- Módulo "Processing":
  - Correspondência de histograma;
  - Similaridade estrutural;
  - Redimensionar imagem;

- Módulo "Utils":
  - Ler imagem;
  - Salvar imagem;
  - Plotar imagem;
  - Plotar resultado;
  - Plotar histograma;
---------------------------------------------
## Passo a passo da configuração para hospedar um pacote em Python no ambiente de testes Test Pypi

- [x] Instalação das últimas versões de "setuptools" e "wheel"

```bash
py -m pip install --user --upgrade setuptools wheel

```
- [x] Certifique que o diretório no terminal seja o mesmo do arquivo "setup.py" rode o comando
      py setup.py sdist bdist_wheel
```
- [x] Após completar a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:
  - [x] build;
  - [x] dist;
  - [x] marcos-image-processing.egg-info.

- [x] Basta subir os arquivos, usando o Twine, para o Test Pypi:

```
py -m twine upload --repository testpypi dist/*
```
- [x] Após rodar o comando acima no terminal, será pedido para inserir o usuário e senha. Feito isso, o projeto estará hospedado no Test Pypi.
Para que o projeto esteja disponível como um pacote para ser usado publicamente, é necessário hospedá-lo no site oficial do Pypi.

### Aqui o objetivo não é utilizar o projeto da Karina para postar em meu perfil do Pypi pessoal, visto que o projeto é dela. Ainda não tenho nenhum projeto que possa ser utilizado como pacote.

### No entanto, tenha em mente que o Test Pypi, como o próprio nome diz, é apenas um ambiente de testes.
Para que o projeto esteja disponível como um pacote para ser usado publicamente, é necessário hospedá-lo no site oficial do Pypi.
----------------------------------------------------
## Instalação local, após hospedagem no Test Pypi

- [x] Instalação de dependências
pip install -r requirements.txt

```
- [x] Instalação do Pacote
Use o gerenciador de pacotes pip install com o link do TestPyPI para instalar o pacote marcos-image-processing.
pip install -i [https://test.pypi.org/simple/](https://test.pypi.org/simple/) marcos-image-processing
-------------------------------------------------
## Como usar em qualquer projeto

python
from marcos-image-processing.processing import combination
combination.find_difference(image1, image2)
```
<!-- <img width="auto" src="https://github.com/LeticiaMilan/image-processing-package/blob/master/image_processing.png?raw=true"> -->

## Autor(a) (quem hospedou o projeto no Test Pypi)
Marcos Luiz

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
### Principais Alterações de Crédito:

* **Autora do Projeto:** Mantida **Karina Kato**.
* **Link do Perfil:** O texto foi ajustado para esclarecer que o link leva ao GitHub de **Marcos Luiz**.
* **Seção de Autoria Final:** A seção final de `Autor` foi renomeada para **`Contribuidor / Publisher no Test PyPI: Marcos Luiz`**, deixando claro o seu papel na publicação e adaptação.
* **Cláusula Importante:** A seção "Importante" foi detalhada para creditar Karina Kato como a criadora original do código.
