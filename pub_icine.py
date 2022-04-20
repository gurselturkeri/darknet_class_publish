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

        global sola_donulmez_levha
        global sola_mecburi_levha
        global kirmizi_isik_levha
        global yesil_isik_levha
        global durak_levha
        global girisi_olmayan_yol_levha
        global saga_mecburi_levha
        global kavsak_levha
        global park_levha
        global engelli_park_levha
        global park_yasak_levha    


        if(box.Class=="sola_donulmez" and box.probability>0.80):   
            sola_donulmez_levha=True       
        else:   
            sola_donulmez_levha=False


        if(box.Class=="sola_mecburi" and box.probability>0.80):  
            sola_mecburi_levha=True
        else:
            sola_mecburi_levha=False       

        if(box.Class=="kirmizi_isik" and box.probability>0.80):           
            kirmizi_isik_levha=True
        else:
            kirmizi_isik_levha=False

        if(box.Class=="yesil_isik" and box.probability>0.80): 
            yesil_isik_levha=True
        else:
            yesil_isik_levha=False

        if(box.Class=="durak" and box.probability>0.80): 
            durak_levha=True
        else:
            durak_levha=False

        if(box.Class=="girisi_olmayan_yol" and box.probability>0.80):
            girisi_olmayan_yol_levha=True
        else:
            girisi_olmayan_yol_levha=False

        if(box.Class=="saga_mecburi" and box.probability>0.80):
            saga_mecburi_levha=True
        else:
            saga_mecburi_levha=False

        if(box.Class=="ada_etrafinda_donunuz" and box.probability>0.80):
            kavsak_levha=True
        else:
            kavsak_levha=False

        if(box.Class=="park" and box.probability>0.80):
            park_levha=True
        else:
            park_levha=False

        if(box.Class=="engelli_park" and box.probability>0.80):
            engelli_park_levha=True
        else: 
            engelli_park_levha=False

        if(box.Class=="park_yasak" and box.probability>0.80):
            park_yasak_levha=True
        else:
            park_yasak_levha=False




def SolaDonulmez():
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
