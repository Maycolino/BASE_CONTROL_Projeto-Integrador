Nome da aplicação: BASE CONTROL

Descrição:
Base Control é uma aplicação para registros, acompanhamento de atividades, geração de relatórios e gráficos. É uma ferramenta prática, rápida, acessível e flexível que atende tanto a indivíduos quanto a empresas. Permite a inserção interativa de informações e dados de atividades laborais, possibilitando aos usuários a obtenção de relatórios atualizados sobre as atividades realizadas e quem as executou.

✅ Requisitos Funcionais:

1ª Tela:
Botões
  - REGISTRAR
  - ACOMPANHAR

2ª Tela:
inserção manual de dados de registro, incluindo:
   - Nº Matricula
   - Colaborador
   - Placa
   - Retirada (data e hora)
   - Devolução (data e hora)
   - Quilômetros rodados
   - Despesa de combustível
   - Despesa de pane
   - Despesa de pedágio
   - Total de despesas
   - Multa
   - Observações

❌ Requisitos Não Funcionais:

- Nome completo e número de matrícula do funcionário serão exibidos automaticamente na segunda tela.
- Performance: A aplicação deve ser responsiva, com baixa latência na execução do código.
- Usabilidade: A interface deve ser intuitiva e fácil de usar, especialmente para usuários iniciantes.
- Escalabilidade: A aplicação deve suportar um aumento no número de usuários sem comprometer a qualidade.
- Segurança: Garantir a segurança dos dados dos usuários e evitar vulnerabilidades.
- Compatibilidade: Deve funcionar em diversos navegadores e sistemas operacionais.

Tecnologia Usada:

A aplicação é desenvolvida em Python, utilizando suas bibliotecas de dados.

Como Rodar:

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Abra o terminal e navegue até o diretório do projeto.
4. Execute o comando `python app.py` para iniciar a aplicação.
5. Uma interface será aberta e você poderá usar o Base Control.

Licença:

Este projeto está sob a licença Projeto Integrador SENAI.

Link da Aplicação:

1. Tela de acesso (janela de login) - Campos de registro:
   - Matrícula do funcionário
   - Senha

2. Tela de registro:
   - Nome completo do motorista e matrícula na empresa serão carregados automaticamente após o login.
   - Campos de registro:
     - Placa
     - Retirada (Data e Hora)
     - Devolução (Data e Hora)
     - Quilômetros Rodados
     - Despesa de Combustível
     - Despesa de Pane
     - Despesa de Pedágio
     - Total de Despesas
     - Observações

Botão:

- Salvar e Sair
