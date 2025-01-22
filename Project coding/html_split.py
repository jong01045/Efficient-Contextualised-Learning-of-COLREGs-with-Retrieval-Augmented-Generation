from langchain_core.documents.base import Document
import re

def document_change(documents, document_no, item_key = None, item_value = None, meta_or_cont = "meta", document_or_content = "document"):
    document = documents[document_no]

    if meta_or_cont == "meta":
        r_value = document.metadata[item_key]
        document.metadata[item_key] = item_value
    else:
        r_value = document.page_content
        document.page_content = item_value

    if document_or_content == "document":
        return document
    elif document_or_content == "content":
        return r_value

def instance_document(metadata, page_content):
    return Document(metadata=metadata, page_content=page_content)

def count_content_length(page):
    length = len(page.page_content)
    return length

def extract_substring(s, start_char, end_char):
    """
    Return the partial of string that starts with start_char and ends with end_char

    Args:
    - s: string to be extracted from
    - start_char: The beginning character of extract string
    - end_char: The end character of extract string
    """
    start_index = s.find(start_char)
    end_index = s.rfind(end_char)
    
    if start_index == -1 or end_index == -1 or start_index >= end_index:
        return ""  # Return an empty string if the characters are not found or invalid range

    return s[start_index:end_index+len(end_char)]

def extract_first_sentence(s):
    pattern = r'\b\w+[^.\n]*?\n'
    match = re.search(pattern, s)
    return match.group() if match else None

def find_documents_containing_string(documents, search_string):
    """
    Find and return Document objects that contain the search_string in their page content.

    Args:
    - documents (list of Document): The list of Document objects to search through.
    - search_string (str): The string to search for in the page content.

    Returns:
    - list of Document: A tuple containing Document objects that contain the search string.
    """
    result = [doc for doc in documents if search_string in doc.page_content]
    return result

def part_a_split(documents):

    doc_list = []

    part_a = documents.pop(10).page_content
    part_a_rule_1_content = extract_substring(part_a, "Application", "1144")
    part_a_rule_2_content = extract_substring(part_a, "Rule 2", "danger.")
    part_a_rule_3_content = extract_substring(part_a,"Rule 3", "action.")
    part_a_rule_3_content = extract_substring(part_a_rule_3_content, "(A", "action.")

    part_a_rule_1_document = instance_document(
        metadata={"heading": "PART A - GENERAL, Rule 1 - Application"},
        page_content=part_a_rule_1_content
    )
    doc_list.append(part_a_rule_1_document)

    part_a_rule_2_document = instance_document(
        metadata={"heading": "PART A - GENERAL, Rule 2 - Responsibility"},
        page_content=part_a_rule_2_content
    )
    doc_list.append(part_a_rule_2_document)

    part_a_rule_3_document = instance_document(
        metadata={"heading": "PART A - GENERAL, Rule 3 - General Definitions"},
        page_content=part_a_rule_3_content
    )
    doc_list.append(part_a_rule_3_document)

    for i, doc in enumerate(doc_list):
        documents.insert(i+10, doc)

    return documents

def insert_character(original_string, character, position):
    return original_string[:position] + character + original_string[position:]

