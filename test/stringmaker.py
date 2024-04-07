from googlesearch import search
def stringmaker(items):
    recipes = []
    for item in items:
        recipes.append(search(item))
    return recipes


sample = ['palak paneer','paneer butter masala','mattar paneer']
mainlist = stringmaker(sample)
string = ''
for i in range(len(mainlist)):
    title = mainlist[i][1]
    link = mainlist[i][0]
    img = mainlist[i][2]
    string+= f""" <div class="recommendation-slice">
        <div class="recommendation-image">
            <img src="{img}" alt="Onion Rings">
            <div class="green-rectangle">
                <div class="spoon-container">
                    <img class="spoon" src="static/winter-cozy-spoon-icon-by-Vexels 1.png" alt="Spoon Icon">
                </div>
                <p class="text">{title}</p>
                <a class="link" href="{link}">{link}</a>
            </div>
        </div>
    </div>"""
print(string)


