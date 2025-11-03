text  = "e clavicle is S-shaped, with the medial end convex forward and the lateral end concave forward. It is widest at its medial end and thins laterally. The medial and lateral ends have flat expanses that are linked by a tubular middle, which has sparse medullary bone. The clavicle functions as a strut, bracing the shoulder from the trunk and allowing the shoulder to function at optimal strength. The medial one-third protects the brachial plexus, the subclavian and axillary vessels, and the superior lung. It is strongest in axial load. The junction between the two cross-sectional configurations occurs in the middle third and constitutes a vulnerable area to fracture, especially with axial loading. Moreover, the middle third lacks reinforcement by muscles or ligaments distal to the subclavius insertion, resulting in additional vulnerability. The distal clavicle contains the coracoclavicular ligaments.The two components are the trapezoid and conoid ligam"

# შლის ტექსტს სიტყვებად
words = text.split()
count = {}

# ეძებს თითოეულ სიტყვას ლექსიკონში და უმატებს მის სათვალავს ერთს
for word in words:
    count[word] = 1 + count.get(word, 0)

for c in count:
    print(c, count[c])