def part_b_split(documents):

    part_b_title = documents.pop(13).metadata['heading'][:-2]
    part_b_section_1_title = part_b_title + ", " + documents[13].metadata['heading'].replace("\n", '').strip()[:-19]
    part_b_section_1_title = insert_character(part_b_section_1_title, " ", 45)
    part_b_section_1_title = insert_character(part_b_section_1_title, " ", 47)
    part_b_rule_4_title = part_b_section_1_title + ", " + documents[13].metadata['heading'].replace("\n", '').strip()[-18:]
    part_b_rule_4_title = insert_character(part_b_rule_4_title, " -", 105)

    documents[13].metadata['heading'] = part_b_rule_4_title

    for doc in documents[14:19]:
        doc_title = doc.metadata['heading'].replace("\n", "").strip()
        doc_title = part_b_section_1_title + ", " + doc_title
        doc_title = insert_character(doc_title, " -", 105)
        doc.metadata['heading'] = doc_title
    
    doc_title = documents[19].metadata['heading'].replace("\n", "").strip()
    doc_title = part_b_section_1_title + ", " + doc_title
    doc_title = insert_character(doc_title, " -", 106)
    documents[19].metadata['heading'] = doc_title
    
    part_b_section_2_title = part_b_title + ", " + documents[20].metadata['heading'].replace("\n", "").strip()[:-20]
    part_b_section_2_title = insert_character(part_b_section_2_title, " -", 46)

    part_b_rule_11_title = part_b_section_2_title + ", " + documents[20].metadata['heading'].replace("\n", "").strip()[-19:]
    part_b_rule_11_title = insert_character(part_b_rule_11_title, " -", 100)

    documents[20].metadata['heading'] = part_b_rule_11_title

    for doc in documents[21:28]:
        doc_title = doc.metadata['heading'].replace("\n", "").strip()
        doc_title = part_b_section_2_title + ", " + doc_title
        doc_title = insert_character(doc_title, " -", 100)
        doc.metadata['heading'] = doc_title

    part_b_section_3_title = documents[28].metadata['heading'].replace("\n", "").strip()
    part_b_section_3_title = insert_character(part_b_section_3_title, " ", 11)
    part_b_section_3_title = insert_character(part_b_section_3_title, " ", 13)
    part_b_section_3_title = insert_character(part_b_section_3_title, ",", 57)
    part_b_section_3_title = part_b_title + ", " + part_b_section_3_title
    part_b_section_3_title = insert_character(part_b_section_3_title, " -", 102)

    documents[28].metadata['heading'] = part_b_section_3_title

    return documents

def instance_document_adv(heading=None, page_content=None):
    return Document(metadata={'heading':heading}, page_content=page_content)

def part_c_split(documents):
    
    part_c_document = documents.pop(29)

    # page contents for all rules in part c
    part_c_content = part_c_document.page_content

    rule_20_content = extract_substring(part_c_content, "(a) Rules in this Part", "Regulations.")
    rule_21_content = extract_substring(part_c_content, "(a) 'Masthead light' mean", "minute.")
    rule_22_content = extract_substring(part_c_content, "The lights prescribed in these Rules shall", "miles.")
    rule_23_content = extract_substring(part_c_content, "(The new paragraph (c)", "white light.")
    rule_24_content = extract_substring(part_c_content, "(a) A power-driven vessel when towing", "the towline.")
    rule_25_content = extract_substring(part_c_content, "(a) A sailing vessel underway shall", "down wards.")
    rule_26_content = extract_substring(part_c_content, "(a) A vessel engaged in fishing,", "for a vessel of her length.")
    rule_27_content = extract_substring(part_c_content, "(a) A vessel not under command shall", "red lights (NUC).")
    rule_28_content = extract_substring(part_c_content, "A vessel constrained", "cylinder.")
    rule_29_content = extract_substring(part_c_content, "(a) A vessel engaged on pilotage", "similar vessel of her length.")
    rule_30_content = extract_substring(part_c_content, "(a) A vessel at anchor shall exhibit", "and (ii) of this Rule.")
    rule_31_content = extract_substring(part_c_content, "(This Rule shall enter into force", "as is possible.")

    part_c_title = part_c_document.metadata['heading'].replace("\n", "").strip()
    part_c_title = insert_character(part_c_title, " ", 6)
    part_c_title = insert_character(part_c_title, " ", 8)

    rule_20_title = part_c_title + ", " + "Rule 20 - Application"
    rule_21_title = part_c_title + ", " + "Rule 21 - Definitions"
    rule_22_title = part_c_title + ", " + "Rule 22 - Visibility of Lights"
    rule_23_title = part_c_title + ", " + "Rule 23 - Power-driven Vessels underway"
    rule_24_title = part_c_title + ", " + "Rule 24 - Towing and Pushing"
    rule_25_title = part_c_title + ", " + "Rule 25 - Sailing Vessels underway and Vessels under Oars"
    rule_26_title = part_c_title + ", " + "Rule 26 - Fishing Vessels"
    rule_27_title = part_c_title + ", " + "Rule 27 - Vessels not under Command or Restricted in their Ability to Manoeuvre"
    rule_28_title = part_c_title + ", " + "Rule 28 - Vessel constrained by their draught"
    rule_29_title = part_c_title + ", " + "Rule 29 - Pilot Vessels"
    rule_30_title = part_c_title + ", " + "Rule 30 - Anchored Vessels and Vessels aground"
    rule_31_title = part_c_title + ", " + "Rule 31 - Seaplanes"

    rule_20_doc = instance_document_adv(rule_20_title, rule_20_content)
    rule_21_doc = instance_document_adv(rule_21_title, rule_21_content)
    rule_22_doc = instance_document_adv(rule_22_title, rule_22_content)
    rule_23_doc = instance_document_adv(rule_23_title, rule_23_content)
    rule_24_doc = instance_document_adv(rule_24_title, rule_24_content)
    rule_25_doc = instance_document_adv(rule_25_title, rule_25_content)
    rule_26_doc = instance_document_adv(rule_26_title, rule_26_content)
    rule_27_doc = instance_document_adv(rule_27_title, rule_27_content)
    rule_28_doc = instance_document_adv(rule_28_title, rule_28_content)
    rule_29_doc = instance_document_adv(rule_29_title, rule_29_content)
    rule_30_doc = instance_document_adv(rule_30_title, rule_30_content)
    rule_31_doc = instance_document_adv(rule_31_title, rule_31_content)

    part_c_rule_docs = [rule_20_doc,rule_21_doc,rule_22_doc,rule_23_doc,rule_24_doc,rule_25_doc,rule_26_doc,rule_27_doc, rule_28_doc, rule_29_doc, rule_30_doc,rule_31_doc]

    for i, rule_doc in enumerate(part_c_rule_docs):
        documents.insert(29+i, rule_doc)

    return documents

