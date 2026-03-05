from django.shortcuts import render
from django.http import HttpResponse

def bmw_view(req):
    if req.method =="GET":
        return HttpResponse( """
    <h1>BMW X3</h1>
    <img src="https://www.bmwusa.com/content/dam/bmwusa/X3/2025/BMW-X3-Exterior-Front-3-4.jpg" alt="" width="300">                      
    <p>1)В 2025 году BMW X3 стал бестселлером бренда в США, обогнав даже более дорогой X5 всего на 300 штук (76 546 против 76 246).</p>
    <p>2)Версия X3 M50 — абсолютный лидер продаж среди всех моделей BMW M в 2025 году, обогнав даже чистокровные M3 и M2.</p>
    <p>3)Новый X3 (поколение 2025+) считается одним из самых технологичных кроссоверов в классе благодаря огромному изогнутому дисплею и продвинутым системам помощи водителю.</p>
    """)

def ferrari_view(req):
    if req.method =="GET":
        return HttpResponse( """
    <h1>Ferrari 296</h1>
    <img src="https://www.ferrari.com/sites/default/files/styles/model_gallery_slide_1920x1080/public/2024-03/296gtb_slide_01.jpg" alt="" width="300">
    <p>1)Ferrari 296 GTB / GTS — это самая массовая и востребованная модель Ferrari в 2024–2026 годах среди новых машин (часто входит в топ по продажам и перепродажам).</p>
    <p>2)Это первый Ferrari с V6 двигателем в среднем расположении за много лет, но с гибридной системой он выдаёт почти 830 л.с. и разгоняется до 100 км/ч за ~2,9 секунды.</p>
    <p>3)296 часто называют "идеальным ежедневным суперкаром" — он сочетает трековый характер с комфортом, что делает его хитом среди коллекционеров и энтузиастов.</p>
    """)

def honda_view(req):
    if req.method =="GET":
        return HttpResponse( """
    <h1>Honda CR-V</h1>
    <img src="https://automobiles.honda.com/-/media/Honda-Automobiles/Categories/Vehicles/CR-V/2025/Overview/2025-cr-v-hybrid-overview-hero-desktop.jpg" alt="" width="300">
    <p>1)В 2025 году Honda CR-V снова стала самой продаваемой моделью бренда в США — более 400 000 штук, и гибридные версии составляют больше половины продаж.</p>
    <p>2)CR-V — один из самых надёжных кроссоверов в мире по рейтингам Consumer Reports и J.D. Power, часто занимает 1-е место в классе компактных SUV.</p>
    <p>3)Глобально продано уже свыше 15 миллионов CR-V с 1995 года — это делает её одной из самых успешных моделей Honda всех времён.</p>
    """)