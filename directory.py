class Directory():
    providers={}
    l = get_all()
    def __init__(self):
        self.providers["airtel"]=["9900","9800","9811"]
        self.providers["BSNL"]=["9440","9822"]
        self.providers["Idea"]=["9848","9912"]
        self.providers["Reliance"]=["9300","9812"]
    def get_filter(self):
        for i in range (len(l)):
            if   s in l[i].get_emailid:
                print l[i].__dict__
    def get_provider_name(self,phonenumber):
        string1=phonenumber(0,3)
        for a,v in  providers:
            if string1 in v:
                print a
    def get_records_of_provider(self,provider):
        list2=providers(provider)
        list3=[]
        for i in range (len(l)):
            string2=l[i].get_phonenumber()
            if string2 in list2:
                list3.append(l[i])
            print list3
    def get_contacts(self):
        for i in range (len(l)):
            if phonenumber==l[i].get_phonenumber:
                print l[i].__dict__







