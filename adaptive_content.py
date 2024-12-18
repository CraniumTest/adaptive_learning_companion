from transformers import pipeline

def get_adaptive_content(text, level='easy'):
    summarizer = pipeline("summarization")
    summary_text = summarizer(text, max_length=60, min_length=30, do_sample=False)
    return summary_text if level == 'easy' else text

# Implementation
# content = "A long educational content piece ..."
# simple_content = get_adaptive_content(content, level='easy')
# print(simple_content)
