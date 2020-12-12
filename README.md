# Python---JSON-to-Dictionary

Name: Generate structure
ID:6
Difficulty: B
Propose: TDY

Creati un script care primeste de la linia de comanda un path catre un director si un fisier
JSON. In fisierul JSON se afla un dictionar in care se afla o structura de directoare si fisiere
astfel: fiecare cheie care are ca valoare un dictionar este un director iar dictionarul contintul,
iar fiecare cheie care are ca valoare un string reprezinta un fisier iar string-ul respectiv este
continutul fisierului. Scriptul va crea in folderul dat ca argument directoarele si fisierele
conform dictionarului din JSON.

INPUT: create_structure.py root_folder_path structure_json_file_path
Exemplu de dictionar:
{“dir1” : {“dir2”: {“file1”: “continut1”, “file2”: “continut2”}, “file3”: “continut3”}, “file4”: “continut4”}
OUTPUT:
root_folder
---dir1
------dir2
---------file1: continut1
---------file2: continut2
------file3: continut3
---file4: continut4
