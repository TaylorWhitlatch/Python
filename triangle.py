height = int(raw_input("Enter tri height"))
for i in range(1,height):
    spaces = (height - i) * " "
    stars = (i * 2 - 1) * "*"
    print spaces + stars + spaces