def part_d_split(documents):

    part_d_doc = documents.pop(41)

    part_d_heading = part_d_doc.metadata['heading'].replace("\n", "").strip()
    rule_32_heading = part_d_heading + ", " + "Rule 32 - Definitions"
    rule_33_heading = part_d_heading + ", " + "Rule 33 - Equipment for Sound Signals"
    rule_34_heading = part_d_heading + ", " + "Rule 34 - Manoeuvring and Warning Signals"
    rule_35_heading = part_d_heading + ", " + "Rule 35 - Sound Signals in restricted Visibility"
    rule_36_heading = part_d_heading + ", " + "Rule 36 - Signals to attract Attention"
    rule_37_heading = part_d_heading + ", " + "Rule 37 - Distress Signals"

    part_d_content = part_d_doc.page_content
    rule_32_content = extract_substring(part_d_content, "(a) The word 'whistle'", "six seconds's duration.")
    rule_33_content = extract_substring(part_d_content, "(Paragraph (a) shall enter", "sound signal.")
    rule_34_content = extract_substring(part_d_content, "(a) When vessels are", "and warning signals.")
    rule_35_content = extract_substring(part_d_content, "(A new paragraph (i) shall", "four short blasts.")
    rule_36_content = extract_substring(part_d_content, "If necessary to attract", "shall be avoided.")
    rule_37_content = extract_substring(part_d_content, "When a vessel is in", "these Regulations.")
    
    rule_32_doc = instance_document_adv(rule_32_heading, rule_32_content)
    rule_33_doc = instance_document_adv(rule_33_heading, rule_33_content)
    rule_34_doc = instance_document_adv(rule_34_heading, rule_34_content)
    rule_35_doc = instance_document_adv(rule_35_heading, rule_35_content)
    rule_36_doc = instance_document_adv(rule_36_heading, rule_36_content)
    rule_37_doc = instance_document_adv(rule_37_heading, rule_37_content)

    part_d_docs = [rule_32_doc, rule_33_doc, rule_34_doc, rule_35_doc, rule_36_doc, rule_37_doc]

    for i, doc in enumerate(part_d_docs):
        documents.insert(41+i, doc)
    
    return documents

def part_e_split(documents):
    part_e = documents[47]

    part_e.metadata['heading'] = part_e.metadata['heading'].replace("\n", "").strip() + ", Rule 38 - Exemptions"
    part_e.page_content = extract_substring(part_e.page_content, "Any vessel (or class of vessels", "permanent exemption.")

    return documents

