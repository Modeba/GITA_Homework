word = input()
while word != "stop":
    if word[-3:] == "ing":
        print(word + "ly")
    else:
        print(word + "ing")
    word = input()

# word = input()
# while word != "stop":
#     if word.endswith("ing"):
#         print(word + "ly")
#     else:
#         print(word + "ing")
#     word = input()