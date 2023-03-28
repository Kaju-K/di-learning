# Challenge 1

word = input("Write a word: ")
word_set = set(word)

indexing_dict = {}

for letter in word_set:
    index = 0
    for i in range(word.count(letter)):
        try:
            indexing_dict.get(letter).append(word.index(letter, index))
        except:
            indexing_dict[letter] = [word.index(letter, index)]
        index = word.index(letter, index) + 1

print(indexing_dict)

# Challenge 2

def conversion_money_str_to_int(money_str):
    return int(money_str[1:].replace(",", ""))

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

can_buy = []

for item in items_purchase:
    if conversion_money_str_to_int(wallet) >= conversion_money_str_to_int(items_purchase[item]):
        can_buy.append(item)

if can_buy:
    print(f"These are the products that you can buy: {sorted(can_buy)}")
else:
    print("You cannot buy anything")