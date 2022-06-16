import os

f = open("./docs/1.md", "w+")
for filename in os.listdir("./imgs"):
    print(filename)
    content = """![](../imgs/{})
""".format(filename)
    f.write(content)
f.close()