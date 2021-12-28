python = "https://asdfjklasjflkjeee.com"
rule1 = python[python.find("//")+2: python.find("//")+5]
rule2 = len(python[python.find("//")+2: python.find(".")])
rule3 = python.count("e")
print(f"생성된 비밀번호: {rule1}{rule2}{rule3}!")
