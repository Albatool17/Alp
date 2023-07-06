'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
print(Sentence)
#the items will be printed
print(Sentence[1])
#look will be items
Sentence.append("life")
#life will be added to the items
Sentence[4] = "sunny"
#sunny will replace bright
print(Sentence[4])
#sunny will be printed
print(Sentence[0] + " " + Sentence[3])
#always and space willl be added and then the will printed
print(Sentence)
#the setence will be printed with the changes