def part_f_split(documents):
    
    part_f_doc = documents.pop(48)

    part_f_content = part_f_doc.page_content
    annex_content = extract_substring(part_f_content, "ANNEX I", "(b) a dye marker.")
    annex_doc = instance_document_adv(page_content=annex_content)

    IMO_content = extract_substring(part_f_content, "IMO RECOMMENDATION ON NAVIGATIONAL", "with the applicable pollution regulations.")
    IMO_REC_doc = instance_document_adv(page_content=IMO_content)

    part_f_title = part_f_doc.metadata['heading'].replace("\n", "").strip()

    rule_39_title = part_f_title + ", Rule 39 - (Added by Res.A.1085(28)) Definitions"
    rule_40_title = part_f_title + ", Rule 40 - (Added by Res.A.1085(28)) Application"
    rule_41_title = part_f_title + ", Rule 41 - (Added by Res.A.1085(28)) Verification of compliance"

    rule_39_content = extract_substring(part_f_content, "(a) Audit means a systematic", "Code for Implementation.")
    rule_40_content = extract_substring(part_f_content, "Contracting Parties shall use", "contained in the present Convention.")
    rule_41_content = extract_substring(part_f_content, "(a) Every Contracting Party shall", "Organization by resolution A.1067(28).")

    rule_39_doc = instance_document_adv(rule_39_title, rule_39_content)
    rule_40_doc = instance_document_adv(rule_40_title, rule_40_content)
    rule_41_doc = instance_document_adv(rule_41_title, rule_41_content)

    part_f_docs = [rule_39_doc,rule_40_doc,rule_41_doc]

    for i, doc in enumerate(part_f_docs):
        documents.insert(i+48, doc)

    return documents, annex_doc, IMO_REC_doc

def annex_split(annex_doc):

    annex_content= annex_doc.page_content
    
    annex_1_content = extract_substring(annex_content, "The term 'height above the hull'", "State whose flag the vessel is entitled to fly.")
    annex_2_content = extract_substring(annex_content, "The lights mentioned herein shal", "its fishing gear.")
    annex_3_content = extract_substring(annex_content, "(a) Frequencies and range of audibility", " flag the vessel is entitled to fly")
    annex_4_content = extract_substring(annex_content, "1. The following signals, used", "Annex IV")

    annex_1_title = "ANNEX I - POSITIONING AND TECHNICAL DETAILS OF LIGHTS AND SHAPES"
    annex_2_title = "ANNEX II - ADDITIONAL SIGNALS FOR FISHING VESSELS FISHING IN CLOSE PROXIMITY"
    annex_3_title = "ANNEX III - TECHNICAL DETAILS OF SOUND SIGNAL APPLIANCES"
    annex_4_title = "ANNEX IV - DISTRESS SIGNALS"

    annex_1_doc = instance_document_adv(heading=annex_1_title, page_content=annex_1_content)
    annex_2_doc = instance_document_adv(annex_2_title, annex_2_content)
    annex_3_doc = instance_document_adv(annex_3_title, annex_3_content)
    annex_4_doc = instance_document_adv(annex_4_title, annex_4_content)

    annex_doc = [annex_1_doc, annex_2_doc, annex_3_doc, annex_4_doc]

    return annex_doc

def capture_numbered_lines(text):
    pattern = r'^\d+\.\s.*?(?=\n|$)'
    matches = re.findall(pattern, text, re.MULTILINE)
    return matches

