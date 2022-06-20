# ----------------------------
# --    --
# -- Simple Bookmark Manage --
# ----------------------------



myfavouritewebs = []

maximumwebs = 5


while maximumwebs > 0:
    
  # Input The New Website
    web = input("Website name without https:// ")

    # Add The New Website To The List
    myfavouritewebs.append(f"https://{web.strip().lower()}")

    maximumwebs -= 1

    print(f"website added, {maximumwebs} place left")


else :

    print("Bookmark is full, you can't add more")

if len(myfavouritewebs) > 0 :


    myfavouritewebs.sort()

    index = 0
    print("Printing The list of websites in your bookmark")

    while index < len(myfavouritewebs) :

        print(myfavouritewebs[index])
        
        index += 1



















     
