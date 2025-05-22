import argparse
from crawler import crawl_site
from indexer import index_docs
from qa_engine import answer_question

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Base help URL to crawl")
    args = parser.parse_args()

    print(f"🔍 Crawling documentation from: {args.url}")
    pages = crawl_site(args.url)

    print(f"✅ Indexed {len(pages)} pages. Processing...")
    index, texts, urls = index_docs(pages)

    print("💬 Ask your question (type 'exit' to quit):")
    while True:
        question = input("> ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        answers = answer_question(question, index, texts, urls)
        if answers:
            for i, (text, url) in enumerate(answers):
                print(f"\n[{i+1}] {text}\n🔗 Source: {url}\n")
        else:
            print("❓ Sorry, I couldn't find anything relevant.")

if __name__ == "__main__":
    main()