def annex_1_split(annex_1_doc, documents):

    annex_1_title = annex_1_doc.metadata['heading']
    annex_1_content = annex_1_doc.page_content

    annex_1_1_title = annex_1_title + ", " + "1. Definition"
    annex_1_2_title = annex_1_title + ", " + "2. Vertical positioning and spacing of lights"
    annex_1_3_title = annex_1_title + ", " + "3. Horizontal positioning and spacing of lights"
    annex_1_4_title = annex_1_title + ", " + "4. Details of location of direction-indicating lights for fishing vessels, dredgers and vessels engaged in underwater operations"
    annex_1_5_title = annex_1_title + ", " + "5. Screens for sidelights"
    annex_1_6_title = annex_1_title + ", " + "6. Shapes"
    annex_1_7_title = annex_1_title + ", " + "7. Colour specification of lights"
    annex_1_8_title = annex_1_title + ", " + "8. Intensity of lights"
    annex_1_9_title = annex_1_title + ", " + "9. Horizontal sectors"
    annex_1_10_title = annex_1_title + ", " + "10. Vertical sectors"
    annex_1_11_title = annex_1_title + ", " + "11. Intensity of non-electric lights"
    annex_1_12_title = annex_1_title + ", " + "12. Manoeuvring light"
    annex_1_13_title = annex_1_title + ", " + "13. High Speed Craft* (This section shall enter into force on 29 November 2003 by Resolution A.910(22))"
    annex_1_14_title = annex_1_title + ", " + "14. Approval"

    annex_1_1_content = "The term 'height above the hull' means height above the uppermost continuous deck. This height shall be measured from the position vertically beneath the location of the light."
    annex_1_2_content = extract_substring(annex_1_content, "(a) On a power-driven vessel of 20 metres", " 6 metres above the hull.")
    annex_1_3_content = extract_substring(annex_1_content, "(a) When two masthead lights are", "basis of the Flag Authority acceptance.")
    annex_1_4_content = extract_substring(annex_1_content, "(a) The light indicating", "prescribed in Rule 27(b)(i) and (ii).")
    annex_1_5_content = extract_substring(annex_1_content, "The sidelights of vessels of 2", "external screens need not be fitted.")
    annex_1_6_content = extract_substring(annex_1_content, "(a) Shapes shall be black an", "correspondingly reduced.")
    annex_1_7_content = extract_substring(annex_1_content, "The chromaticity of all navigation", "y 0.382 0.382 0.425 0.406")
    annex_1_8_content = extract_substring(annex_1_content, "(a) The minimum luminous intensity", " control of the luminous intensity.")
    annex_1_9_content = extract_substring(annex_1_content, "(a) \n(i) In the forward direction", "carrying out the drawing approval process")
    annex_1_10_content = extract_substring(annex_1_content, "(a) The vertical sectors of electric", "be met as closely as possible.")
    annex_1_11_content = "Non-electric lights shall so far as practicable comply with the minimum intensities, as specified in the Table given in Section 8 of this Annex."
    annex_1_12_content = extract_substring(annex_1_content, "Notwithstanding the provisions of paragraph", "apart from the masthead light.")
    annex_1_13_content = extract_substring(annex_1_content, "* Refer to the International Code", "masthead lights in metres.")
    annex_1_14_content = "The construction of lanterns and shapes and the installation of lanterns on board the vessel shall be to the satisfaction of the appropriate authority of the State whose flag the vessel is entitled to fly."

    annex_1_1_doc = instance_document_adv(annex_1_1_title, annex_1_1_content)
    annex_1_2_doc = instance_document_adv(annex_1_2_title, annex_1_2_content)
    annex_1_3_doc = instance_document_adv(annex_1_3_title, annex_1_3_content)
    annex_1_4_doc = instance_document_adv(annex_1_4_title, annex_1_4_content)
    annex_1_5_doc = instance_document_adv(annex_1_5_title, annex_1_5_content)
    annex_1_6_doc = instance_document_adv(annex_1_6_title, annex_1_6_content)
    annex_1_7_doc = instance_document_adv(annex_1_7_title, annex_1_7_content)
    annex_1_8_doc = instance_document_adv(annex_1_8_title, annex_1_8_content)
    annex_1_9_doc = instance_document_adv(annex_1_9_title, annex_1_9_content)
    annex_1_10_doc = instance_document_adv(annex_1_10_title, annex_1_10_content)
    annex_1_11_doc = instance_document_adv(annex_1_11_title, annex_1_11_content)
    annex_1_12_doc = instance_document_adv(annex_1_12_title, annex_1_12_content)
    annex_1_13_doc = instance_document_adv(annex_1_13_title, annex_1_13_content)
    annex_1_14_doc = instance_document_adv(annex_1_14_title, annex_1_14_content)

    annex_1_doc = [annex_1_1_doc, annex_1_2_doc, annex_1_3_doc, annex_1_4_doc, annex_1_5_doc, annex_1_6_doc, annex_1_7_doc, annex_1_8_doc, annex_1_9_doc, annex_1_10_doc, annex_1_11_doc, annex_1_12_doc, annex_1_13_doc, annex_1_14_doc]

    for i, doc in enumerate(annex_1_doc):
        documents.insert(i+51, doc)

    return documents

