from googlesearch import search
def listmaker(items):
    recipes = []
    for item in items:
        recipes.append(search(item))
    return recipes

def dictionaryMaker(mainlist):
    list_of_dictionaries = []

    for item in mainlist:
        dictionary = {
            'link': item[0],
            'title': item[1],
            'img': item[2]
        }
        list_of_dictionaries.append(dictionary)
    return list_of_dictionaries

def stringmaker(list):
    mainlist = listmaker(list)
    # string = ''
    # print(mainlist)
    for i in range(len(mainlist)):
        title = mainlist[i][1]
        link = mainlist[i][0]
        img = mainlist[i][2]
    #     string+= f""" <div class="recommendation-slice">
    #         <div class="recommendation-image">
    #             <img src="{img}" alt="{title}">
    #             <div class="green-rectangle">
    #                 <div class="spoon-container">
    #                     <img class="spoon" src="static/winter-cozy-spoon-icon-by-Vexels 1.png" alt="Spoon Icon">
    #                 </div>
    #                 <p class="text">{title}</p>
    #                 <a class="link" href="{link}">{link}</a>
    #             </div>
    #         </div>
    #     </div>"""
    # print(string)
    return dictionaryMaker(mainlist)

# list1 = ['palakpaneer','dosa','idli']
# print(stringmaker(list1))