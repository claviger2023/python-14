articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    find_results = []
    if not letter_case:
        key = key.lower()
        for k in articles_dict:
            title_author = k.get("title") + ' ' + k.get("author")
            title_author = title_author.lower()
            if title_author.find(key) != -1:
                find_results.append(k)
    else:
        for k in articles_dict:
            title_author = k.get("title") + ' ' + k.get("author")
            if title_author.find(key) != -1:
                find_results.append(k)
    return find_results

print(find_articles("ocean"))

      
    
        
        
        
            
        
        
            
        
        
            
        
        
            
        
            
    