def manipulate_sentence():
    # Given sentence
    sentence = "Learning Python is fun and rewarding."
    
    # a. Extract the substring "Python is fun" using negative slicing
    substring = sentence[-28:-14]  # "Python is fun"
    print("Extracted substring:", substring)
    
    # b. Modify the original string by replacing "rewarding" with "exciting"
    modified_sentence = sentence.replace("rewarding", "exciting")
    print("Modified sentence:", modified_sentence)
    
    # c. Insert the phrase " Keep practicing!" after "exciting" programmatically
    insert_position = modified_sentence.find("exciting") + len("exciting")
    final_sentence = modified_sentence[:insert_position] + " Keep practicing!" + modified_sentence[insert_position:]
    print("Final sentence after insertion:", final_sentence)
    
    # d. Capitalize the first letter of each word in the final output
    capitalized_sentence = final_sentence.title()
    print("Capitalized sentence:", capitalized_sentence)

# Call the function
manipulate_sentence()
