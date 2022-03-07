with open("README.md", "r+") as file:
    text : str = file.read()
    
new_text = ""    
    
lines = text.split("\n")
current_text = ""
for i in range(len(lines)):
    if lines[i] == "#":
        current_text = f"# {lines[i + 1]}\n{lines[i + 2]}\n"
        new_text += current_text
    
with open("teste.md", "w") as file:
    file.write(new_text)