def annex_2_split(annex_2_doc, documents):

    annex_2_title = annex_2_doc.metadata['heading']
    annex_2_content = annex_2_doc.page_content

    annex_2_1_title = annex_2_title + ", " + "1. General"
    annex_2_2_title = annex_2_title + ", " + "2. Signals for trawlers"
    annex_2_3_title = annex_2_title + ", " + "3. Signals for purse seiners"

    annex_2_1_content = extract_substring(annex_2_content, "The lights mentioned herein shall", "these Rules for fishing vessels")
    annex_2_2_content = extract_substring(annex_2_content, "(a) Vessels of 20 m of more in length", "of this section, as appropriate.")
    annex_2_3_content = "Vessels engaged in fishing with purse seine gear may exhibit two yellow lights in a vertical line. These lights shall flash alternately every second and with equal light and occultation duration. These lights may be exhibited only when the vessel is hampered by its fishing gear."

    annex_2_1_doc = instance_document_adv(annex_2_1_title, annex_2_1_content)
    annex_2_2_doc = instance_document_adv(annex_2_2_title, annex_2_2_content)
    annex_2_3_doc = instance_document_adv(annex_2_3_title, annex_2_3_content)

    documents.insert(65,annex_2_1_doc)
    documents.insert(66,annex_2_2_doc)
    documents.insert(67,annex_2_3_doc)

    return documents

def annex_3_split(annex_3_doc, documents):

    annex_3_title = annex_3_doc.metadata['heading']
    annex_3_content = annex_3_doc.page_content

    annex_3_1_title = annex_3_title + ", " + "1. Whistles (The subparagraphs (a) and (c) shall enter into force on 29 November 2003, as amended by Resolution A.910(22))" 
    annex_3_2_title = annex_3_title + ", " + "2. Bell or gong (The subparagraph (b) shall enter into force on 29 November 2003, as amended by Resolution A.919(22))"
    annex_3_3_title = annex_3_title + ", " + "3. Approvals"

    annex_3_1_content = extract_substring(annex_3_content, "(a) Frequencies and range of audibility.", "the others by at least 10 Hz")
    annex_3_2_content = extract_substring(annex_3_content, "(a) Intensity of signal", "of the mass of the bell")
    annex_3_3_content = "The construction of sound signal appliances, their performance and their installation on board the vessel shall be to the satisfaction of the appropriate authority of the State whose flag the vessel is entitled to fly."

    annex_3_1_doc = instance_document_adv(annex_3_1_title, annex_3_1_content)
    annex_3_2_doc = instance_document_adv(annex_3_2_title, annex_3_2_content)
    annex_3_3_doc = instance_document_adv(annex_3_3_title, annex_3_3_content)

    documents.insert(68, annex_3_1_doc)
    documents.insert(69, annex_3_2_doc)
    documents.insert(70, annex_3_3_doc)

    return documents

def annex_4_split(annex_4_doc, documents):

    annex_4_title = annex_4_doc.metadata['heading']
    annex_4_content = annex_4_doc.page_content

    annex_4_doc = instance_document_adv(annex_4_title, annex_4_content)

    documents.insert(71, annex_4_doc)

    return documents

def IMO_split(IMO_doc):

    IMO_doc_content = IMO_doc.page_content
    IMO_title = "IMO RECOMMENDATION ON NAVIGATIONAL WATCHKEEPING" 

    IMO_section_1_title = IMO_title + ", " + "Section I - Basic principles to be Observed in Keeping a Navigational Watch"
    IMO_section_2_title = IMO_title + ", " + "Section II - Operational Guidance for Officers in charge of a Navigational Watch"
    
    IMO_section_1_content = extract_substring(IMO_doc_content, "[Introduction] \n1. The master of every ship is bound", "framework of existing international regulations.")
    IMO_section_2_content = extract_substring(IMO_doc_content, "[ Introduction ] \n1. This Section contains operational", "with the applicable pollution regulations.")

    IMO_section_1_doc = instance_document_adv(heading=IMO_section_1_title, page_content=IMO_section_1_content)
    IMO_section_2_doc = instance_document_adv(heading=IMO_section_2_title, page_content=IMO_section_2_content)
    IMO_doc = [IMO_section_1_doc, IMO_section_2_doc]

    return IMO_doc

