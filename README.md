# Resume-generator-pdf---docx
Resume generator / pdf - docx


# Gerador de Currículo

Este projeto gera currículos profissionais em formato Word (.docx) usando Python e a biblioteca python-docx.

## Funcionalidades

- Geração automática de currículos em formato Word
- Estrutura modular e reutilizável
- Tratamento de erros
- Dados parametrizados para fácil personalização

## Instalação

1. Clone ou baixe este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

1. Abra o arquivo `gerar_curriculo.py`
2. Modifique os dados pessoais na seção `dados_pessoais` dentro da função `main()`
3. Execute o script:
```bash
python gerar_curriculo.py
```

## Estrutura dos dados

O currículo é gerado a partir de um dicionário com as seguintes seções:

- **nome**: Nome completo
- **telefone**: Número de telefone
- **email**: Endereço de email
- **linkedin**: Perfil do LinkedIn
- **objetivo**: Objetivo profissional
- **experiencias**: Lista de experiências profissionais
- **formacao**: Lista de formações acadêmicas
- **skills**: Skills técnicos

## Exemplo de uso

```python
dados_pessoais = {
    'nome': "Seu Nome Completo",
    'telefone': "(11) 99999-9999",
    'email': "seuemail@email.com",
    'linkedin': "linkedin.com/in/seuperfil",
    'objetivo': "Seu objetivo profissional...",
    # ... outros dados
}

gerador = GeradorCurriculo(dados_pessoais)
gerador.gerar_curriculo("Meu_Curriculo.docx")
```

## Arquivos gerados

O script gera um arquivo Word (.docx) com o nome especificado, contendo todas as seções do currículo formatadas adequadamente.

## Dependências

- python-docx: Para criação e manipulação de documentos Word

## Licença

Este projeto é de uso livre para fins educacionais e profissionais. 