o
    [mêbrÇ  ã                   @   s$  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ dZ	dZ
dZdZdZdZd	Ze d
Ze dZe dZe dZe dZg d¢ZdZdZdZed ZddiZdd Zdd Zdd Zdd Zdd Zd d! Z d"d# Z!d$d% Z"d&d' Z#d(d) Z$d*d+ Z%e  e  e  dS ),é    N)ÚTimeoutz[31mz[32mz[33mz[34mz[35mz[2;37mz[0mz[1;47mz[1;41mz[1;42mz[1;43mz[1;44m)Z05d5015259730682de8b542355525b16ab7026c976a72993dZ(83e338e3a43cdcc649a1ea49957d2c0223b601bbZ(36a4ce62890b18e216951bb2cf4b9748129418f8z1.5z    u   â£  â£â£  â£â£ uÿ   âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââz
User-AgentzjOpera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54c                   C   s&   t jdkrt d¡ d S t d¡ d S )NÚwin32ÚclsÚclear)ÚsysÚplatformÚosÚsystem© r
   r
   úMailFinder.pyr      s   
r   c                  C   sÒ   t jd } t jj}t d|  ¡ t d¡ t d|  ¡ z4|dkr+t d|  ¡ W d S |dkr9t d|  ¡ W d S |d	krGt d|  ¡ W d S t d|  ¡ W d S    tt t d
t	 dt dt	 d	 Y d S )Nr   zrm -rf zOwget https://github.com/mishakorzik/MailFinder/blob/main/MailFinder.py?raw=truezmv MailFinder.py?raw=true Ú3zpython3 Ú2zpython Ú1ú[ú!ú]zL Error! Failed to start MailFinder check if python is installed correctly...)
r   ÚargvÚversion_infoÚmajorr   r	   ÚprintÚspaceÚbÚw)Úscript_nameZ
version_pyr
   r
   r   Úupdate"   s   

*r   c                   C   s6   t d t d¡ t  tjtjtjgtj¢R   d S )Nz?{space}{b}[{w}01{b}]{w} Error! You forgot to write something...é   )	r   ÚtimeÚsleepr   r   Úexeclr   Ú
executabler   r
   r
   r
   r   Úrestart4   s   
r    c                   C   sr   t t d t dt dt dt dt d  t dt t dt d	t t dt d
t t dt d d S )Nan  
     __   __  _______  ___   ___      _______  ___   __    _  ______   _______  ______
    |  |_|  ||   _   ||   | |   |    |       ||   | |  |  | ||      | |       ||    _ |
    |       ||  |_|  ||   | |   |    |    ___||   | |   |_| ||  _    ||    ___||   | ||
    |       ||       ||   | |   |    |   |___ |   | |       || | |   ||   |___ |   |_||_
    |       ||       ||   | |   |___ |    ___||   | |  _    || |_|   ||    ___||    __  |
    | ||_|| ||   _   ||   | |       ||   |    |   | | | |   ||       ||   |___ |   |  | |
    |_|   |_||__| |__||___| |_______||___|    |___| |_|  |__||______| |_______||___|  |_|z                  z.:.:;..z MailFinder vz Developer: misha korzhik z..;:.:.Ú
z>> z5To find the mail you need, write your last name and 
z=first name in different ways. For example: vuiko, vuikoo, vu
z0It still takes a long time to find your e-mail.
)r   r   r   ÚyÚversionÚ	des_spacer
   r
   r
   r   Úbanner:   s   &>r%   c                  C   sÄ  t t t dt dt dt d	 t t t dt dt dt d	 t t t dt dt dt d	 t t d	t d
 t t t dt dt dt d	 t t t dt dt dt d	 t t t dt dt dt d	 ttt t dt dt dt dt d	 ¡ } | dks| dkrt  d S | dks¤| dkr©t  d S | dks±| dkr¶t	  d S | dks¾| dkrÃt
  d S | dksË| dkrÐt  d S | dksØ| dkrÝt  d S t  d S )Nr   r   r   z Search e-mail from databaser   z Add e-mail to databaser   z! Check username on emails domainsú ú|Ú4z% Search e-mail information, hunter.ioÚ5z Search e-mail via fullnameÚ6z Update MailFinder
ú?ú Select a number:Ú01Ú02Ú03Ú04Z05Z06)r   r   r   r   ÚstrÚinputÚlowerÚdatabaseÚaddtodatabaseÚ	validatorÚ	emailinfoÚ
mailfinderr   r    )Útyper
   r
   r   Ú
selecttypeF   s*   $$$$$$2






r:   c                   C   s   t  d¡ t  t  d S )Né   )r   r   r   r%   r
   r
   r
   r   Úauto^   s   

r<   c                  C   sp  t  t¡} t  ttt t dt dt dt dt d 	¡ }t  zzt
 d| d |  ¡ ¡ }|d }t|d	 }t|d
 }t|d }t|d }t|d }t|d }	t|d }
t|d }t|d }tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|	  tt t dt dt dt d	|
  tt t dt dt dt d	|  tt t dt dt dt d	|  W nb   t  tt t dt dt dt d	 tt t dt dt dt d	 ttt t dt dt dt d t d 	¡ } t
 d| d |  ¡ ¡ }|d }t|d	 }t|d
 }t|d }t|d }t|d }t|d }	t|d }
t|d }t|d }tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|  tt t dt dt dt d	|	  tt t dt dt dt d	|
  tt t dt dt dt d	|  tt t dt dt dt d	|  Y W t
 d| d |  ¡j}d S W t
 d| d |  ¡j}d S t
 d| d |  ¡j}w )!Nr   r+   r   z  Write an email for information:r&   z.https://api.hunter.io/v2/email-verifier?email=z	&api_key=ÚdataÚstatusÚresultZregexpZ	gibberishZ
