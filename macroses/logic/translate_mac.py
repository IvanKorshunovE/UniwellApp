def remove_space_before_paragraphs(text):
    return text.replace('\n ', '\n')

text = " \nHello, this is the first paragraph. \n\n This is the second paragraph. \n\n\n And this is the third."
text = remove_space_before_paragraphs(text)
print(text)