def IMO_section_1_split(section_1_doc, documents):

    section_1_title = section_1_doc.metadata['heading']
    section_1_content = section_1_doc.page_content

    intro_title = section_1_title + ", " + "[Introduction]"
    watch_title = section_1_title + ", " + "[Watch arrangements]"
    fitness_title = section_1_title + ", " + "[Fitness for duty]"
    navigation_title = section_1_title + ", " + "[Navigation]"
    look_title = section_1_title + ", " + "[Look-out]"
    pilot_title = section_1_title + ", " + "[Navigation with Pilot embarked]"
    protection_title = section_1_title + ", " + "[Protection of the marine environment]"

    intro_content = extract_substring(section_1_content, "1. The master of every", "by all ships")
    watch_content = extract_substring(section_1_content, "3. The composition of the watch", "special operational circumstances.")
    fitness_content = extract_substring(section_1_content, "5. The watch system shal", "fit when going on duty.")
    navigation_content = extract_substring(section_1_content, "6. The intended voyage shall be", "the safe navigation of the ship.")
    look_content = extract_substring(section_1_content, "11. Every ship shall at all", "assistance must be immediately available.’")
    pilot_content = extract_substring(section_1_content, "12. Despite the duties and", "conditions and the ship's characteristics.")
    protection_content = extract_substring(section_1_content, "13. The master and officer", "existing international regulations.")

    intro_doc = instance_document_adv(intro_title, intro_content)
    watch_doc = instance_document_adv(watch_title, watch_content)
    fitness_doc = instance_document_adv(fitness_title, fitness_content)
    navigation_doc = instance_document_adv(navigation_title, navigation_content)
    look_doc = instance_document_adv(look_title, look_content)
    pilot_doc = instance_document_adv(pilot_title, pilot_content)
    protection_doc = instance_document_adv(protection_title, protection_content)

    IMO_section_1_doc = [intro_doc, watch_doc, fitness_doc, navigation_doc, look_doc, pilot_doc, protection_doc]

    for i, doc in enumerate(IMO_section_1_doc):
        documents.insert(i+72, doc)

    return documents