disposableZ
mx_recordsZsmtp_serverZ
smtp_checkÚblockú+z Email       : z Status      : z Result      : z Regexp      : z gibberish   : z disposable  : z mx_records  : z smtp_server : z smtp_check  : z Block       : r   z4 Oh no, it looks like the free api keys have run outz- Create your api key on the hunter.io websitez Write you hunter.io api key:)ÚrandomÚchoiceÚh_apisr<   r1   r2   r   r   r   r3   ÚrequestsÚgetÚjsonr   Útext)Zh_apiÚemailrF   r=   ZoneZtwoZthreeZfourZfiveZsixZsevenZeightZniner
   r
   r   r7   c   sn   
2(((((((((.$$2(((((((((,ä6r7   c                  C   s`  t   ttt t dt dt dt dt d ¡ } t   ttt  g d¢}zr|D ]l}| d | }d}zEt	j
d	d
|idd| idd}| ¡ d }|dkrett t dt dt dt d| 
 ntt t dt dt dt d| 
 	 W q, ty   tt t dt dt dt d| 
 Y q,w W d S  ty¯   tdf tj ¡  Y d S w )Nr   r+   r   z# While user name to validate email:r&   )6ú	gmail.comú	yahoo.comúoutlook.comúhotmail.comúlive.comz
icloud.comz	email.comzaol.comzqq.comzcomcast.netz	proton.mezprotonmail.comz	inbox.comzfootball.uaúi.uaúemail.uaú3g.uaúmeta.uaúua.fmú
yandex.comú	yandex.ruúmail.ruúinbox.ruúlist.ruúmyrambler.ruú
rambler.ruúautorambler.ruúlenta.ruz
rambler.uaúro.ruz
onmail.comzmail.comz
europe.comzusa.comz	iname.comzwriteme.comzasia.comzengineer.comzpost.comzdr.comz
myself.comzcoolsite.netzconsultant.comzcheerful.comzaccountant.comz
cash4u.comzcyberservices.comz
worker.comzworkmail.comzeuropemail.comzgermanymail.comzmoscowmail.comzmexicomail.comzitalymail.comú@z$92658c91-ac9a-4fd5-aa4c-d614881c5989ú-https://isitarealemail.com/api/email/validaterI   ÚAuthorizationúBearer é   ©ÚparamsÚheadersÚtimeoutr>   Úvalidú DONE ú	 Status: Zvalidedú Email: z FAIL Zinvalidz EXIT rf   ú)r<   r1   r2   r   r   r   r3   r   ÚlinesrE   rF   rG   ÚBÚgÚRr   ÚYÚKeyboardInterruptr   ÚstdoutÚflush)Úuserr=   ÚdomainrI   ÚapiÚresponser>   r
   r
   r   r6      s:   28ý*(,ÿñþr6   c            
      C   sÊ  t  d¡ t  zdd l} W n	   t d¡ Y ddlm}m} t  t  t	t
t t dt dt dt dt d	}t	t
t t dt dt dt d
t d	}t	t
t t dt dt dt dt d	}t	t
t t dt dt dt dt d	}t	t
t t dt dt dt dt d	}d}|j|| d}	|	jd| d| d| d| d| 
dd t  t  tt t dt dt dt d	 tt t dt dt dt d	 d S )Nç      ø?r   z!python3 -m pip install discord.py)ÚWebhookÚRequestsWebhookAdapterr   r+   r   z While victim e-mail:r&   z While victim fullname:z While victim phone(without +):z While victim device:z While victim city:zxhttps://discord.com/api/webhooks/986356156513529927/6Q-vwIVODV4TAOcMXx-Jdv3zhOAETyUjhs3Dd459KGUyyCKdDUibtYYIDZCAHVvLtBSU)ZadapterzEmail: z
Phone: z
Fullname: z	
Device: z
City: Z
MailFinder)ZcontentZusernamerA   z3 All done! Succesfully sended data to mishakorzhik!z9 When the program update comes out then it will be added!)r   r   r   Údiscordr   r	   ry   rz   r%   r1   r2   r   r   r   Zfrom_urlÚsendr   )
r{   ry   rz   rI   ÚfullnameZphoneZdeviceZcityZwebhook_linkZwebhookr
   r
   r   r5   ï   s*   
.....,$(r5   c                  C   sÎ#  t  d¡ t  t  ttt t dt dt dt dt d} t  t  t  d¡ | dks5| d	krt	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d d S | dkrët	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d d S | dksô| dkrMt	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d d S | dksW| d kr°t	  t
t t dt d
t dt dt d! t
t t dt d
t dt dt d t
t t dt d
t dt dt d" t
t t dt d
t dt dt d# d S | d$ksº| d%krt	  t
t t dt d
t dt dt d& t
t t dt d
t dt dt d t
t t dt d
t dt dt d' t
t t dt d
t dt dt d( d S | d)ks| d*krvt	  t
t t dt d
t dt dt d+ t
t t dt d
t dt dt d t
t t dt d
t dt dt d, t
t t dt d
t dt dt d d S | d-ks| d.krÙt	  t
t t dt d
t dt dt d/ t
t t dt d
t dt dt d t
t t dt d
t dt dt d0 t
t t dt d
t dt dt d d S | d1kr7t	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt d2t d t
t t dt d
t dt dt d3 d S | d4krªt	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d5 t
t t dt d
t dt dt d6 t
t t dt d
t dt d7t d8 d S | d9krt	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d: t
t t dt d
t dt dt d; t
t t dt d
t dt d7t d< d S | d=krt	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d> t
t t dt d
t dt dt d? t
t t dt d
t dt d7t d8 d S | d@ks| dAkrt	  t
t t dt d
t dt dt dB t
t t dt d
t dt dt d t
t t dt d
t dt dt dC t
t t dt d
t dt dt dD t
t t dt d
t dt d7t d d S | dEks| dFkrt	  t
t t dt d
t dt dt dG t
t t dt d
t dt dt d t
t t dt d
t dt dt dH t
t t dt d
t dt dt dI t
t t dt d
t dt d7t d8 d S | dJks| dKkrøt	  t
t t dt d
t dt dt dL t
t t dt d
t dt dt d t
t t dt d
t dt dt dM t
t t dt d
t dt dt dN t
t t dt d
t dt d7t dO d S | dPks| dQkrpt	  t
t t dt d
t dt dt dR t
t t dt d
t dt dt d t
t t dt d
t dt dt dS t
t t dt d
t dt dt dT t
t t dt d
t dt d7t dO d S | dUksz| dVkrèt	  t
t t dt d
t dt dt dW t
t t dt d
t dt dt dX t
t t dt d
t dt dt dY t
t t dt d
t dt dt dZ t
t t dt d
t dt d7t d[ d S | d\ksò| d]kr`t	  t
t t dt d
t dt dt d^ t
t t dt d
t dt dt d t
t t dt d
t dt dt d_ t
t t dt d
t dt dt d` t
t t dt d
t dt d7t da d S | dbksj| dckrØt	  t
t t dt d
t dt dt dd t
t t dt d
t dt dt de t
t t dt d
t dt dt df t
t t dt d
t dt dt dg t
t t dt d
t dt d7t dh d S | dikrKt	  t
t t dt d
t dt dt d t
t t dt d
t dt dt dj t
t t dt d
t dt dt dk t
t t dt d
t dt dt dl t
t t dt d
t dt d7t dm d S | dnksU| dokrÃt	  t
t t dt d
t dt dt dp t
t t dt d
t dt dt dq t
t t dt d
t dt dt dr t
t t dt d
t dt dt ds t
t t dt d
t dt d7t dt d S | duksÍ| dvk	r;t	  t
t t dt d
t dt dt dw t
t t dt d
t dt dt dj t
t t dt d
t dt dt dx t
t t dt d
t dt dt dy t
t t dt d
t dt d7t dz d S | d{k	sJ| d|k	sJ| d}k	rÍt	  t
t t dt d
t dt d~t d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt d7t d d S | dk	sÜ| dk	sÜ| dk
r_t	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt d7t d d S | dk
si| dk
r×t	  t
t t dt d
t dt dt d t
t t dt d
t dt dt dj t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt d7t d d S | dk
sá| dkrOt	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt d7t d d S | dksY| dkrÇt	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d  t
t t dt d
t dt dt d t
t t dt d
t dt d7t d¡ d S | d¢kr:t	  t
t t dt d
t dt dt d£ t
t t dt d
t dt dt d¤ t
t t dt d
t dt dt d t
t t dt d
t dt dt d¥ t
t t dt d
t dt d7t d¦ d S | d§ksD| d¨kr²t	  t
t t dt d
t dt dt d© t
t t dt d
t dt dt dª t
t t dt d
t dt dt d« t
t t dt d
t dt dt d¬ t
t t dt d
t dt d7t d­ d S | d®ks¼| d¯kr*t	  t
t t dt d
t dt dt d° t
t t dt d
t dt dt d± t
t t dt d
t dt dt d² t
t t dt d
t dt dt d³ t
t t dt d
t dt d7t d´ d S | dµkrt	  t
t t dt d
t dt dt d¶ t
t t dt d
t dt dt d· t
t t dt d
t dt dt d t
t t dt d
t dt dt d¸ t
t t dt d
t dt d7t d¹ d S | dºks§| d»krt	  t
t t dt d
t dt dt d¼ t
t t dt d
t dt dt d½ t
t t dt d
t dt dt d¾ t
t t dt d
t dt dt d¿ t
t t dt d
t dt d7t dÀ d S | dÁks| dÂkrt	  t
t t dt d
t dt dt dÃ t
t t dt d
t dt dt dÄ t
t t dt d
t dt dt dÅ t
t t dt d
t dt dt dÆ t
t t dt d
t dt d7t dÇ d S | dÈks| dÉkrt	  t
t t dt d
t dt dt dÊ t
t t dt d
t dt dt d½ t
t t dt d
t dt dt dË t
t t dt d
t dt dt dÌ t
t t dt d
t dt d7t dÀ d S | dÍks| dÎkr}t	  t
t t dt d
t dt dt dÏ t
t t dt d
t dt dt dÐ t
t t dt d
t dt dt dÑ t
t t dt d
t dt dt dÒ t
t t dt d
t dt d7t dÓ d S | dÔks| dÕkrõt	  t
t t dt d
t dt dt dÖ t
t t dt d
t dt dt d× t
t t dt d
t dt dt dØ t
t t dt d
t dt dt dÙ t
t t dt d
t dt d7t dÚ d S | dÛkrht	  t
t t dt d
t dt dt dÜ t
t t dt d
t dt dt dÝ t
t t dt d
t dt dt d t
t t dt d
t dt dt dÞ t
t t dt d
t dt d7t dß d S | dàksr| dákràt	  t
t t dt d
t dt dt dâ t
t t dt d
t dt dt d¤ t
t t dt d
t dt dt dã t
t t dt d
t dt dt dä t
t t dt d
t dt d7t då d S | dæksê| dçkrXt	  t
t t dt d
t dt dt dè t
t t dt d
t dt dt dé t
t t dt d
t dt dt dê t
t t dt d
t dt dt dë t
t t dt d
t dt d7t dì d S | díksb| díkrÐt	  t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt dt d t
t t dt d
t dt d7t d d S t
t t dt dît dt dït dð d S )ñNrx   r   r+   r   z1 While victim e-mail or phone number (without +):r&   g      à?zbabenkosergij323@gmail.comZ380683753584rA   z Email:z babenkosergij323@gmail.comz Device:z	 Redmi 6Az Phone:z +380683753584z
 Fullname:u    Ð¡ÐµÑÐ³ÑÐ¹ ÐÐ°Ð±ÐµÐ½ÐºÐ¾zromanyshyn150611@gmail.comz New Email:z urakrasava2@gmail.comz Redmi 9z
 Not Foundu    Ð®ÑÐ° Ð Ð¾Ð¼Ð°Ð½Ð¸ÑÐ¸Ð½zegormustovic1@gmail.comz+380663560561z egormustovic707@gmail.comz Iphone SE 5z +380663560561u    ÐÐ³Ð¾Ñ ÐÑÑÑÐ¾Ð²ÑÑzbulygin0909@gmail.comZ79283995209z bulygin0909@gmail.comz +79283995209u     ÐÐ¸Ð¼Ð° ÐÐ¸ÑÐ¾Ð²Ð¾Ð»ÐµÐ½ÐºÐ¾zyaroslavsn2011@gmail.comZ79199710974z yaroslavsn2011@gmail.comz +79199710974u    Ð¯ÑÐ¾ÑÐ»Ð°Ð²zsteptsnick@yandex.comZ79651844696z steptsnick@yandex.comz +79651844696zbroc2895@gmail.comZ79372991242z broc2895@gmail.comz +79372991242Z79884421066z Phone: +79884421066u    Ð¡ÑÐ»ÑÐ°Ð½ ÐÐ²Ð°Ð½Ð¾Ð²Z79884434347z +79884434347u    Ð Ð¾Ð¼Ð°Ð·Ð°Ð½ ÐÐ°ÑÐ°Ð½Ð¾Ð²z City:z MoscowZ79884437549z +79884437549u    Ð¥Ð°Ð±Ð¸Ð± ÐÑÐ¸ÑÐ¾Ð²z	 DagestanZ79884437878z +79884437878u&    ÐÐ¶Ð°Ð¼Ð¸Ð»Ñ ÐÐ°ÑÑÑÐ´Ð¸Ð½Ð¾Ð²Ð°Z79884444587zvagif-sultanov@mail.ruz vagif-sultanov@mail.ruz +79884444587u    ÐÐ°Ð³Ð¸Ñ Ð¡ÑÐ»ÑÐ°Ð½Z79884490169zwww.scorpione@mail.ruz www.scorpione@mail.ruz +79884490169z Abdurahman GadzhievZ79884503424ztsahaeva1973@gmail.comz tsahaeva1973@gmail.comz +79884503424z Zulfiya Tsahaevaz MakhachkalaZ79884553338zzaur-amiraliev@mail.ruz zaur-amiraliev@mail.ruz +79884553338u    ÐÐ°ÑÑÐ¾Ð²ÑÐµ ÐÐ¾ÑÐºÐ¸Z
7993530634zyadawallivijay9@gmail.comz yadawallivijay9@gmail.comz Poco M2z +7993530634z yadawalli vijayz NarsapuramZ905524509973zkubraozturk1907@hotmail.comz kubraozturk1907@hotmail.comz +905524509973z kubraozturkz 34Z
8141191339zrutvikm205@gmail.comz rutvikm205@gmail.comz	 oppoA11Kz +8141191339z Rutvik Movaliyaz SurayZ
9034675423z Androidz +9034675423z Pratik Jaiswalz chikhliZ79024333324zkiraillll@mail.comz kiraillll@mail.comz	 HONOR 9Xz +79024333324u5    Ð¤ÐµÐ´Ð¾ÑÐ¾Ð² ÐÐ¸ÑÐ¸Ð»Ð» ÐÐ»Ð°Ð´Ð¸Ð¼Ð¸ÑÐ¾Ð²Ð¸Ñz Yoshkar-OlaZ28773108zthimsenchristian@gmail.comz thimsenchristian@gmail.comz	 28773108z thimsen , christianu    tÃ¸nderZ
6239466267zgod999yt@gmail.comzraviranjan2007@gmail.comz One Email:z god999yt@gmail.comz Two Email:z raviranjan2007@gmail.comz oppoc15z +6239466267z raviranjanz	 ludhianaZ
2813841551Z
2813609009zwhittingtonann@gmail.comz whittingtonann@gmail.comz One Phone:z +2813609009z Two Phone:z +2813841551z frederic henry whittingtonz huffman texasZ07725709622zabedas221223@gmail.comz abedas221223@gmail.comz +07725709622z abedz Iraqzshajahan425386@gmail.comZ9660572043070z shajahan425386@gmail.comz oppof11z +9660572043070z Not Found!z sudi arbiyizshylegay@gmail.comZ33766033168z shylegay@gmail.comz +33766033168z Francezalexgarcia00123.ag@gmail.comz alexgarcia00123.ag@gmail.comz androidz alex garciaz spainzmohammeddanish65@gmail.comZ
8153643824z mohammeddanish65@gmail.comz Samsungz +8153643824z Mohammed Danishz
 Bangalorezaanshupriya35@gmail.comZ
9142158515z aanshupriya35@gmail.comz vivoz +9142158515z aanshupriyaz dehliZ09757974586z +09757974586z	 computerz soesoez yangonzmichellegonzalez2020@gmail.comZ
4632538260z michellegonzalez2020@gmail.comz B140DLz +4632538260z michelle gonzalezz indianapoliszreginalofficial@gmail.comZ16782490086z reginalofficial@gmail.comz Iphonez +16782490086z reginal White z Chicagozmichelkegonzalez2020@gmail.comZ14632538260z michelkegonzalez2020@gmail.comz +14632538260z michelle lee gonzalezziftakherlabib017@gmail.comZ8801916461328z iftakherlabib017@gmail.comz
 narzo 30az +8801916461328z Iftakher Labibz mymenshingzcristianavellaned1@gmail.comZ51901540843z cristianavellaned1@gmail.comz redmi note 8 proz +51901540843z$ cristian miguel avellaneda saldivarz	 chiclayozsimactipik@gmail.comz simactipik@gmail.comz xiaomiz Simac Tipikz Rijekazedoformica@gmail.comZ
3515909000z edoformica@gmail.comz +3515909000z edoardoz romezdaritra66@email.comZ
9339181011z daritra66@email.comz	 Oppo a53z +9339181011z aritraz	 agarparaÚ ú-z Error! Not found, use zsearch email via fullname)r   r   r   r%   r1   r2   r   r   r   r<   r   )rI   r
   r
   r   r4     s&  
.
***.***.***.***.***.***.***.
***.
****.
****.
****.****.****.****.****.****.****.****.
****.****.****.*****.*****.****.****.****.
****.****.****.
****.****.****.****.****.****.
****.****.****.****..r4   c                  C   s)  t  d¡ t  t  ttt t dt dt dt dt d 	¡ } ttt t dt dt dt dt d 	¡ }t  d¡ t  t  t
t t dt dt dt d		 t
t t dt d
t dt d	 t
t t dt dt dt d	 t
t t dt dt dt d	 t
d ttt t dt dt dt dt d 	¡ }|dksµ|dkrºg d¢}n&|d
ksÂ|dkrÇg d¢}n|dksÏ|dkrÔg d¢}n|dksÜ|dkràg d¢}t
d |sét  | sît  |sót  | | }d}d}t  d¡ t  t  d| v r|  dd¡}n#d| v r|  dd¡}nd| v r*|  dd ¡}nd!| v r5|  d!d"¡}d|v rA| dd¡}nGd#|v rM| d#d$¡}n;d%|v rY| d%d&¡}n/d'|v re| d'd(¡}n#d)|v rq| d)d*¡}nd+|v r}| d+d,¡}nd-|v r| d-d.¡}| d/ }| d0 }d1| d2 }	t
tt  g |	 dd¡| d3 |	 dd¡| d4 |	 dd¡| d5 |	 dd¡| d6 |	 dd¡| d7 |	 dd¡| d8 |	 dd¡| d9 |	 dd¡| | dd¡| d: | dd¡| d; | dd¡| d< | dd¡| d= | dd¡| d> | dd¡| d? | dd¡| d8 | dd¡| d@ | dd¡| d6 | dd¡| d7 | dd¡| dA | dd¡| dB | dd¡| dC | dd¡| dD | dd¡| dE | dd¡| dF | dd¡| dG | dd¡| dA | dd¡| dH | dd¡d2 |  | dd¡d2 | | dd¡|  | dd¡| | dd¡d2 |  | dd¡d2 | | dd¡d2 |  |  dd¡| |  dd¡d2 | | dd¡d2 | | dd¡d2 | | dd¡d2 | | dd¡d2 | dB | dd¡d2 | d3 | dd¡d2 | dI | dd¡d2 | dJ | dd¡d2 | dK | dd¡d2 | dL | dd¡d2 | d@ | dd¡d2 | dM | dd¡d2 | dN | dd¡d2 | dF | dd¡d2 | dO | dd¡d2 | dP | dd¡d2 | dQ | dd¡d2 | d4 | dd¡d2 | dR | dd¡d2 | dS | dd¡d2 | dT | dd¡d2 | dU | dd¡d2 | dV | dd¡d2 | dW | dd¡d2 | dX | dd¡d2 | d | dd¡d2 | dY | dd¡d2 | dZ | dd¡d2 | d[ | dd¡d2 | d\ | dd¡d2 | d] | dd¡d2 | d | dd¡d2 | d
 | dd¡d2 | d^ | dd¡d2 | d_ | dd¡d2 | d` | dd¡d2 | da | dd¡d2 | db | dd¡d3 | dd¡d? | dd¡dc | dd¡dd | dd¡dB | dd¡de | dd¡d_ | dd¡dA | dd¡df | dd¡dg | dd¡dh | dd¡di | dd¡dj | dd¡dk | dd¡dl | dd¡dm | dd¡dn | dd¡do | dd¡dp | dd¡dq | dd¡dr | dd¡ds | dd¡dt | dd¡du | dd¡dv | dd¡dw | dd¡dx | dd¡dy | dd¡dz | dd¡d{ | dd¡d| | dd¡d} | dd¡d~ | dd¡d | dd¡d | dd¡d@ | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d` | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡d | dd¡dG | dd¡dB | dd¡d | dd¡d | dd¡d4 | dd¡dR | dd¡d | dd¡d  | dd¡d¡ | dd¡dO | dd¡dP | dd¡d¢ | dd¡d£ | dd¡dV | dd¡d¤ | dd¡d¥ | dd¡d[ | dd¡d\ | dd¡dY | dd¡dZ | dd¡d | dd¡d | dd¡d
 | dd¡d | dd¡d1 | dd¡| dd¡| d¦ | dd¡| d@ | dd¡| d6 | dd¡| d7 | dd¡| dA | dd¡| dB | dd¡| dC | dd¡| dD | dd¡| dE | dd¡| dF | dd¡| dG | dd¡| dA | dd¡| dH | dd¡| dh | dd¡| d | dd¡| d` | dd¡| d | dd¡| d | dd¡| dw | dd¡| dh | dd¡| d3 | dd¡| d_ | dd¡| d | dd¡| d§ | dd¡| d¨ | dd¡| d© | dd¡| dª | dd¡| d« | dd¡| d¬ | dd¡| d­ | dd¡| d® | dd¡| d4 | dd¡| dQ | dd¡| dS | dd¡| d¯ | dd¡| d° | dd¡| d± | dd¡| d² | dd¡| d³ | dd¡| dX | dd¡| d´ | dd¡| d¢ | dd¡| dµ | dd¡| d¥ | dd¡| d[ | dd¡| d¶ | dd¡| d· | dd¡| d¸ | dd¡| d¹ | dd¡| d\ | dd¡| d] | dd¡| dY | dd¡| dZ | dd¡| dº | dd¡| d | dd¡| d | dd¡| d
 | dd¡| d | dd¡| d1 |  dd¡| | dd¡| | dd¡| d: | dd¡| d; | dd¡| d< | dd¡| d= | dd¡| d> | dd¡| d? | dd¡| d8 | dd¡| d® | dd¡| d» | dd¡| d¼ | dd¡| d? | dd¡| d½ | dd¡| d¾ | dd¡| d¦ | dd¡| d¿ | dd¡| d@ | dd¡| d6 | dd¡| d7 | dd¡| dA | dd¡| dB | dd¡| dC | dd¡| dD | dd¡| dE | dd¡| dF | dd¡| dG | dd¡| dA | dd¡| dH | dd¡| dh | dd¡| d | dd¡| d` | dd¡| d | dd¡| d | dd¡| dw | dd¡| dh | dd¡| d3 | dd¡| d_ | dd¡| d | dd¡| d§ | dd¡| d¨ | dd¡| d© | dd¡| dª | dd¡| d« | dd¡| d¬ | dd¡| d­ | dd¡| d® | dd¡| d4 | dd¡| dQ | dd¡| dS | dd¡| d¯ | dd¡| d° | dd¡| d± | dd¡| d² | dd¡| d³ | dd¡| dX | dd¡| d´ | dd¡| d¢ | dd¡| dµ | dd¡| d¥ | dd¡| d[ | dd¡| d¶ | dd¡| d· | dd¡| d¸ | dd¡| d¹ | dd¡| d\ | dd¡| d] | dd¡| dY | dd¡| dZ | dd¡| dº | dd¡| d | dd¡| d | dd¡| d
 | dd¡| d | dd¡| d1 | dd¡| | dd¡| dÀ | dd¡| d? | dd¡| d¿ | dd¡| dÁ | dd¡| dÂ | dd¡| d: | dd¡| d; | dd¡| d< | dd¡| d= | dd¡| d> | dd¡| d? | dd¡| d8 | dd¡| d¦ | dd¡| d@ | dd¡| d6 | dd¡| d7 | dd¡| dA | dd¡| dB | dd¡| dC | dd¡| dD | dd¡| dE | dd¡| dF | dd¡| dG | dd¡| dA | dd¡| dH | dd¡| dh | dd¡| d | dd¡| d` | dd¡| d | dd¡| d | dd¡| dw | dd¡| dh | dd¡| d3 | dd¡| d_ | dd¡| d | dd¡| d§ | dd¡| d¨ | dd¡| d© | dd¡| dª | dd¡| d« | dd¡| d¬ | dd¡| d­ | dd¡| d® | dd¡| d4 | dd¡| dQ | dd¡| dS | dd¡| d¯ | dd¡| d° | dd¡| d± | dd¡| d² | dd¡| d³ | dd¡| dX | dd¡| d´ | dd¡| d¢ | dd¡| dµ | dd¡| d¥ | dd¡| d[ | dd¡| d¶ | dd¡| d· | dd¡| d¸ | dd¡| d¹ | dd¡| d\ | dd¡| d] | dd¡| dY | dd¡| dZ | dd¡| dº | dd¡| d | dd¡| d | dd¡| d
 | dd¡| d | dd¡| d1 |  dd¡| |  dd¡| d¦ |  dd¡| d@ |  dd¡| d6 |  dd¡| d7 |  dd¡| dA |  dd¡| dB |  dd¡| dC |  dd¡| dD |  dd¡| dE |  dd¡| dF |  dd¡| dG |  dd¡| dA |  dd¡| dH |  dd¡| dh |  dd¡| d |  dd¡| d` |  dd¡| d |  dd¡| d |  dd¡| dw |  dd¡| dh |  dd¡| d3 |  dd¡| d_ |  dd¡| d |  dd¡| d§ |  dd¡| d¨ |  dd¡| d© |  dd¡| dª |  dd¡| d« |  dd¡| d¬ |  dd¡| d­ |  dd¡| d® |  dd¡| d4 |  dd¡| dQ |  dd¡| dS |  dd¡| d¯ |  dd¡| d° |  dd¡| d± |  dd¡| d² |  dd¡| d³ |  dd¡| dX |  dd¡| d´ |  dd¡| d¢ |  dd¡| dµ |  dd¡| d¥ |  dd¡| d[ |  dd¡| d¶ |  dd¡| d· |  dd¡| d¸ |  dd¡| d¹ |  dd¡| d\ |  dd¡| d] |  dd¡| dY |  dd¡| dZ |  dd¡| dº |  dd¡| d |  dd¡| d |  dd¡| d
 |  dd¡| d | dd¡| | dd¡| dº | dd¡| dZ | dd¡| dÃ | dd¡| d: | dd¡| d§ | dd¡| dÄ | dd¡| dÅ | dd¡| dÆ | dd¡| dÇ | dd¡| d¿ | dd¡| d¦ | dd¡| d4 | dd¡| dB | dd¡| dS | dd¡| d« | dd¡| d@ | dd¡| d? | dd¡| d§ | dd¡| d | dd¡| d
 | dd¡| d | dd¡| d | dd¡| dY | dd¡| d | dd¡| dX | dd¡| d6 | dd¡| d7 | dd¡| dS | dd¡| d£ | dd¡| d | dd¡| d² | dd¡| dÈ | dd¡| dÉ | dd¡| dÊ | dd¡| dË | dd¡| dÌ | dd¡| dÍ | dd¡| dÎ | dd¡| dÏ | dd¡| dÐ | dd¡| dÑ | dd¡| dÒ | dd¡| dÓ | dd¡| dÔ | dd¡| dÕ | dd¡| dÖ | dd¡| dP | dd¡| dQ | dd¡| d× | dd¡| dØ | dd¡| d | dd¡| dÙ }
tdÚdÛ}g }z\|
D ]W}|D ]Q}|d | }dÜ}g dÝ¢}t |¡}tjdÞdß|idàdá| idâdã}| ¡ dä }|dåkrI| |¡ | |dæ ¡ t
t t dçt dèt dåt dé| 
 qú	 qúqöW n tyc   t
dêf tj ¡  Y nw | ¡  t
tt  t
t t dët dtt| dìt dÚt 
 d S )íNrx   r   r+   r   z While victim first name:r&   z While victim last name:r   zC Services: gmail.com, yahoo.com, outlook.com, hotmail.com, live.comr   z< Services: yandex.com, yandex.ru, mail.ru, inbox.ru, list.rur   zD Services: myrambler.ru, rambler.ru, lenta.ru, autorambler.ru, ro.rur(   z0 Services: i.ua, email.ua, 3g.ua, meta.ua, ua.fmr~   r,   r-   )rJ   rK   rL   rM   rN   r.   )rT   rU   rV   rW   rX   r/   )rY   rZ   r\   r[   r]   r0   )rO   rP   rQ   rR   rS   r^   ZiyZijZchÚcZshaZsaZviyÚviÚshÚzZtvieZtviyZushunZyshynZkovZkivZzhiZziZsahlZsakhlZikZmarmeladÚ0Ú.Z777Z62Z122Z528Z538Z122000Z160511Z0000Z00000Z0001Z00001Z100000Z150611Z323Z666Z707Z701Z344Z811Z400Z100Z945Z906Z969Z700Z600Z313Ú500Z99Z89Z61Z71Z81Z95Z85Z60Z50Z55Ú7r*   Z10Ú9Ú8Z881Z999Z222Z393Z383Ze80Z717Z760Z809Z807Z888Z848Z844Z909Z900Ú950Z955Z960Z970Z670Z610Z606Z650Z681Z662Z555Z505Z550Z525Z537Z531Z411Z477Z444Z499Z333Z321Z388Z370Z300Z299Z288Z270Z277Z266Z240Z244Z255Z232Z211Z200Z199Z189Z188Z166Z165Z169Z196Z150Z142Z133Z120Z111Z000Z00Z54Z23Z22Z69Z96Z59Z11Z380Z001Z002Z003Z877Z312Z841Z808Z607Z79Z41Z42Z44Z56Z57Z12Z32Z36Z76Z40r)   Z1010Z1111Z263Z1000Z706Z989Z708Z3331Z3021ÚtopZminiZkikZhehZ43Z2000Z2001Z2002Z2003Z2004Z2005Z2006Z2007Z2008Z2009Z72Z82Z98Z97Z53Z52Z198z
result.txtr   z	1 000 000)2z$18b15db3-4c02-473e-bb2d-39805a993abfz$83218c83-69c0-4238-ba69-2c18699998f4z$2501fcca-29e5-4fff-b48e-7cf70d6ead1ez$18476942-d0db-4a3e-9574-639c6f48f851z$014888c0-095a-4a7e-8367-6e12c857ffa0z$cddbbcdd-0fd1-46e6-9cb8-476f8fc1e07bz$47c2769a-6dd2-4bc0-ac81-7b8c191238a9z$c9170bef-30a2-4d76-bf1d-e16532446893z$9c6405cd-7213-4d31-a7fd-b6218c97d4f7z$93302033-0fc2-45d1-9be3-aad7aa2e9fe6z$560b7d47-91bf-4362-b548-85d23f831322z$1512da7c-95b7-4ce6-9b56-70db932964ccz$1110e3b2-00d8-4633-8813-48b837971e13z$dce9497b-ecfd-4ecc-b159-ed3cf5519ab6z$c9d6bbea-6b41-4bcb-b1a6-421b95d40c92z$935cef62-fcd3-4958-a6bd-e44e76b6610ez$f3e53f50-16a5-4b6c-8a86-33e57263ac7fz$49da25eb-cafb-4dbd-9a4d-f837d89aa6b7z$78fa66d9-3aeb-4775-8742-1a197bbfe4d1z$b91d73e7-b039-43ab-b8f7-fb763b12f341z$15816a58-c827-41de-9faa-13fd9a677724z$c58b57b4-5aa7-420d-ac46-f063af1488f7z$4a1cba4c-c6fc-4d7e-b514-c76da9178f59z$14cea250-83fe-48ba-b2ad-8e57cb23a80ez$7b94ca89-2659-450b-b830-6423e64dd7f8z$68e4af7d-b1d5-474f-a8dd-0a69b78114b9z$93f1baa4-8ea2-4b4b-905d-56e0286ede67z$be1a5f7e-06d0-49ee-95db-de8d59b25186z$150de096-a9a0-450c-a20d-4a212d74f696z$07452089-66bc-4e70-ab80-90f83c6f300fú$fb36f45a-5627-499f-a399-9de47fbee171r   z$b35ca57f-cfa9-4e49-80a3-90cddd04d71dz$9d767511-ad68-49ff-b252-bf42a671c2e8z$960c5ccf-18b3-4417-bca0-6ace2f042fcfz$5aa9818d-44c9-46ed-b749-76f3a654e52ez$8048a6dd-7bde-4e9b-bac0-cd6f1ba39ef8z$064e2356-9189-41bd-bb1c-239c714e08dcz$95c8e2e0-9085-4048-8092-4392e4209bb1z$98893b7f-b76f-484e-8f54-8b0c26bd7c6ez$f4037fd5-637b-4a55-bbea-6ade15517c04z$de131a1e-64b1-4ff3-b560-5a9a783a8136z$87c0d451-89e7-4056-8a84-862c09ad4456z$f6ece0f0-2151-4282-bd13-5e7070991491z$6fc96263-8b04-4208-a9df-8b25912b4c42z$dd43ac2d-e93a-466b-ab82-a1e71c922e02z$3ffe1c4e-287e-4440-9df9-5d36d78a8dcez$879127a3-fe82-44a1-bc48-486293d49186z$9e8e5203-07a4-42cd-bf4d-310b10f70976z$54ef3d7a-d15a-4dec-a724-976083d0744er_   rI   r`   ra   rb   rc   r>   rg   r!   rh   ri   rj   rk   ú>z retrieved as: )r   r   r   r%   r1   r2   r   r   r   r3   r   r    Úreplacerl   ÚopenrB   rC   rE   rF   rG   ÚappendÚwriterm   rn   rq   r   rr   rs   ÚcloseÚlenr"   )ÚnameZfamiliar9   r=   r}   Zna1Zfa1Zik_nZmar_nZok0ZlistuserÚfÚokrt   ru   rI   Zapi_numZapisrv   rw   r>   r
   r
   r   r8     sè  
22
$$$$2






ÿþýüûúùø	÷
öõôóòñðïîíìëêéèçæåäãâá à!ß"Þ#Ý$Ü%Û&Ú'Ù(Ø)×*Ö+Õ,Ô-Ó.Ò/Ñ0Ð1Ï2Î3Í4Ì5Ë6Ê7É8È9Ç:Æ;Å<Ä=Ã>Â?Á@ÀA¿B¾C½D¼E»FºG¹H¸I·J¶KµL´M³N²O±P°Q¯R®S­T¬U«VªW©X¨Y§Z¦[¥\¤]£^¢_¡` abcdefghijklmnopqrstuvwxyz{|}~  ÿ  þ  ý  ü  û  ú  ù  ø 	 ÷ 
 ö  õ  ô  ó  ò  ñ  ð  ï  î  í  ì  ë  ê  é  è  ç  æ  å  ä  ã  â  á   à ! ß " Þ # Ý $ Ü 
% Û & Ú ' Ù ( Ø ) × * Ö + Õ , Ô - Ó . Ò / Ñ 0 Ð 1 Ï 2 Î 3 Í 4 Ì 5 Ë 6 Ê 7 É 8 È 9 Ç : Æ ; Å < Ä = Ã > Â ? Á @ À A ¿ B ¾ C ½ D ¼ E » F º G ¹ H ¸ I · J ¶ K µ L ´ M ³ N ² O ± P ° Q ¯ R ® S ­ T ¬ U « V ª W © X ¨ Y § Z ¦ [ ¥ \ ¤ ] £ ^ ¢ _ ¡ `   a  b  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z  {  |  }  ~       ÿ    þ    ý    ü    û    ú    ù    ø  	  ÷  
  ö    õ    ô    ó    ò    ñ    ð    ï    î    í    ì    ë    ê    é    è    ç    æ    å    ä    ã    â    á     à  !  ß  "  Þ  #  Ý  $  Ü  %  Û  &  Ú  '  Ù  (  Ø  )  ×  *  Ö  +  Õ  ,  Ô  -  Ó  .  Ò  0  Ð  1  Ï  2  Î  3  Í  4  Ì  5  Ë  6  Ê  7  É  8  È  9  Ç  :  Æ  ;  Å  <  Ä  =  Ã  >  Â  ?  Á  @  À  A  ¿  B  ¾  C  ½  D  ¼  E  »  F  º  G  ¹  H  ¸  I  ·  J  ¶  K  µ  L  ´  M  ³  N  ²  O  ±  P  °  Q  ¯  R  ®  S  ­  T  ¬  U  «  V  ª  W  ©  X  ¨  Y  §  Z  ¦  [  ¥  \  ¤  ]  £  ^  ¢  _  ¡  `     a    b    c    d    e    f    g    h    i    j    k    l    m    n    o    p    q    r    s    t    u    v    x    y    z    {    |    }    ~            ÿ      þ      ý      ü      û      ú      ù      ø   	   ÷   
   ö      õ      ô      ó      ò      ñ      ð      ï      î      í      ì      ë      ê      é      è      ç      æ      å      ä      ã      â      á       à   !   ß   "   Þ   #   Ý   $   Ü   %   Û   &   Ú   '   Ù   (   Ø   )   ×   *   Ö   +   Õ   ,   Ô   -   Ó   .   Ò   /   Ñ   0   Ð   1   Ï   2   Î   3   Í   4   Ì   5   Ë   6   Ê   7   É   8   È   9   Ç   :   Æ   ;   Å   <   Ä   =   Ã   >   Â   ?   Á   @   À   A   ¿   B   ¾   C   ½   D   ¼   E   »   F   º   G   ¹   H   ¸   I   ·   J   ¶   K   µ   L   ´   M   ³   N   ²   O   ±   P   °   Q   ¯   R   ®   S   ­   T   ¬   U   «   V   ª   W   ©   X   ¨   Y   §   Z   ¦   [   ¥   \   ¤   ]   £   ^   ¢   _   ¡   `       a      b      c      d      e      f      g      h      
j
ý

,ðÿþ4r8   )&r   Úrer   r   rG   rE   rB   Zrequests.exceptionsr   Úrrn   r"   r   ÚpÚdr   ÚWro   ÚGrp   rm   rD   r#   r   r$   rl   re   r   r   r    r%   r:   r<   r7   r6   r5   r4   r8   r
   r
   r
   r   Ú<module>   sP   8 




8T      R
