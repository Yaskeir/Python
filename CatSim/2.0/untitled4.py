middleCatsx = []
middleCatsy = []
for middleCat in middleCats:
    middleCatsx.append(middleCat.positionsX)
    middleCatsy.append(middleCat.positionsY)
    
plt.plot(middleCatsx, middleCatsy, 'r', label="a")

mousex = []
mousey = []
for mouse in mice:
    mousex.append(mouse.positionsX)
    mousey.append(mouse.positionsY)
       
plt.plot(mousex, mousey, 'b', label="b")

kittenx = []
kitteny = []
for kitten in kittens:
    kittenx.append(kitten.positionsX)
    kitteny.append(kitten.positionsY)

plt.plot(kittenx, kitteny, 'g')

lazyCatsx = []
lazyCatsy = []
for lazyCat in lazyCats:
    lazyCatsx.append(lazyCat.positionsX)
    lazyCatsy.append(lazyCat.positionsY)
 
plt.plot(lazyCatsx, lazyCatsy, 'y', label="a")
plt.legend( title="Legenda", bbox_to_anchor=(1, 0.5))

plt.title('Wykres ')
plt.show()
