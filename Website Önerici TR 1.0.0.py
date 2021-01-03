print("-Website Önerici 1.0.0'a Hoşgeldiniz!- \nDaha Çok Websiteler ve Kategoriler Eklenicektir.")
soru=input("En Çok Hangisini Yapmaktan Hoşlanırsınız? \n KATEGORİLER \n -Müzik Dinlemek | Seçmek için M yazın \n -Kitap Okumak | Seçmek için K yazın \n -Oyun Oynamak | Seçmek için O yazın \n -Yemek Tariflerine Bakmak | Seçmek için Y yazın \n")

if soru=="M" or soru=="m":
    print("Müzik Kategorisinde Websiteler: \n music.youtube.com Not: Youtube Kullanıcıları İçin Önerilir. \n itunes.com Not: Apple Kullanıcıları İçin Önerilir. \n plaza.one Not: Vaporwave ve Lo-Fi dinlemek için bir website \n spotify.com Not: Çoğu Müzik Burada. \n iheart.com Not: Amerika dışında online dinlenemiyor olsa da, mobil uygulamaları üzerinden dinleyebildiğimiz müzik 'radyoları' topluluğudur. \n")
elif soru=="K" or soru=="k":
    print("Kitap Kategorisinde Websiteler: \n gutenberg.org Not: Kamu alanına girmiş (telif hakkı artık olmayan, bedava) 700'den fazla kitap burda. \n onlinekitapoku.com Not: Adı Üstünde. \n ekitap.ktb.gov.tr Not: Yok")
elif soru=="O" or soru=="o":
    print("Oyun Kategorisinde Websiteler: \n steampowered.com Not: Neredeyse tüm oyunlar Burda. Bu website dışında güvenilir website yok varsa bile kullanışlı değildir")
elif soru=="Y" or soru=="y":
    print("Yemek Kategorisinde Websiteler: \n nefisyemektarifleri.com Not: Yok")
else:
    print("Bulunamadı... lütfen programı yeniden başlatın.")
