from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


def summarize_text(text, sentence_count=5):
    try:
        if not text or len(text.strip()) == 0:
            return "No content available for summary."

        parser = PlaintextParser.from_string(
            text,
            Tokenizer("english")
        )

        summarizer = TextRankSummarizer()

        summary = summarizer(parser.document, sentence_count)

        result = " ".join(str(sentence) for sentence in summary)

        if not result.strip():
            return text[:500] + "..."

        return result

    except Exception as e:
        print("SUMMARY ERROR:", e)
        return text[:500] + "..."
