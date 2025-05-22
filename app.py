import streamlit as st
from crawler import crawl_site
from indexer import index_docs
from qa_engine import answer_question

st.title("📚 AI Doc QA Assistant")

# Input URL
url = st.text_input("Enter base documentation URL", "https://help.zluri.com")

if url:
    with st.spinner("🔍 Crawling and indexing documentation..."):
        pages = crawl_site(url)
        index, texts, urls = index_docs(pages)
    
    st.success(f"✅ Indexed {len(pages)} pages.")

    # ✅ Add the form here
    with st.form("qa_form"):
        question = st.text_input("Ask a question")
        submitted = st.form_submit_button("Submit")

        if submitted and question:
            st.write(f"👉 You asked: {question}")
            answers = answer_question(question, index, texts, urls)

            # 🔍 Add debug output here
            st.write(f"🔍 Raw Answers: {answers}")

            if answers:
                for i, (text, url) in enumerate(answers):
                    st.markdown(f"**Answer {i+1}:** {text}\n\n[🔗 Source]({url})")
            else:
                st.warning("😕 Sorry, I couldn't find anything relevant.")
