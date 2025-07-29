from langchain_core.prompts import PromptTemplate

template = """
Please Summarize the Research Paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
If Certain information is not available in the paper, respond with: "Insufficient Information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length.  

"""

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template=template
)

print(template.invoke({"paper_input": "paper_input", "style_input": "style_input", "length_input": "length_input"}))