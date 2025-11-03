text = input()
if "small" in text:
    print("small")
elif "tall" in text:
    print("tall")
elif "middle" in text:
    print("middle")
else:
    print("Arcerti ar moidzebna")

# text = input()
# def new_func(text):
#     word1 = "small"
#     word2 = "tall"
#     word3 = "middle"

#     for i in range(len(text)):
#         for e in range(len(word1)):
#             if i + e > len(text) or text[i + e] != word1[e]:
#                 break
#         else:
#             print(word1)
#             break

#         for e in range(len(word2)):
#             if i + e > len(text) or text[i + e] != word2[e]:
#                 break
#         else:
#             print(word2)
#             break

#         for e in range(len(word3)):
#             if i + e > len(text) or text[i + e] != word3[e]:
#                 break
#         else:
#             print(word3)
#             break

# new_func(text)