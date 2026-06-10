def main():
    entry = input("What time is it? ")
    result=convert(entry)
    if 8>=result>=7 :
        print ("breakfast time")

    if 13>=result>=12  :
        print("lunch time")

    if 19>=result>=18  :
        print("dinner time")
def convert(time):
    hours, minutes = time.split(":")
    if "a.m." in minutes :
        min , abc = minutes.split(" ")
        newmin= float(min)/60
        return float(hours) + newmin
    elif "p.m." in minutes and float(hours)!=12 :
        hours= float(hours)+12
        min , abc = minutes.split(" ")
        newmin= float(min)/60
        return float(hours) + newmin
    else:
        newmin= float(minutes)/60
        return float(hours) + newmin
if __name__ == "__main__":
    main()
