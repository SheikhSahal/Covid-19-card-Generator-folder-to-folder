import pandas as pd
df = pd.read_csv('./static/log.csv')

re = str(df)
# print(len(str(df.values[18])))
print(re)

print("Number of rows ", len(df.index))

## If you want the column and row count then

row_count, column_count = df.shape

print("Number of rows ", row_count)
print("Number of columns ", column_count)  

# def insertNewlines(text, lineLength):

#     if len(text) <= lineLength:
#         return text
#     else:
#         return text[:lineLength] + '\n' + insertNewlines(text[lineLength:], lineLength)

# text = "Given text and a desired line length, wrap the text as a typewriter would. Insert a newline character  '\\n' after each word that reaches or exceeds the desired line length."
# print (insertNewlines(text, 15))


# import random

# print(random.randint(3, 100000000000))

# import os
# #providing the path of the folder
# #r = raw string literal
# def remove_images():
#     folder_path = (r'./static/')
#     #using listdir() method to list the files of the folder
#     test = os.listdir(folder_path)
#     #taking a loop to remove all the images
#     #using ".png" extension to remove only png images
#     #using os.remove() method to remove the files
#     for images in test:
#         if images.endswith(".png"):
#             os.remove(os.path.join(folder_path, images))