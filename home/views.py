from django.shortcuts import render
import connBD


def listHotel():
    c = connBD.connectBD()
    with c.cursor() as select:
        sql = 'select * from tbhoteis'
        select.execute(sql)
        result = select.fetchall()
    c.close()
    return result


def namesImg(dicNames):
    names = []
    for name in dicNames:
        names.append(name['name'].lower().replace(' ', '_'))
    return names


def index(request):
    return render(request, 'home/index.html', {'hotels': listHotel(), 'nameImgs': namesImg(listHotel())})
