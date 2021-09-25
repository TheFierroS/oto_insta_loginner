from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Program açık kaynak kod olduğu için hesabım çalınır mı diye korkmayın zaten programı kendi bilgisayarınızda çalıştırıyorsunuz :)
username = input("Lütfen Kullanıcı Adı, Telefon Numarası veya E-Posta Adresinizi Giriniz : ") #kullanıcı adı girişi
password = input("Lütfen Şifrenizi Giriniz : ") #şifre girişi
dogrulama = input("Çift Haneli Doğrulamanız Aktif mi ? E/H : ") #çift haneli doğrulama sorgusu
 
driver = webdriver.Firefox() #Eğer Chrome Tarayıcısı Kullanıyorsanız Firefox yazan kısmı Chrome olarak değiştirin
driver.maximize_window()

#seleium ile ilgili kısım
driver.get("https://www.instagram.com/accounts/login/") #burda selenium ile tarayıcımızda istediğimiz adresi açıyoruz.

time.sleep(5) #sayfa kaynagının tam anlamıyla yüklenmesi ve hata vermemesi için 5 saniye bekliyoruz

kullaniciAdi = driver.find_element_by_name("username") #kullanıcı adı yazacagımız kısmın sayfa kaynagında bulunması
sifre = driver.find_element_by_name("password") #şifre yazacagımız kısmın sayfa kaynagında bulunması
button = driver.find_element_by_class_name("y3zKF") #giriş yap butonunun sayfa kaynagında bulunması

kullaniciAdi.click()
kullaniciAdi.send_keys(username) #girdiğiniz kullanıcı adının sayfada yerine yazılması işlemi

sifre.click()
sifre.send_keys(password) #girdiğiniz şifrenin sayfada yerine yazılması işlemi

button.click() #giriş yap butonuna tıklama işlemi

time.sleep(5) #giriş yap butonuna bastıktan sonra adres değişikliği olacagı için üstteki 5 saniye bekleme işlemiyle aynı mantıkta

if dogrulama == "E" or dogrulama == "e":
    code = input("Lütfen Telefonunuza Gelen Doğrulama Kodunu Giriniz : ") #çift haneli döğrulama için sms kodu girişi
    securitCode = driver.find_element_by_name("verificationCode") #kodun girileceği yerin sayfa kaynagında bulunması
    securitCode.click()
    securitCode.send_keys(code) #kodun yerine yazılması işlemi
    secondButton = driver.find_element_by_class_name("y3zKF")
    secondButton.click() #kodu girdikten sonra altındaki butona tıklayarak sizi instagrama yönlendirir :)

elif dogrulama == "H" or dogrulama == "h":
    pass

else:
    pass

#İyi Kullanımlar 
