# Free-İnternet(Özgür İnternet)
#Free-Network

[!CAUTION]
>FR Version:1.0 Compliler V:0.6

> [!CAUTION]
> Kaspersky isimli antivirüs yazılımı Rus hükümetiyle olan anlaşmasından dolayı GoodbyeDPI'ın çalışmasına engel olmaktadır. Kaspersky isimli yazılımı kullanıyorsanız, kullandıysanız veya devre dışı halde bile olsa bilgisayarınızda bulunuyorsa lütfen tamamen kaldırın. Bunu yapmadığınız taktirde GoodbyeDPI çok yüksek ihtimalle çalışmayacaktır. Kaspersky yerine alternatif antivirüs yazılımları tercih edebilir ya da Windows Defender kullanabilirsiniz. (Windows Defender 2025 yılı itibariyle kötü amaçlı yazılım ve siteleri engellemekte son derece yeterlidir.)
Kaspersky'i GoodbyeDPI ZIP dosyasının indirme işlemi sırasında devre dışı bırakmanız, indirdikten sonra dışlamalara eklemeniz veya devre dışı bırakmanız sorunu çözmeyecektir. GoodbyeDPI'ı doğru şekilde kullanabilmek için Kaspersky isimli antivirüs yazılımından bir şekilde kurtulmalısınız.
>
> ## Özet​
Bu proje Discord ve diğer engelli site ve uygulamalara VPN'siz ve internet hızında yavaşlama olmadan girmek için GoodbyeDPI'ın düzenlenmiş GUİ destekli bir versiyonudur.

