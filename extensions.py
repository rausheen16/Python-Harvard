file=input("enter file name ")
newfile= file.strip().lower()
if ".gif" in newfile:
    print ("image/gif")
elif ".jpg" in newfile:
    print ("image/jpeg")
elif "jpeg" in newfile:
    print ("image/jpeg")
elif ".png" in newfile:
    print("image/png")
elif ".pdf" in newfile:
    print("application/pdf")
elif ".txt" in newfile:
    print("text/plain")
elif ".zip" in newfile:
    print("application/zip")
else:
    print("application/octet-stream")

