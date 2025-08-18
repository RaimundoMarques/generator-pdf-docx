from docx import Document
from docx2pdf import convert  # Biblioteca para converter DOCX em PDF
import os

class GeradorCurriculo:
    def __init__(self, dados_pessoais):
        self.dados = dados_pessoais
        self.doc = Document()
    
    def adicionar_cabecalho(self):
        self.doc.add_heading(self.dados['nome'], level=0)
        contatos = f"📞 Telefone: {self.dados['telefone']} | 📧 Email: {self.dados['email']} | 🔗 LinkedIn: {self.dados['linkedin']}"
        self.doc.add_paragraph(contatos)
    
    def adicionar_objetivo(self):
        self.doc.add_heading("Objetivo", level=1)
        self.doc.add_paragraph(self.dados['objetivo'])
    
    def adicionar_experiencia(self):
        self.doc.add_heading("Experiência Profissional", level=1)
        for exp in self.dados['experiencias']:
            self.doc.add_heading(exp['empresa'], level=2)
            self.doc.add_paragraph(f"{exp['cargo']} | {exp['periodo']} | {exp['local']}")
            self.doc.add_paragraph(exp['descricao'])
    
    def adicionar_formacao(self):
        self.doc.add_heading("Formação Acadêmica", level=1)
        for formacao in self.dados['formacao']:
            self.doc.add_paragraph(formacao['curso'])
            self.doc.add_paragraph(f"{formacao['periodo']}\nStatus: {formacao['status']}\nTipo: {formacao['tipo']}\nCampus: {formacao['campus']}")
    
    def adicionar_skills(self):
        self.doc.add_heading("Skills Técnicos", level=1)
        self.doc.add_paragraph(self.dados['skills'])
    
    def gerar_curriculo(self, nome_arquivo_docx="Curriculo.docx"):
        try:
            self.adicionar_cabecalho()
            self.adicionar_objetivo()
            self.adicionar_experiencia()
            self.adicionar_formacao()
            self.adicionar_skills()
            
            # Salvar DOCX
            self.doc.save(nome_arquivo_docx)
            print(f"DOCX gerado com sucesso! Arquivo: {nome_arquivo_docx}")
            
            # Converter para PDF
            nome_arquivo_pdf = nome_arquivo_docx.replace(".docx", ".pdf")
            convert(nome_arquivo_docx, nome_arquivo_pdf)
            print(f"PDF gerado com sucesso! Arquivo: {nome_arquivo_pdf}")
            
            return True
        except Exception as e:
            print(f"Erro ao gerar currículo: {e}")
            return False

def main():
    dados_pessoais = {
        'nome': "Raimundo Marques de Freitas Filho",
        'telefone': "(97) 98411-1260",
        'email': "raimundo.marques.ff@gmail.com",
        'linkedin': "https://www.linkedin.com/in/raimundo-marques-filho-06478b108/",
        'objetivo': "Atuar como Full Stack Developer, desenvolvendo aplicações web e mobile modernas, integrando sistemas e contribuindo para soluções escaláveis que agreguem valor ao negócio, buscando conhecimento e experiência para aprimorar meus conhecimentos e capacidades.",
        'experiencias': [
            {
                'empresa': "Instituto Cal-Comp de Pesquisa e Inovação Tecnológica da Amazônia – ICCT",
                'cargo': "Desenvolvedor Full Stack II",
                'periodo': "Maio de 2024 – Atual",
                'local': "Manaus/AM",
                'descricao': "- Desenvolvimento e manutenção de aplicações full stack\n- Implementação de novas funcionalidades e otimização de código\n- Integração de sistemas e APIs para aprimorar fluxos de trabalho internos\n- Colaboração com equipes multidisciplinares para desenvolvimento de soluções inovadoras\n- Desenvolvimento de implementações web e web/mobile\n- Criação de soluções para linhas de montagem de equipamentos de fábricas\n- Tecnologias utilizadas: Docker, Docker-Compose, Linux, React, NestJS, MUI React, Tailwind, Typescript, C# Blazor"
            },
            # ... mantenha as outras experiências aqui
        ],
        'formacao': [
            {
                'curso': "Pós-Graduado em Engenharia de Software – UNIFAVIP Wyden – Martha Falcão, Manaus",
                'periodo': "Janeiro de 2024 - Julho de 2025",
                'status': "Aguardando certificado",
                'tipo': "Especialização",
                'campus': "Polo Universitário – Caruaru – PE"
            },
            {
                'curso': "Graduação em Análise e Desenvolvimento de Sistemas – UNIFAVIP Wyden – Martha Falcão, Manaus",
                'periodo': "Janeiro de 2021 - Dezembro de 2023",
                'status': "Concluído",
                'tipo': "Tecnólogo",
                'campus': "Polo Universitário – Caruaru – PE"
            }
        ],
        'skills': "- Frontend: React, Vue 3, Blazor, Tailwind, Bootstrap, MUI\n- Backend: NestJS, Node.js, PHP (Laravel), C#, Python FastAPI\n- DevOps: Docker, Docker-Compose, Linux\n- Banco de Dados: SQL Server, MySQL, PostgreSQL\n- Integrações: SOAP, REST, JSON/XML, TOTVS RM\n- Controle de Versão: Git, GitHub, GitLab"
    }
    
    gerador = GeradorCurriculo(dados_pessoais)
    gerador.gerar_curriculo("Curriculo_Raimundo_Marques.docx")
    gerador.gerar_curriculo("Curriculo_Raimundo_Marques.pdf")

if __name__ == "__main__":
    main()