> [!NOTE]  GoodbyeDPI
> Windows 7, 8, 8.1, 10 veya 11 işletim sistemlerinde **yönetici olarak çalıştırmanız** mecburidir.
> [!CAUTION] Free Network adlı GoodbyeDPI alt yapılı  GUI versionudur
>  GoodbyeDPI aracında Windows 7, 8, 8.1, 10 veya 11 işletim sistemlerinde **yönetici olarak çalıştırmanız** mecburi iken
> Free Networkde yönetici olarak çalıştırmanız gerekmez  tek tıkla butona basarak çalıştırabilirsiniz fakat FR Terminalini kullanarak
> GoodbyeDPI frameworkünü  indirmeniz gerekmektedir
> indirdiğiniz zaman butonlara basarak veya FR terminalde command yazarak Discord ve diğer engelli site ve uygulamalara VPN'siz ve internet hızında yavaşlama olmadan girebilirsiniz
>
>  [!NOTE]
> **[VirusTotal sonuçlarında](https://www.virustotal.com/gui/file/3ca863444ce065361b1152e1dddae1147962fc78b90c17ff346efbb35bd146ee)** 73 adet antivirüs progamı içerisinde (bağlantıyla yönlendirileceğiniz sayfada 66 adet antivirüs programı bulunmakta çünkü bazıları ``.zip`` dosyalarını online taramayı desteklememekte) yalnızca Kaspersky isimli uygulama bu yazılımın zararlı olduğunu söylemektedir ancak bu hatalı bir uyarıdır (yukarıdaki uyarıyı okuyunuz). **Dolayısıyla Kaspersky kullanıyorsanız ya devre dışı bırakmanız ya da antivirüs programınızı değiştirmeniz önerilir.**

> [!IMPORTANT]
> WinDivert dosyalarının açıklamalarında ya da silmeye çalışırken karşılaşacağınız Bitcoin adresi sizi korkutmasın.
WinDivert açık kaynaklı bir Windows Paket İnceleme-Değiştirme aracı kütüphanesidir. Bu kütüphanenin sahibi [basil00](https://github.com/basil00) isminde bir geliştiricidir. Bu geliştirici tamamen ücretsiz ve açık kaynak kodlu şekilde bu kütüphaneyi [Github - Windivert](https://github.com/basil00/WinDivert) isimli Github repository'sinde paylaşmaktadır.
Bu geliştirici tamamen ücretsiz şekilde yayınladığı bu kütüphaneden hiçbir gelir elde etmemekte ancak kendisine gelecek bağışları da kabul etmektedir. Bağış yapılacak adres ise .dll ve .sys dosyalarının açıklamalarında bulunuyor. Yani gördüğünüz Bitcoin yazısı ve yanındaki karmaşık sayılar ve harflerden oluşan adres WinDivert kütüphanesinin geliştiricisi olan basil00'a ait bağış yapabileceğiniz **Bitcoin cüzdan adresidir.** Bu adresi resmi sitesinde de paylaşıyor, [bu da bağış sayfasının linki](https://reqrypt.org/donate.html).

## Free Network kullanımı
uygulama exe dosyası olduğundan tek tıkla kurulum başlıyor ardından önünüze seçenekler geliyor o seçenekler hizmeti kurarak kullanma   bu seçenek(service_install_dnsredir_turkey) cihazınız açıldığında otomatik discorda ve diğer yasaklı uygulamalara girebilmenizi sağlar
bir diğer seçenek ise  yasaklı uygulamalara girebilmek için her seferinde  "turkey_dnsredir_cmd" adlı butona basarak etkinleştirmenizdir arkada batch dosyası çalışır işiniz bittiğinde bu batch dosyasını  kapatabilirsiniz  hatta Free Network uygulamasınıda  kapatabilirsiniz
Servisi silmek için "service_remove_cmd_path" adlı butona tıklamanız  bu butona tıkladığınızda servis silinir ve her  cihazınızı aç kapa yaptığınızda    yasaklı  uygulamalara erişemeyeceksiniz manuel olarak başlatmanız yada servisi tekrar kurmanız gerekmektedir
> [!IMPORTANT]
> exeyi çalıştırır çalıştırmaz hemen butonlara basarsanız hiçbirşey olmaz çünkü GoodbyeDPI kurulmamıştır bunu kurmak için FR Terminal eklentisini Appdata-Roaming-Free İnternet-Termınal  bölümüne (MoonDevelop web sitemden güncellemelerini indirebilirsiniz) dist,build klasörülerini ve .spec dosyasını Termınal klasörüne  koymalısınız terminalin çalışması için dosylar:dosya ekle
 
##FR Terminal kullanımı ve commandlar
FR terminal GoodbyeDPI turkeyi indirmeniz  veya başka işlemler yapmanız için geliştirilen terminaldir
[!NOTE]
Command:"fr install goodbyedpiTR"  tırnak içindeki commandı yazarak goodbyedpiTR yi kurabilir ve butonlara basarak çalıştırabilirsiniz
Command:"gbdt -run ~comme turkey_dnsredir.cmd" ırnak içindeki commandı yazarak  servisi kurmadan  yasaklı uygulamalara erişebilirsiniz ama  yasaklı uygulamalara her gireceğinizde  bu kodu yazabilir veya ana menüdeki "turkey_dnsredir_cmd" butonuna basmalısınız
unutmayın bilgisayarınızı aç kapa yaptığınızda eğer servisi kurmadısyanız  bunu sürekli yapmalısınız tabi yasaklı uygulamalara girecek iseniz.
Command:"gbdt -run ~comme service_remove.cmd" tırnak içindeki commandı yazarakgoodbyedpiTR servisini kurabilirsiniz  veya ana menüdeki bu butona basa bilirsiniz "service_install_dnsredir_turkey"  böylece manuel olarak sürekli açmanız gerekmez
kendi cihazınız otomatik açtığınızda devreye girer
Command:"gbdt -run ~comme service install ~turkey" yazarak servisi kaldırabilirsiniz ama yasaklı uygulamalara gireceğiniz zaman ya manuel yada servisi tekrar kurmanız gerekmektedir veya direkt ana menüdeki bu butona basabilirsiniz "service_remove_cmd_path" 

> [!IMPORTANT]
> Alternatifler bir sonraki güncellemede eklenecektir bu uygulama geliştirilecektir teşekkürler


[!NOTE]
Bu uygulamayı geliştirirken https://github.com/cagritaskn/GoodbyeDPI-Turkey bu githubdaki cagritasknın dosyalarını kullandım  ben sadece  kullanımı birazdaha kolaylaştırmaya çalıştım
Teşekkürler:

Destek
Bu programı kullanmak tamamen ücretsizdir. Kullanımından herhangi bir gelir elde etmiyorum. ☺

## Yasal Uyarı
>
> [!IMPORTANT]
> Bu uygulamanın kullanımından doğan her türlü yasal sorumluluk kullanan kişiye aittir. Uygulama yalnızca eğitim ve araştırma amaçları ile yazılmış ve düzenlenmiş olup; bu uygulamayı bu şartlar altında kullanmak ya da kullanmamak kullanıcının kendi seçimidir. Açık kaynak kodlarının paylaşıldığı bu platformdaki düzenlenmiş bu proje, bilgi paylaşımı ve kodlama eğitimi amaçları ile yazılmış ve düzenlenmiştir.