def IMO_section_2_split(section_2_doc, documents):

    section_2_title = section_2_doc.metadata['heading']
    section_2_content = section_2_doc.page_content

    intro_title = section_2_title + ", " + "[Introduction]"
    General_title = section_2_title + ", " + "[General]"
    Taking_title = section_2_title + ", " + "[Taking over the watch]"
    Periodic_title = section_2_title + ", " + "[Periodic checks of navigational equipment]"
    Automatic_title = section_2_title + ", " + "[Automatic pilot]"
    Electronic_title = section_2_title + ", " + "[Electronic navigational aids]"
    Echo_title = section_2_title + ", " + "[Echo-sounder]"
    Navigational_title = section_2_title + ", " + "[Navigational records]"
    Radar_title = section_2_title + ", " + "[Radar]"
    Navigation_title = section_2_title + ", " + "[Navigation in coastal waters]"
    Clear_title = section_2_title + ", " + "[Clear weather]"
    Restricted_title = section_2_title + ", " + "[Restricted visibility]"
    Calling_title = section_2_title + ", " + "[Calling the master]"
    Pilot_title = section_2_title + ", " + "[Navigation with pilot embarked]"
    Watchkeeping_title = section_2_title + ", " + "[The watchkeeping personnel]"
    Ship_title = section_2_title + ", " + "[Ship at anchor]"

    intro_content = extract_substring(section_2_content, "1. This Section contains operational", " pollution of the marine environment")
    General_content = extract_substring(section_2_content, "2. The officer of the watch is", " responsibility and this is mutually understood.")
    Taking_content = extract_substring(section_2_content, "8. The officer of the watch should not hand", "such action is completed.")
    Periodic_content = extract_substring(section_2_content, "11. The officer of the watch should mak", "functioning properly.")
    Automatic_content = extract_substring(section_2_content, "12. Officers of the watch should bear in mind the need to station the helmsman and to", "versa should be made by, or under the supervision of, a responsible officer.")
    Electronic_content = "13. The officer of the watch should be thoroughly familiar with the use of electronic navigational aids carried, including their capabilities and limitations."
    Echo_content = "14. The echo-sounder is a valuable navigational aid and should be used whenever appropriate."
    Navigational_content = "15. A proper record of the movements and activities of the vessel should be kept during the watch."
    Radar_content = extract_substring(section_2_content, "16. The officer of the watch should use the", "radar practice.")
    Navigation_content = extract_substring(section_2_content, "21. The largest scale chart on board, suitable for", "relevant navigation marks")
    Clear_content = extract_substring(section_2_content, "23. The officer of the watch", "having the desired effect.")
    Restricted_content = extract_substring(section_2_content, "24. When restricted visibility is", "prominently in mind.")
    Calling_content = extract_substring(section_2_content, "25. The officer of the watch", "circumstances so require.")
    Pilot_content = extract_substring(section_2_content, "26. Despite the duties", "master arrives.")
    Watchkeeping_content = extract_substring(section_2_content, "27. The officer of", "appropriate look-out.")
    Ship_content = extract_substring(section_2_content, "28. If the master considers", "pollution regulations.")

    intro_doc = instance_document_adv(intro_title, intro_content)
    General_doc = instance_document_adv(General_title, General_content)
    Taking_doc = instance_document_adv(Taking_title, Taking_content)
    Periodic_doc = instance_document_adv(Periodic_title, Periodic_content)
    Automatic_doc = instance_document_adv(Automatic_title, Automatic_content)
    Electronic_doc = instance_document_adv(Electronic_title, Electronic_content)
    Echo_doc = instance_document_adv(Echo_title, Echo_content)
    Navigational_doc = instance_document_adv(Navigational_title, Navigational_content)
    Radar_doc = instance_document_adv(Radar_title, Radar_content)
    Navigation_doc = instance_document_adv(Navigation_title, Navigation_content)
    Clear_doc = instance_document_adv(Clear_title, Clear_content)
    Restricted_doc = instance_document_adv(Restricted_title, Restricted_content)
    Calling_doc = instance_document_adv(Calling_title, Calling_content)
    Pilot_doc = instance_document_adv(Pilot_title, Pilot_content)
    Watchkeeping_doc = instance_document_adv(Watchkeeping_title, Watchkeeping_content)
    Ship_doc = instance_document_adv(Ship_title, Ship_content)

    IMO_section_2_docs = [intro_doc, General_doc, Taking_doc, Periodic_doc, Automatic_doc,
                          Electronic_doc, Echo_doc, Navigational_doc, Radar_doc, Navigation_doc,
                          Clear_doc, Restricted_doc, Calling_doc, Pilot_doc, Watchkeeping_doc, Ship_doc]
    
    for i, doc in enumerate(IMO_section_2_docs):
        documents.insert(79+i, doc)

    return documents

def split_main(documents):

    #Title page and ARITICLE I
    document_change(documents=documents, document_no=0, item_key="heading", item_value="Convention on the International Regulations \nfor Preventing Collisions at Sea, 1972 \nConsolidated edition, 2018", document_or_content="document")
    content_1 = document_change(documents, 0, "heading", "Title Page", meta_or_cont="meta", document_or_content="content")
    article_1_content = document_change(documents=documents, document_no=0, document_or_content="content", meta_or_cont="cont", item_value=content_1)
    article_1_document = Document(metadata={
        'heading': "ARTICLE I"},
        page_content= article_1_content)
    documents.insert(1, article_1_document)

    for doc in documents[1:10]:
        doc.metadata['heading'] = doc.metadata['heading'].replace("\n", "").strip()

    # PART A - GENERAL
    documents = part_a_split(documents=documents)

    # PART B 
    documents = part_b_split(documents=documents)

    # PART C
    documents = part_c_split(documents=documents)

    # PART D
    documents = part_d_split(documents=documents)

    # PART E
    documents = part_e_split(documents=documents)

    # PART F
    documents, annex_doc, IMO_REC_doc = part_f_split(documents=documents)

    # ANNEX 
    annex_doc = annex_split(annex_doc=annex_doc)

    documents = annex_1_split(annex_doc[0], documents)

    documents = annex_2_split(annex_doc[1], documents)

    documents = annex_3_split(annex_doc[2], documents)

    documents = annex_4_split(annex_doc[3], documents)

    # IMO
    IMO_doc = IMO_split(IMO_REC_doc)

    documents = IMO_section_1_split(IMO_doc[0], documents=documents)

    documents = IMO_section_2_split(IMO_doc[1], documents)

    # Count length for each document
    for page in documents:
        page.metadata['page_length'] = count_content_length(page)

    return documents



    


