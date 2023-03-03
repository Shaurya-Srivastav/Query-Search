try: 
    from googlesearch import search
except ImportError: 
    print("No module found")

#searching the web
query = input("Enter Your Query: ")

for j in search(query, stop=1, pause=2):
    print(j)