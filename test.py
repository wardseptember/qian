import os

f = open("./docs/1.md", "w+")
for filename in os.listdir("./imgs"):
    print(filename)
    content = """<div align="center"> <img src="../imgs/{}" width="400" height = "600"/> </div><br>
""".format(filename)
    f.write(content)
f.close()