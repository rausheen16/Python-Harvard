def convert(entry):
    if "Hello :)" in entry:
       result= entry.replace("Hello :)","Hello 🙂")
    if "Goodbye :(" in entry:
       result= entry.replace("Goodbye :(","Goodbye 🙁")
    if "Hello :) Goodbye :(" in entry:
        result= entry.replace("Hello :) Goodbye :(" , "Hello 🙂 Goodbye 🙁" )
    print (result)



def main():
    entry = input("type your entry ")
    convert(entry)


main()

