from my_sites import sites, open_site

print("Favorite Websites Menu:")
for number in sites:
    print(number, "-", sites[number][0])

choice = int(input("Enter a number: "))

if choice in sites:
    url = sites[choice][1]
    open_site(url)
else:
    print("Invalid choice.")
