adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

## OVERWRITE the content of the adwentures_of_tom_sawer variable in tasks 1-3
# task 01 ==
""" The data in the adwentures_of_tom_sawer string is split randomly due to an error.
Need to replace the end of the paragraph with a space: .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Replace .... with a space.
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Ensure there is no more than one space between words in the text.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Output how many times the letter "h" appears in the text.
"""
count_h = adwentures_of_tom_sawer.count("h")
print(count_h)

# task 05
""" Output how many words in the text start with a Capital letter.
"""

word_list = adwentures_of_tom_sawer.split()
c_letter_count = sum(1 for word in word_list if word[0].isupper())
print(f"Count of capital letter is:{c_letter_count}")

# task 06
""" Output the position where the word "Tom" occurs for the second time.
"""

first_tom = adwentures_of_tom_sawer.find("Tom")
second_tom = adwentures_of_tom_sawer.find("Tom", first_tom + 1)
print(second_tom)


# task 07
""" Split the adwentures_of_tom_sawer variable by the end of the sentence.
Save the result in the adwentures_of_tom_sawer_sentences variable.
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Output the fourth sentence from adwentures_of_tom_sawer_sentences.
Convert the string to lowercase.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
print(fourth_sentence.lower())


# task 09
""" Check if any sentence starts with "By the time".
"""
for check_sentence in adwentures_of_tom_sawer_sentences:
    if check_sentence.strip().startswith("By the time"):
        print(f"Found sentence!")
        print(f"Here: {check_sentence.strip()}")
        break
else:
    print(f"Sentence not found.")

# task 10
""" Output the number of words in the last sentence of adwentures_of_tom_sawer_sentences.
"""
clean_sentences = [s for s in adwentures_of_tom_sawer_sentences if s.strip()]
last_sentence = clean_sentences[-1]
word_count = len(last_sentence.split())
print(f"Last sentence: {last_sentence}")
print(f"Number of words in the last sentence:{word_count}")
