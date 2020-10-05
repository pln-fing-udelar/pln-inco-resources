import csv
import re
import os
import xml.etree.ElementTree as ET

def process_corpus_task1(original_file):
    tree = ET.parse(original_file)
    factuality_dict = {}
    root = tree.getroot()
    for child in root.iter():
        if child.tag == 'text':
            parent_id = child.items()[0][1]
            event_counter = 1
        elif child.tag == 'event':
            new_id = parent_id + 'e' + str(event_counter).zfill(3)
            factuality_dict[new_id]=child.attrib['factuality']
            child.set('id', new_id)
            child.set('factuality','')
            event_counter+=1

    tree.write('FACT2020test_task1_ready.xml',encoding='UTF-8',xml_declaration=True)

    with open('FACT2020test_task1_ready.csv', 'w') as f:
    	for id_evento in factuality_dict.keys():
            f.write("%s, %s\n" % (id_evento, factuality_dict[id_evento]))

def process_corpus_task2(original_file):
    with open(original_file, "r+") as f:
        xml = re.sub(r"<event.*?>", "¿¡!?", f.read())
        xml = re.sub(r"</event.*?>", "", xml)
        f.close()
    no_events_xml = original_file[:-4] + "_no_events.xml"
    with open (no_events_xml,"w+") as f:
        f.write(xml)
        f.close()

    token_count=1
    event_tokens = []

    tree = ET.parse(no_events_xml)
    root = tree.getroot()
    for child in root.iter():
        if child.tag == 'text':
            lines = child.text.splitlines(True)
            for i, line in enumerate(lines):
                tokens = line.split()
                for j, token in enumerate(tokens):
                    if token[:4]=='¿¡!?':
                        token = token[4:]
                        event_tokens.append(str(token_count))
                    tokens[j] = token + "/" + str(token_count)                    	
                    token_count+=1
                lines[i] = " ".join(tokens)
            child.text = "\n".join(lines)

    tree.write('FACT2020test_task2_ready.xml',encoding='UTF-8',xml_declaration=True)
    os.remove(no_events_xml)
    with open('FACT2020test_task2_ready.csv', 'w') as f:
    	for id_token in event_tokens:
            f.write(id_token + "\n")	

def generate_baseline_task2(train_file):
    with open(train_file, "r+") as f:
        xml = re.sub(r"<event.*?>", "¿¡!?", f.read())
        xml = re.sub(r"</event.*?>", "", xml)
        f.close()
    no_events_xml = train_file[:-4] + "_no_events.xml"
    with open (no_events_xml,"w+") as f:
        f.write(xml)
        f.close()
    events = []
    tree = ET.parse(no_events_xml)
    root = tree.getroot()
    for child in root.iter():
        if child.tag == 'text':
            lines = child.text.splitlines(True)
            for line in lines:
                tokens = line.split()
                for token in tokens:
                    if token[:4]=='¿¡!?':
                        events.append(token[4:])
    os.remove(no_events_xml)

    #Ahora recorremos el corpus de test_task2. Si el token pertenece al diccionario, se anota como evento.
    id_tokens_baseline=[]
    tree = ET.parse("FACT2020test_task2_ready.xml")
    root = tree.getroot()
    for child in root.iter():
        if child.tag == 'text':
            lines = child.text.splitlines(True)
            for line in lines:
                tokens = line.split()
                for token in tokens:
                    original_token = token.split("/")[0]
                    id_token = token.split("/")[1]
                    if original_token in events:
                        print(original_token)
                        print(id_token)
                        id_tokens_baseline.append(id_token)
    with open('task2_baseline.csv', 'w') as f:
    	for id_token in id_tokens_baseline:
            f.write(id_token + "\n")	


if __name__ == "__main__":
    process_corpus_task1("FACT2020test_task1.xml")
    process_corpus_task2("FACT2020test_task2.xml")
    generate_baseline_task2("FACT2020_train_test/FACT2020train_fixed.xml")
