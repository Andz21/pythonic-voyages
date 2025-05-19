# 6. Write all content of a file into a new file by skipping line number 5

with open("test.txt","r") as file:
    data = file.readlines()  # returns a list

with open("new_test.txt","w") as new_file:
      for i,content in enumerate(data):
          if i != 4:
              new_file.write(content)



