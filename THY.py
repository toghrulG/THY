class ucus():
    havayolu = "THY"

ucus1 = ucus()

#ucus1.havayolu >> 'THY'

class ucus ():
    havayolu = "THY"

    def __init__(self,kod,qalxıs,enis,vaxt,kapasite,sernisin):
        self.kod = kod
        self.qalxıs = qalxıs
        self.enis = enis
        self.vaxt = vaxt
        self.kapasite = kapasite
        self.sernisin = sernisin

    def __repr__(self):
        return "{} sefer sayili ucus sistemde yaradilmisdir..".format(self.kod)

#ucus3       

ucus2 = ucus('TK123', 'IST', 'ANK', '60', '300','50')

#ucus2.qalxıs >> 'IST'

ucus3 = ucus('TK321', 'BOD', 'ANT', '40', '250','300')

    def anons_yap(self):
        return "{} sefer sayili {}-{} ucusumuz {} deq surecek".format (
            self.kod
            self.qalxis
            self.enis
            self.vaxt)
        
 #ucus3.anons_yap() >> 'TK321' sefer sayili BOD-ANT ucusumuz 40 deq surecek

    def oturacaq_sayin_yenile (self):
        return self.kapasite - self.sernisin

    def bilet_satis(self,bilet_ededi=1):
        if self.sernisin + bilet_ededi <= self.kapasite:
            self.sernisin += bilet_ededi
            self.oturacaq_sayin_yenile()
            print('{} eded bilet satilmisdir. 
            qalan oturacaq sayi {}'.format(bilet_ededi, self.oturacaq_sayin_yenile()))

        else:
            print('emeliyyat heyata kecmedi.yetersiz oturacaq sayi')    


    def bilet_iptal (self,bilet_ededi=1):
        if self.sernisin >= bilet_ededi
        self.sernisin -= bilet_ededi
        print('{} eded bilet legv olunub.yeni oturacaq 
        sayi {}'.format(bilet_ededi,self.oturacaq_sayin_yenile()))

    else:
        print('emeliyyat heyata kecmedi.legv olunacaq qeder sernisin yoxdur)


#ucus3.bilet_satis(5) >> 5 eded bilet satilmisdir.qalan oturacaq sayi 250
