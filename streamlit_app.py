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
        ...
        (mantém o restante da instrução aqui — igual ao seu script original)"""

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
