import streamlit as st
import openai

# --- Interface ---
st.set_page_config(page_title="Gerador de RSAs Médicos", layout="wide")
st.title("Gerador de Anúncios Google Ads (RSAs) para Médicos")

# --- Inputs do Usuário ---
api_key = st.text_input("🔑 API Key da OpenAI", type="password")
var_url = st.text_input("🌐 URL da Landing Page")
var_nome = st.text_input("👩‍⚕️ Nome do Médico(a)")
var_especialidade = st.text_input("🏥 Especialidade Médica")
var_cidade = st.text_input("📍 Cidade")
var_diferenciais = st.text_area("✨ Diferenciais / USPs")
var_descricao = st.text_area("📝 Descrição do Serviço/Produto")
var_publico = st.text_input("🎯 Público-Alvo")
var_cta = st.text_input("📣 Chamada para Ação (CTA)")
var_idioma = st.selectbox("🗣 Idioma do Anúncio", ["português", "inglês", "espanhol"])
var_palavras = st.text_area("🔎 Palavras-chave (separadas por vírgula)")

if st.button("🚀 Gerar Anúncios"):
    if not api_key:
        st.error("Insira sua API Key.")
    else:
        openai.api_key = api_key

        instrucoes = """Você é um especialista em redação para Google Ads, com foco em anúncios do tipo Responsivo de Pesquisa (RSAs) para médicos.
Seu objetivo é gerar anúncios otimizados para conversão e totalmente compatíveis com as diretrizes do Google Ads.

Siga as instruções abaixo cuidadosamente.

📥 Coleta de Dados:
URL da Landing Page

Nome do médico

Especialidade médica

Cidade

Descrição do Produto/Serviço

Diferenciais/USPs (o que torna o produto único)

Público-Alvo

Chamada para Ação (CTA) desejada

Idioma

Palavras-chave relevantes (termos de busca)

Idioma do anúncio


📤 Geração de Conteúdo (output formatado em tabelas separadas):
✅ 1. RSA - Headlines (20 itens):

Limite de 30 caracteres por headline.

Use palavras-chave e USPs.

Seja direto e persuasivo.

Varie formatos: perguntas, benefícios, ação.

Exemplo: "Frete Grátis para Todo Brasil", "Agende Sua Avaliação Hoje"

✅ 2. RSA - Descriptions (8 itens):

Limite de 90 caracteres por descrição.

Expanda os benefícios, adicione contexto ou urgência.

✅ 3. Callout Assets (10 itens):

Limite de 25 caracteres.

Destaques rápidos como: "Atendimento 24h", "Descontos Exclusivos"

✅ 4. Sitelinks (4 itens):

Para cada sitelink, gere:

Título (máx. 25 caracteres)

Descrição 1 (máx. 35 caracteres)

Descrição 2 (máx. 35 caracteres)

✅ 5. Snippets Estruturados (Structured Snippets) (2 a 4 snippets):

Escolha entre essas categorias (com base no produto):

Tipos

Destinos

Modelos

Serviços

Cursos

Comodidades

Marcas

Exemplo: Serviços: Consultoria, Treinamento, Suporte 24/7

Gere no formato: Cabeçalho: Item 1, Item 2, Item 3...

📊 Apresente os Resultados Assim:
Para os itens 1, 2 e 3, use tabelas com 3 colunas:

Coluna 1: Número

Coluna 2: Conteúdo

Coluna 3: Contagem de Caracteres

Para os Sitelinks, use uma tabela com 4 colunas:

Número, Título, Descrição 1, Descrição 2 (com contagem de caracteres ao lado de cada item)

Para os Snippets Estruturados, exiba em uma lista formatada:

Exemplo: Comodidades: Wi-Fi grátis, Piscina, Café da manhã incluso

⚠️ Atenção às Diretrizes:

Nenhum texto deve ultrapassar o limite de caracteres.

Conte os caracteres corretamente (incluindo espaços e pontuação).

Use linguagem clara, comercial e focada em conversão.

Priorize headlines que usam termos de busca do usuário.

Siga boas práticas de anúncios de alto desempenho."""


        pergunta = f"""Abaixo, temos todas os dados de entrada. Agora, gere este resultado seguindo as instruções dados anteriormente.
        📥 Coleta de Dados:
        URL da Landing Page: {var_url}

        Nome do médico: {var_nome}

        Especialidade médica: {var_especialidade}

        Cidade: {var_cidade}

        Descrição do Produto/Serviço: {var_descricao}

        Diferenciais/USPs (o que torna o produto único): {var_diferenciais}

        Público-Alvo: {var_publico}

        Chamada para Ação (CTA) desejada: {var_cta}

        Idioma: {var_idioma}

        Palavras-chave relevantes (termos de busca): {var_palavras}

        Idioma do anúncio: {var_idioma}
        """

        with st.spinner("Aguarde, gerando anúncios..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": instrucoes},
                        {"role": "user", "content": pergunta}
                    ]
                )
                resposta = response['choices'][0]['message']['content']
                st.success("✅ Anúncios gerados com sucesso!")
                st.markdown(resposta)
            except Exception as e:
                st.error(f"Erro ao gerar: {e}")
