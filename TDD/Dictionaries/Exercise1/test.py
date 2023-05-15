import os

def get_name_path_file(name_file: str) -> str:
    file_path = os.path.abspath(name_file)
    return "The name of file is: " + name_file + "\n" + "The path of file is: " + file_path

def open_count_frecuency_file(name_file: str) -> None:
    file = open(name_file, "r")
    content = file.read()
    words = content.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    for word in sorted(frequency):
        print(word, "---", frequency[word])
    
