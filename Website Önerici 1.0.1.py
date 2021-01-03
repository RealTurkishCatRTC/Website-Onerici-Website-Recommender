print("-Website Önerici 1.0.1'e Hoşgeldiniz! \n-Başka bir Kategoriye Bakmak için programı yeniden başlatın \n-Daha Çok Websiteler ve Kategoriler Eklenicektir\n")
soru=input("En Çok Hangisini Yapmaktan Hoşlanırsınız? \n KATEGORİLER \n -Müzik Dinlemek | Seçmek için M yazın \n -Kitap Okumak | Seçmek için K yazın \n -Oyun Oynamak | Seçmek için O yazın \n -Yemek Tariflerine Bakmak | Seçmek için Y yazın \n -Spor Yapmak | Seçmek için S yazın \n -Alışveriş Yapmak | Seçmek için A yazın \n -Film İzlemek | Seçmek için F yazın \n\n")

if soru=="M" or soru=="m":
    print("Müzik Kategorisinde Websiteler: \n music.youtube.com Not: Youtube Kullanıcıları İçin Önerilir. \n itunes.com Not: Apple Kullanıcıları İçin Önerilir. \n plaza.one Not: Vaporwave ve Lo-Fi dinlemek için bir website \n spotify.com Not: Çoğu Müzik Burada. \n iheart.com Not: Amerika dışında online dinlenemiyor olsa da, mobil uygulamaları üzerinden dinleyebildiğimiz müzik 'radyoları' topluluğudur. \n")
elif soru=="K" or soru=="k":
    print("Kitap Kategorisinde Websiteler: \n gutenberg.org Not: Kamu alanına girmiş (telif hakkı artık olmayan, bedava) 700'den fazla kitap burda. \n onlinekitapoku.com Not: Adı Üstünde. \n ekitap.ktb.gov.tr Not: Yok \n kitapsan.com.tr Not: Yok")
elif soru=="O" or soru=="o":
    print("Oyun Kategorisinde Websiteler: \n steampowered.com Not: Neredeyse tüm oyunlar Burda. Bu website dışında güvenilir website yok varsa bile kullanışlı değildir")
elif soru=="Y" or soru=="y":
    print("Yemek Kategorisinde Websiteler: \n nefisyemektarifleri.com Not: Yok")
elif soru=="S" or soru=="s":
    print("Spor Kategorisinde Websiteler: \n aspor.com.tr Not: ATV ama spor için olan. \n ntvspor.net Not: NTV ama spor için olan. \n sports.yahoo.com Not: Yok \n tr.bein.com Not: Global bir firma olan BeIN'in Türkiye'ye Özel Spor Kanalı \n ssport.tv Not: Kendilerini ''Türkiye'nin Premier Spor Kanalı'' diye tanıtırlar.")
elif soru=="a" or soru=="A":
    print("Alışveriş Kategorisinde Websiteler: \n amazon.com.tr Not: Yok \n trendyol.com Not: Yok \n ciceksepeti.com Not:Amazon'un yaptığı bir şey. \n hepsiburada.com Not: Yok")
elif soru=="F" or soru=="f":
    print("Film Kategorisinde Websiteler: \n exxen.com Not: Bu Yılın Başında açıldı. \n netflix.com Not: Kim Bilmez Ki...")
else:
    print("[ Bu Kategori Bulunamadı... ]\n[ Lütfen programı yeniden başlatın ve geçerli bir kategori seçin. ]")
    
    
 
