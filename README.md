# retencao_mobibrasil
Aplicação em desenvolvimento para auxiliar no dia-a-dia da equipe de manutenção da empresa mobibrasil, servindo principalmente na hora da criação da relação dos veículos que se encontram em manutenção

 ## Tecnologias utilizadas
- FastAPI
- Angular CLI@18

## Login screen
<img width="1913" height="905" alt="image" src="https://github.com/user-attachments/assets/5a61bdd5-717d-4ae5-9a9b-c07caa8aafca" />

## Homepage
<img width="1912" height="906" alt="image" src="https://github.com/user-attachments/assets/33072fc7-eb41-486c-8e5a-690e4f96455e" />

# Execução do Backend:

1. Crie e ative seu ambiente virtual:

python -m venv venv
## Windows
venv\Scripts\activate
## Linux/Mac
source venv/bin/activate

2. Instale as dependencias:

pip install -r requirements.txt

3. Configure o banco de dados, se necessário:

alembic init \
alembic revision --autogenerate -m "nome para migração" \
alembic upgrade head


4. Execute a aplicação:

python -m uvicorn backend.main:app --reload


Autores -> [Pedro Henrique Barbosa Da Silva](https://github.com/PedroBDev) e [Rhuan Arquiles Lucena De Freitas](https://github.com/RhuanArquiles)
