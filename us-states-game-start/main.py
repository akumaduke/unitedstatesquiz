import turtle
import pandas

ekran = turtle.Screen()
ekran.title(" akuQuizz")
image= "./imaj.gif"
ekran.addshape(image)
turtle.shape(image)
done=pandas.read_csv("50_etats.csv")
etats= done.etat.to_list()

lis_etat=[]


while len(lis_etat)< 50:
    repons= ekran.textinput(title=f"ou devine {len(lis_etat)}/50", prompt= "bay on nom etat zanmi").title()

    if repons == "Soti":
        etat_manquant =[]
        for etat in etats:
            if etat not in lis_etat:
                etat_manquant.append(etat)
        pa_jwenn=pandas.DataFrame(etat_manquant)
        pa_jwenn.to_csv("etats_a_apprendre.csv")
        break
    if repons in etats:
        lis_etat.append(repons)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        etat_bon=done[done.etat==repons ]
        t.goto(int(etat_bon.x), int(etat_bon.y))
        t.write(repons)



