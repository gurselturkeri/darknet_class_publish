sola_donulmez_levha = None
sola_mecburi_levha = None
kirmizi_isik_levha = None
yesil_isik_levha = None
durak_levha = None
girisi_olmayan_yol_levha = None
saga_mecburi_levha = None
kavsak_levha = None
park_levha = None
engelli_park_levha = None
park_yasak_levha = None


def YoloFunc(data):
    

    for box in data.bounding_boxes:
        
        if(box.Class=="sola_donulmez" and box.probability>0.80):   
            global sola_donulmez_levha
            sola_donulmez_levha=1     
            print("sola_donulmez")

        if(box.Class=="sola_mecburi" and box.probability>0.80):
            global sola_mecburi_levha
            sola_mecburi_levha=1 
            print("sola_mecburi")

        if(box.Class=="kirmizi_isik" and box.probability>0.80):
            global kirmizi_isik_levha
            kirmizi_isik_levha=1 
            print("kirmizi_isik")

        if(box.Class=="yesil_isik" and box.probability>0.80):
            global yesil_isik_levha
            yesil_isik_levha=1 
            print("yesil_isik")

        if(box.Class=="durak" and box.probability>0.80):
            global durak_levha
            durak_levha=1 
            print("durak")

        if(box.Class=="girisi_olmayan_yol" and box.probability>0.80):
            global girisi_olmayan_yol_levha
            girisi_olmayan_yol_levha=1 
            print("girisi_olmayan_yol")

        if(box.Class=="saga_mecburi" and box.probability>0.80):
            global saga_mecburi_levha
            saga_mecburi_levha=1 
            print("saga_mecburi")

        if(box.Class=="ada_etrafinda_donunuz" and box.probability>0.80):
            global kavsak_levha
            kavsak_levha=1 
            print("ada_etrafinda_donunuz")

        if(box.Class=="park" and box.probability>0.80):
            global park_levha
            park_levha=1 
            print("park")

        if(box.Class=="engelli_park" and box.probability>0.80):
            global engelli_park_levha
            engelli_park_levha=1 
            print("engelli_park")

        if(box.Class=="park_yasak" and box.probability>0.80):
            global park_yasak_levha
            park_yasak_levha=1 
            print("park_yasak")




def SolaDonulmez():
    print("Fonksiyona girdi")

def SolaMecburi():

def KirmiziIsik():

def YesilIsik():

def Durak():

def GirisiOlmayanYol():

def SagaMecburi():

def AdaEtrafindaDonunuz():

def Park():

def EngelliPark():
def ParkYasak(): 
