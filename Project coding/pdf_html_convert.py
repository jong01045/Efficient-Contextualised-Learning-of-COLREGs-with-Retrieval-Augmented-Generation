from langchain_community.document_loaders import PDFMinerPDFasHTMLLoader
from bs4 import BeautifulSoup
import re
from langchain_core.documents import Document
from typing import Sequence

def load_pdf_to_html(file_path: str) -> Sequence[Document]:
    loader = PDFMinerPDFasHTMLLoader(file_path=file_path)

    document_miner_html = loader.load()

    docs = beautSoupCaller(document_miner_html)

    return docs

def beautSoupCaller(document_miner_html) -> Sequence[Document]:
    soup = BeautifulSoup(document_miner_html[0].page_content, "html.parser")
    content = soup.find_all("div")

    cur_fs = None
    cur_text = ""
    snippets = []  # first collect all snippets that have the same font size
    for c in content:
        sp = c.find("span")
        if not sp:
            continue
        st = sp.get("style")
        if not st:
            continue
        fs = re.findall("font-size:(\d+)px", st)
        if not fs:
            continue
        fs = int(fs[0])
        if not cur_fs:
            cur_fs = fs
        if fs == cur_fs:
            cur_text += c.text
        else:
            snippets.append((cur_text, cur_fs))
            cur_fs = fs
            cur_text = c.text
    snippets.append((cur_text, cur_fs))

    cur_idx = -1
    semantic_snippets = []
    # Assumption: headings have higher font size than their respective content
    for s in snippets:
        # if current snippet's font size > previous section's heading => it is a new heading
        if (
            not semantic_snippets
            or s[1] > semantic_snippets[cur_idx].metadata["heading_font"]
        ):
            metadata = {"heading": s[0], "content_font": 0, "heading_font": s[1]}
            metadata.update(document_miner_html[0].metadata)
            semantic_snippets.append(Document(page_content="", metadata=metadata))
            cur_idx += 1
            continue

        # if current snippet's font size <= previous section's content => content belongs to the same section (one can also create
        # a tree like structure for sub sections if needed but that may require some more thinking and may be data specific)
        if (
            not semantic_snippets[cur_idx].metadata["content_font"]
            or s[1] <= semantic_snippets[cur_idx].metadata["content_font"]
        ):
            semantic_snippets[cur_idx].page_content += s[0]
            semantic_snippets[cur_idx].metadata["content_font"] = max(
                s[1], semantic_snippets[cur_idx].metadata["content_font"]
            )
            continue

        # if current snippet's font size > previous section's content but less than previous section's heading than also make a new
        # section (e.g. title of a PDF will have the highest font size but we don't want it to subsume all sections)
        metadata = {"heading": s[0], "content_font": 0, "heading_font": s[1]}
        metadata.update(document_miner_html[0].metadata)
        semantic_snippets.append(Document(page_content="", metadata=metadata))
        cur_idx += 1

    return semantic_snippets

