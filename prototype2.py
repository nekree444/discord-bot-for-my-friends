from discord.ext.commands import Bot
from discord.ext import commands
from discord import Intents
import requests
from bs4 import BeautifulSoup
import datetime
##import schedule
import time
import random
from discord.ext import tasks
import asyncio
import calendar
from dotenv import load_dotenv
import os

load_dotenv('./.env')
load_dotenv('./users.env')

intents = Intents.default()
intents.message_content = True
intents.members = True

monday = ['https://media.tenor.com/fL-e2WrYVJ4AAAAM/happy-new-week.gif', 'https://media.tenor.com/El_J1rdpT6wAAAAM/snoopy.gif', 'https://media.tenor.com/soJcUjM0jE8AAAAM/good-monday-morning.gif', 'https://media.tenor.com/CC31qIerj64AAAAM/happy-monday-good-monday-morning.gif', 'https://media.tenor.com/5jTsk-wlE2AAAAAM/monday-morning.gif', 'https://media.tenor.com/s91LR9-1QDYAAAAM/grumpy-its-monday.gif', 'https://media.tenor.com/eBouiobxhjMAAAAM/good-morning-monday-happy-monday.gif', 'https://media.tenor.com/dQYC2s6tqkYAAAAM/happy-monday-good-morning-monday.gif', '/assets/img/gif-maker-entrypoints/search-entrypoint-optimized.gif', 'https://media.tenor.com/bC5yG0SaclcAAAAM/good-morning.gif', 'https://media.tenor.com/Xz8jC-tncUEAAAAM/hello-monday.gif', 'https://media.tenor.com/v12n8HNWt8sAAAAM/monday-morning.gif', 'https://media.tenor.com/V4DQFQqFIOAAAAAM/good-monday-morning.gif', 'https://media.tenor.com/JnIxAxkFFDwAAAAM/good-morning.gif', 'https://media.tenor.com/yRf55kQ8aPMAAAAM/happy-monday.gif', 'https://media.tenor.com/u3-J8iH9gE0AAAAM/coffee-good-morning.gif', 'https://media.tenor.com/krabFGKTaNAAAAAM/good-morning.gif', 'https://media.tenor.com/-K6ua4BaLaQAAAAM/happy-monday-monday-motivation.gif', 'https://media.tenor.com/pC-2ZrotVMUAAAAM/morning-monday.gif', 'https://media.tenor.com/VNIdKIKd3TcAAAAM/howdy.gif', 'https://media.tenor.com/WpHBaUm7xAEAAAAM/monday-morning-good-morning-happy-monday.gif', 'https://media.tenor.com/fWCYDcXAykcAAAAM/garfield-hello.gif', 'https://media.tenor.com/cgFuUvAwrjQAAAAM/good-morning-morning.gif', 'https://media.tenor.com/GZPlBvDUSCwAAAAM/hello-monday.gif', 'https://media.tenor.com/fnZr9letHdkAAAAM/happy-monday.gif', 'https://media.tenor.com/dAQsOS6jj9YAAAAM/good-morning-monday.gif', 'https://media.tenor.com/bGbGB11iEzsAAAAM/monday.gif', 'https://media.tenor.com/CbzfQrVSfyoAAAAM/good-morning-coffee.gif', 'https://media.tenor.com/WARqEw_ceiUAAAAM/it%27s-monday.gif', 'https://media.tenor.com/YEQ-wsH37j8AAAAM/vec50maandag-vec50monday.gif', 'https://media.tenor.com/FzGgaeNaJosAAAAM/monday-happy.gif', 'https://media.tenor.com/0a3JbzxwFCcAAAAM/hello-monday.gif', 'https://media.tenor.com/tR38nf4skeUAAAAM/good-morning-images-new-2023-good-morning.gif', 'https://media.tenor.com/cPYRbUhFWbIAAAAM/it%27s-monday.gif', 'https://media.tenor.com/D2rvxIY0ZIsAAAAM/monday-blessings.gif', 'https://media.tenor.com/T6jpPzPkdt0AAAAM/good-monday-morning.gif', 'https://media.tenor.com/Tav3TZOlIpUAAAAM/happy-monday.gif', 'https://media.tenor.com/0jPDuK9w4kcAAAAM/monday-vec50.gif', 'https://media.tenor.com/hBjdmlWTmVYAAAAM/new-day-monday.gif', 'https://media.tenor.com/NIBWzZHAwBoAAAAM/blessings-god.gif', 'https://media.tenor.com/KyGBna_tHvIAAAAM/monday-motivation.gif', 'https://media.tenor.com/IqnCSteKiREAAAAM/goodmorning-snow.gif', 'https://media.tenor.com/LttLttjMJYkAAAAM/good-morning-good-morning-wishes.gif', 'https://media.tenor.com/DDOjuBDeOzUAAAAM/monday-morning.gif', 'https://media.tenor.com/NDZ0JO_WwrgAAAAM/love-son.gif', 'https://media.tenor.com/5iWQpHDf8bsAAAAM/monday-good-morning.gif', 'https://media.tenor.com/yklKCkLwxA8AAAAM/monday-morning-good-morning-images-new-2023.gif', 'https://media.tenor.com/q3HhV4EWVkYAAAAM/good-morning.gif', 'https://media.tenor.com/foluH3vCHU0AAAAM/good-monday-morning.gif', 'https://media.tenor.com/ZBTi7SlPARMAAAAM/good-morning.gif']
tuesday = ['https://media.tenor.com/vzA2MuCKPswAAAAM/good-tuesday-morning.gif', 'https://media.tenor.com/Hta9sTdVKScAAAAM/taco-tuesday-happy-tuesday.gif', 'https://media.tenor.com/RE_ULVc2KBkAAAAM/happy-tuesday.gif', 'https://media.tenor.com/TWALwBSbro0AAAAM/terrific-tuesday.gif', 'https://media.tenor.com/6HUXZnsd9A8AAAAM/good-tuesday-morning.gif', 'https://media.tenor.com/4vaIoJQAb7IAAAAM/good-morning-tuesday.gif', 'https://media.tenor.com/6IM1DTxib_AAAAAM/good-morning.gif', 'https://media.tenor.com/VmOWkhnJtAkAAAAM/tuesday-blessings.gif', 'https://media.tenor.com/tadpm6ZOh58AAAAM/morning-happy-tuesday.gif', 'https://media.tenor.com/XDFqvbmXZI4AAAAM/tuesday-blessings.gif', 'https://media.tenor.com/JGrg9n0FZAEAAAAM/tuesday.gif', 'https://media.tenor.com/AoOUAzt42UQAAAAM/good-morning-drink.gif', 'https://media.tenor.com/goX0KPt_sZsAAAAM/tuesday-blessings.gif', 'https://media.tenor.com/iHAviTYpiC8AAAAM/good-morning.gif', 'https://media.tenor.com/Ssu5IBGY-LEAAAAM/goodmorning-happytuesday.gif', 'https://media.tenor.com/Mb-21s1WWlwAAAAM/good-tuesday-morning.gif', 'https://media.tenor.com/MeOy2SbW8iQAAAAM/good-morning-rose.gif', 'https://media.tenor.com/ev6Eltc7X04AAAAM/good-morning.gif', 'https://media.tenor.com/bcFesdt7ntwAAAAM/it%27s-tuesday.gif', 'https://media.tenor.com/_7d6ab3D8-4AAAAM/have-a-nice-day.gif', 'https://media.tenor.com/I03r_XevDbcAAAAM/tuesday-teddy-bear.gif', 'https://media.tenor.com/3j0PbNAcy_YAAAAM/tuesday-blessings-happy-tuesday.gif', 'https://media.tenor.com/no1Pm5sH6-UAAAAM/a-goofy-movie-goofy.gif', 'https://media.tenor.com/UHtO9_AenwQAAAAM/happy-tuesday.gif', 'https://media.tenor.com/ggDY2KGP2wgAAAAM/tuesday-love.gif', 'https://media.tenor.com/kW98i_dU7pwAAAAM/happy-tuesday.gif', 'https://media.tenor.com/ydfDkvZH2HkAAAAM/good-mor.gif', 'https://media.tenor.com/5r5k5mFKYOoAAAAM/mao-cat.gif', 'https://media.tenor.com/JaLgOIE0zPIAAAAM/mickey-mouse.gif', 'https://media.tenor.com/BReVEcNQV9kAAAAM/happy-tuesday.gif', 'https://media.tenor.com/-5VQBjBO7x0AAAAM/happy-tuesday.gif', 'https://media.tenor.com/atE75aL9NKcAAAAM/bishop-chilling.gif', 'https://media.tenor.com/dxT6v11b-s0AAAAM/purrlene-the-cat-good-morning-cat.gif', 'https://media.tenor.com/8EHwUpfsEIUAAAAM/good-morning-good-morning-flowers.gif', '/assets/img/gif-maker-entrypoints/search-entrypoint-optimized.gif', 'https://media.tenor.com/gslQgr-tj3wAAAAM/tuesday-terrific-tuesday-tiger.gif', 'https://media.tenor.com/1VTv_CeQUyEAAAAM/good-tuesday-morning.gif', 'https://media.tenor.com/bjV9TdFxP3YAAAAM/tuesday-morning.gif', 'https://media.tenor.com/SyrAlSJ7JsgAAAAM/goodmorning-happytuesday.gif', 'https://media.tenor.com/G6PhAwxP6OEAAAAM/good-morning-happy-tuesday.gif', 'https://media.tenor.com/vrGATCrODpsAAAAM/good-morning.gif', 'https://media.tenor.com/NDl7r7x0Z9wAAAAM/vec50dinsdag-dinsdag.gif', 'https://media.tenor.com/h-5vjhbRtIMAAAAM/tuesday-vec50.gif', 'https://media.tenor.com/xdSgyfr4gqwAAAAM/it%27s-tuesday-good-tuesday-morning.gif', 'https://media.tenor.com/6HoWfjknFccAAAAM/morning-happy-tuesday.gif', 'https://media.tenor.com/jJY-JgXjLuEAAAAM/happy-tuesday-happy-tuesday-morning.gif', 'https://media.tenor.com/Tf0cV_VgH5IAAAAM/terrific-tuesday.gif', 'https://media.tenor.com/opz5Sc7KZLgAAAAM/tuesday-blessings.gif', 'https://media.tenor.com/bCdyEEFhvGAAAAAM/goodmorning-happytuesday.gif', 'https://media.tenor.com/7vd0SoogBvsAAAAM/good-tuesday-morning.gif']
wednesday = ['https://media.tenor.com/jfOm12ZopnEAAAAM/have-a-beautiful-day-wednesday-morning.gif', 'https://media.tenor.com/u6Epwh4jILoAAAAM/hump-day-wednesday.gif', 'https://media.tenor.com/0xLbZTLNJ8gAAAAM/wednesday-morning.gif', 'https://media.tenor.com/u3TIrewbgAsAAAAM/butterfly.gif', 'https://media.tenor.com/DEdOQDRlLcAAAAAM/animated-text.gif', 'https://media.tenor.com/z_1tDd5zkaUAAAAM/good-morning.gif', 'https://media.tenor.com/KVBFO73zK_gAAAAM/wednesday-good.gif', 'https://media.tenor.com/9rW40su5CzUAAAAM/wednesday-morning.gif', 'https://media.tenor.com/cK70MjsuWI8AAAAM/wednesday-hump-day.gif', 'https://media.tenor.com/wjPgfJPMEQ8AAAAM/wednesday-morning.gif', 'https://media.tenor.com/sKJsfqYH0QkAAAAM/good-morning.gif', 'https://media.tenor.com/N8tob-LB9e0AAAAM/good-wednesday-morning-happy-wednesday.gif', 'https://media.tenor.com/-TSy-bYYJE0AAAAM/wednesday-blessings.gif', 'https://media.tenor.com/ncXW-LAtZVgAAAAM/blessings-good.gif', 'https://media.tenor.com/aDcZXpTgSt8AAAAM/blessed-wednesday-morning.gif', 'https://media.tenor.com/0LmF0ddcBGAAAAAM/wednesday-happy.gif', 'https://media.tenor.com/aCYQi8M_Bc0AAAAM/wednesday-good.gif', 'https://media.tenor.com/595zVBhhZaUAAAAM/garfield-coffee.gif', 'https://media.tenor.com/maH8vvDXmhgAAAAM/this-morning-everyone.gif', 'https://media.tenor.com/FUQCXyOxaAEAAAAM/weekend-nice.gif', 'https://media.tenor.com/gcdSM2zhyC0AAAAM/2024-new-year-images-with-quotes-happy-new-year-2024-images-with-quotes.gif', 'https://media.tenor.com/j_bkOhu-wdQAAAAM/wednesday-have-a-wonderful-wednesday.gif', 'https://media.tenor.com/ETtiW5HmcMQAAAAM/bless-you.gif', 'https://media.tenor.com/XCP4a0muZaoAAAAM/good-morning-images-new-2023.gif', 'https://media.tenor.com/Oyv2HlPS6f4AAAAM/morning-good.gif', 'https://media.tenor.com/KlmGPt-Ec4AAAAAM/wednesday-vec50.gif', 'https://media.tenor.com/a0o-EBzAl24AAAAM/wednesday-blessings.gif', 'https://media.tenor.com/pN4zLC5TQdcAAAAM/happy-wednesday.gif', 'https://media.tenor.com/ckaWfGyUI-AAAAAM/morning-goodmorning.gif', 'https://media.tenor.com/cpSxW2y0RLIAAAAM/wednesday-morning-greetings.gif', 'https://media.tenor.com/yI03uWWIjN0AAAAM/happy-wednesday.gif', 'https://media.tenor.com/ZG3h5kVuIZYAAAAM/good-morning.gif', '/assets/img/gif-maker-entrypoints/search-entrypoint-optimized.gif', 'https://media.tenor.com/878K-sA4_2AAAAAM/wednesday-blessings.gif', 'https://media.tenor.com/_XmDS3I882MAAAAM/happy-wednesday-wednesday.gif', 'https://media.tenor.com/dB3hawnSyfkAAAAM/good-morning.gif', 'https://media.tenor.com/YQcl1iAAWnYAAAAM/animated-text.gif', 'https://media.tenor.com/EKulpfuuIUAAAAAM/happy-wednesday.gif', 'https://media.tenor.com/CAVuIKo9_twAAAAM/blessed-wednesday.gif', 'https://media.tenor.com/YIWf8TF3QkEAAAAM/morning-butterfly.gif', 'https://media.tenor.com/8axIdPOs0y0AAAAM/wednesday-happywednesday.gif', 'https://media.tenor.com/Y2v6Pzq9AEIAAAAM/good-morning-wednesday-wednesday-blessings.gif', 'https://media.tenor.com/-lO30FeY5EEAAAAM/good-morning-images-new-2023-good-morning.gif', 'https://media.tenor.com/PocNnkPYTtEAAAAM/happy-wednesday-wednesday.gif', 'https://media.tenor.com/UmrLsC4414gAAAAM/good-morning.gif', 'https://media.tenor.com/LvB0MXSV2hQAAAAM/have-a-beautiful-day-wednesday-morning.gif', 'https://media.tenor.com/MH5lukEt3DwAAAAM/good-morning.gif', 'https://media.tenor.com/-LqoqA8KBN8AAAAM/tee-tess.gif', 'https://media.tenor.com/eMj5agWP8X0AAAAM/good-wednesday-morning.gif', 'https://media.tenor.com/3rW9vppw-1kAAAAM/goodmornibg-happywednesday.gif']
thursday = ['https://media.tenor.com/kNF5MC-M5FgAAAAM/thursday.gif', 'https://media.tenor.com/Y52QRE8P8sQAAAAM/thursday-morning.gif', 'https://media.tenor.com/TIsZPB_Ofx8AAAAM/thursday-donderdag.gif', 'https://media.tenor.com/SPz5OF9NSVMAAAAM/good-thursday-morning.gif', 'https://media.tenor.com/SyBzGwyrzRIAAAAM/happy-thursday-thursday.gif', 'https://media.tenor.com/WWarvffkAX8AAAAM/good-morning.gif', 'https://media.tenor.com/SAjEZ7trvPIAAAAM/do-vec50do.gif', '/assets/img/gif-maker-entrypoints/search-entrypoint-optimized.gif', 'https://media.tenor.com/9Dlo_Cb7974AAAAM/thursday-good.gif', 'https://media.tenor.com/oYl3f2OjCvwAAAAM/god-blessing.gif', 'https://media.tenor.com/9GjX9ZOJjkwAAAAM/cat-lol.gif', 'https://media.tenor.com/VqW90LGvnYsAAAAM/goodmorning-sunrise.gif', 'https://media.tenor.com/ev6Eltc7X04AAAAM/good-morning.gif', 'https://media.tenor.com/vqL3vjPmSiQAAAAM/happy-thursday-funny.gif', 'https://media.tenor.com/n6PXyAxR6l0AAAAM/happy-thursday-snoopy.gif', 'https://media.tenor.com/omreym6hTvwAAAAM/happy-thursday-thursday.gif', 'https://media.tenor.com/2l-VDqiXamoAAAAM/good-morning.gif', 'https://media.tenor.com/X4OUxqPTvdEAAAAM/thursday-good.gif', 'https://media.tenor.com/fMJXA-gbEIMAAAAM/happy-thursday.gif', 'https://media.tenor.com/y9jRpb2VubUAAAAM/thursday-happy.gif', 'https://media.tenor.com/HIsirNecamMAAAAM/thursday-morning.gif', 'https://media.tenor.com/OHs5NJ2rgOwAAAAM/pandb-betty.gif', 'https://media.tenor.com/aLBXevBkHzoAAAAM/good-morning-happy-morning.gif', 'https://media.tenor.com/e4qAeUT0u0gAAAAM/disn-positive.gif', 'https://media.tenor.com/_4EQOrp3fpYAAAAM/happy-thursday-thursday.gif', 'https://media.tenor.com/CTWYHKzMzOYAAAAM/happy-birthday-thursday.gif', 'https://media.tenor.com/paSXw6HQvKMAAAAM/thursday-morning.gif', 'https://media.tenor.com/rctEsL9puIcAAAAM/monkey-thursday.gif', 'https://media.tenor.com/3G-Xzl2Ynz8AAAAM/thursday-morning.gif', 'https://media.tenor.com/KBhRrLD3x5QAAAAM/thursday.gif', 'https://media.tenor.com/SJaXaEwbzk4AAAAM/thursday-morning.gif', 'https://media.tenor.com/53dXdju8SDwAAAAM/thursday-dancing.gif', 'https://media.tenor.com/dlsxh8Pe2XEAAAAM/thursday-good.gif', 'https://media.tenor.com/cMHStAJymq0AAAAM/thankful-thursday.gif', 'https://media.tenor.com/OZTlZeN3WTEAAAAM/thursday-snoopy.gif', 'https://media.tenor.com/R1wZoZKUv5gAAAAM/thursday-morning.gif', 'https://media.tenor.com/M3nDNKWiy8cAAAAM/good-morning.gif', 'https://media.tenor.com/0RwMOsHY0yAAAAAM/good-thursday-morning.gif', 'https://media.tenor.com/gl-PJ-V0_d0AAAAM/thursday-morning.gif', 'https://media.tenor.com/Mqa0yUwsqQUAAAAM/good-morning.gif', 'https://media.tenor.com/johxtuVkIZ8AAAAM/good-morning.gif', 'https://media.tenor.com/xFYUlPkY4xwAAAAM/good-morning-have-a-great-day.gif', 'https://media.tenor.com/Yrqz93twn1wAAAAM/thursday-morning.gif', 'https://media.tenor.com/qFSFqo7DfAMAAAAM/good-thursday-morning.gif', 'https://media.tenor.com/48bXn0aUxr0AAAAM/thankful-thursday.gif', 'https://media.tenor.com/FRL2sX7_CFgAAAAM/good-morning.gif', 'https://media.tenor.com/8tVg7QN6fb0AAAAM/thursday-morning.gif', 'https://media.tenor.com/R9wWvPbaM8wAAAAM/it%27s-thursday.gif', 'https://media.tenor.com/FRQqbYKAFIgAAAAM/animated-text.gif', 'https://media.tenor.com/wxL2ADD0FGgAAAAM/good-morning.gif']
friday = ['https://media.tenor.com/7kEdR_fp1w0AAAAM/friday-morning.gif', 'https://media.tenor.com/xpVPuma1EKsAAAAM/happy-friday.gif', 'https://media.tenor.com/naIJLMFPXuEAAAAM/friday-blessings.gif', 'https://media.tenor.com/gu7ZQURjxPsAAAAM/good-morning-friday.gif', 'https://media.tenor.com/RTHzSo8zYvcAAAAM/friday-morning.gif', 'https://media.tenor.com/oAFUGMGV-FMAAAAM/friday-blessings-and-prayers-quotes.gif', 'https://media.tenor.com/3miBA_1wP_8AAAAM/good-friday-morning.gif', 'https://media.tenor.com/16BWFaa6Lr8AAAAM/happy-friday.gif', 'https://media.tenor.com/Y07r9QvkYjgAAAAM/happy-friday.gif', 'https://media.tenor.com/zLnVrAajPdAAAAAM/friday-excited.gif', 'https://media.tenor.com/NR2Vk9gAk-AAAAAM/good-morning-cute-gif.gif', 'https://media.tenor.com/ssCV0jCadTgAAAAM/happyfriday-friday.gif', 'https://media.tenor.com/aS_rMHnL_f8AAAAM/friday.gif', 'https://media.tenor.com/Nx50dGf1qeEAAAAM/good-morning.gif', 'https://media.tenor.com/wxvBOr6aN1IAAAAM/good-morning-friday-morning.gif', 'https://media.tenor.com/0JmD-PL4Q-8AAAAM/good-morning.gif', 'https://media.tenor.com/vGinlyGRAHEAAAAM/friday-dance.gif', 'https://media.tenor.com/S1Khj2R5L_gAAAAM/happy-weekend-it%27s-friday.gif', 'https://media.tenor.com/-hk_deAdCMYAAAAM/friday-friday-dance.gif', 'https://media.tenor.com/MTCyAIJe7x0AAAAM/happy-cat.gif', 'https://media.tenor.com/LRqkLhdmDoUAAAAM/friday-finally-friday.gif', 'https://media.tenor.com/6N7m4lCVl84AAAAM/happy-friday.gif', 'https://media.tenor.com/DDui6i1NEksAAAAM/need-coffee-for-you.gif', 'https://media.tenor.com/9TZ1YfkrExsAAAAM/friday.gif', 'https://media.tenor.com/ZE6hBQJPqVAAAAAM/good-friday-morning.gif', 'https://media.tenor.com/az860KbOh4QAAAAM/happy-friday.gif', 'https://media.tenor.com/VoXc6C_SkzUAAAAM/tgif-13.gif', 'https://media.tenor.com/iPF8LFWARbgAAAAM/good-friday-morning.gif', 'https://media.tenor.com/GZDRW92MCGwAAAAM/happy-friday-friday-morning.gif', 'https://media.tenor.com/dvLY2gPYX-YAAAAM/friday-happy.gif', 'https://media.tenor.com/N5XCiQG4reUAAAAM/morning.gif', 'https://media.tenor.com/goKK9nKxXrEAAAAM/friday.gif', '/assets/img/gif-maker-entrypoints/search-entrypoint-optimized.gif', 'https://media.tenor.com/Srkc084IUngAAAAM/happy-friday.gif', 'https://media.tenor.com/aJOqh9TrzZMAAAAM/happy-friday.gif', 'https://media.tenor.com/wMwUqer8C1AAAAAM/thursday-happy.gif', 'https://media.tenor.com/xuX7q4fSRIoAAAAM/good-friday-morning.gif', 'https://media.tenor.com/L5WrkONWq3oAAAAM/mommy.gif', 'https://media.tenor.com/IJ8kgS008TUAAAAM/happy-friday-friday.gif', 'https://media.tenor.com/LpN8awERo1YAAAAM/andras-andrascsuka.gif', 'https://media.tenor.com/qU-NcgA03dgAAAAM/good-morning.gif', 'https://media.tenor.com/Ow-rLMiWVPkAAAAM/friday-blessings-and-prayers-quotes.gif', 'https://media.tenor.com/Jvs4u2XVCtoAAAAM/good-friday-morning.gif', 'https://media.tenor.com/R7qbwWdyQq8AAAAM/friday-blessings.gif', 'https://media.tenor.com/4dyQbbiyamgAAAAM/good-mornin-good-morning.gif', 'https://media.tenor.com/QzpvmN5jbRIAAAAM/happy-friday.gif', 'https://media.tenor.com/W2Pqsj39nQcAAAAM/good-morning-happy-friday.gif', 'https://media.tenor.com/UNxx11CLwIcAAAAM/happy-friday-friday-blessings.gif', 'https://media.tenor.com/1sRmv1ecOYsAAAAM/good-friday-morning.gif', 'https://media.tenor.com/6cZ023QBUFwAAAAM/friday-good.gif']
saturday = ['https://media.tenor.com/1WfOue1TXIMAAAAM/goodmorning.gif', 'https://media.tenor.com/ppc3-hDiE6AAAAAM/monkey.gif', 'https://media.tenor.com/OxOocqMcUMAAAAAM/saturday.gif', 'https://media.tenor.com/3d87UtCwBD4AAAAM/saturday-happy-weekend.gif', 'https://media.tenor.com/5mKsminw5aEAAAAM/happy-saturday.gif', 'https://media.tenor.com/bBju7bpLYccAAAAM/happy-saturday-good-morning.gif', 'https://media.tenor.com/Zs7FCEK6BYAAAAAM/good-morning-images.gif', '/assets/img/gif-maker-entrypoints/search-entrypoint-optimized.gif', 'https://media.tenor.com/HDwRagpG7OMAAAAM/saturday-blessings.gif', 'https://media.tenor.com/cXrj3is_KEwAAAAM/happy-day.gif', 'https://media.tenor.com/484Gj-7EoXAAAAAM/saturday.gif', 'https://media.tenor.com/N3vjBT6EMjgAAAAM/saturday-blessings.gif', 'https://media.tenor.com/NhauDj80i6kAAAAM/saturday-blessings.gif', 'https://media.tenor.com/WzXcY9wM_bQAAAAM/happy-dance.gif', 'https://media.tenor.com/K13OKcPT3QwAAAAM/saturday.gif', 'https://media.tenor.com/zCYtScQgF_8AAAAM/monkey.gif', 'https://media.tenor.com/0JJTTugw5LwAAAAM/good-morning-have-a-great-saturday.gif', 'https://media.tenor.com/u7Vz6gZvZnMAAAAM/good-morning-saturday.gif', 'https://media.tenor.com/AFVTfS2J4HYAAAAM/good-morning.gif', 'https://media.tenor.com/Wv16uU6_RYQAAAAM/its-saturday-flower.gif', 'https://media.tenor.com/SF5NacuoLpAAAAAM/saturday-good.gif', 'https://media.tenor.com/L_K1wYbW9AkAAAAM/saturday-good.gif', 'https://media.tenor.com/LazvsAjPSrIAAAAM/happy-weekend-sunny-day.gif', 'https://media.tenor.com/Z73V6iTLpncAAAAM/saturday-morning.gif', 'https://media.tenor.com/Ys-Sdu4Qx7QAAAAM/fancy-cat-aristocats.gif', 'https://media.tenor.com/s2gulM9v1DkAAAAM/saturday-good.gif', 'https://media.tenor.com/vujYwMT3XBQAAAAM/have-a-blessed-day-blessed-day.gif', 'https://media.tenor.com/oYsalqtZe0YAAAAM/feliz-s%C3%A1bado-saturday-morning.gif', 'https://media.tenor.com/I20vab7JK3UAAAAM/good-morning.gif', 'https://media.tenor.com/n9htQ4eWSDsAAAAM/happy-saturday.gif', 'https://media.tenor.com/_s46ABUkxBUAAAAM/friends-good-luck.gif', 'https://media.tenor.com/LeVD8RwsNwEAAAAM/saturday-morning.gif', 'https://media.tenor.com/yREKQDzfaxIAAAAM/good-morning.gif', 'https://media.tenor.com/dDrqLNsvEwkAAAAM/good-morning.gif', 'https://media.tenor.com/PRuQ-kbukPIAAAAM/happy-saturday.gif', 'https://media.tenor.com/N_zIUbHx0QcAAAAM/happy-saturday-morning.gif', 'https://media.tenor.com/eii5teZQt4wAAAAM/good-morning.gif', 'https://media.tenor.com/7bswcpyrekwAAAAM/saturday-happy.gif', 'https://media.tenor.com/rhnKX5EBPjwAAAAM/almost-the-weekend.gif', 'https://media.tenor.com/YZV5WFH6C0kAAAAM/good-morning.gif', 'https://media.tenor.com/6s1otWSADUQAAAAM/saturday-vec50.gif', 'https://media.tenor.com/CcnG2DAwSNUAAAAM/good-morning.gif', 'https://media.tenor.com/jnjfrnzbwnsAAAAM/saturday-happy.gif', 'https://media.tenor.com/eVh8rAvN2IQAAAAM/saturday-happy.gif', 'https://media.tenor.com/LbTuSdVE13gAAAAM/hello-good-morning.gif', 'https://media.tenor.com/iFVjoXp1b0kAAAAM/good-saturday-morning.gif', 'https://media.tenor.com/minb0Uc8hzMAAAAM/good-morning.gif', 'https://media.tenor.com/3CZrDFgv3WkAAAAM/happy-saturday-good-morning-happy-saturday.gif', 'https://media.tenor.com/K6SnPNrKMeIAAAAM/saturday-happy.gif', 'https://media.tenor.com/fgrh_R802HYAAAAM/saturday-blessings.gif']
sunday = ['https://media.tenor.com/nkSeBeHauf8AAAAM/sunday.gif', 'https://media.tenor.com/ZLy-VTZOFbIAAAAM/happy-sunday.gif', 'https://media.tenor.com/NH3pMu6Ix14AAAAM/svaradio-fm-have-a-sweet-sunday.gif', 'https://media.tenor.com/cjCKTshuR3YAAAAM/thank-you.gif', 'https://media.tenor.com/cvnevEPRprwAAAAM/sunday-august-20-2023.gif', 'https://media.tenor.com/nTQMVYxkEOwAAAAM/sunday.gif', 'https://media.tenor.com/V90wNO833-cAAAAM/happy-saturday-quotes.gif', 'https://media.tenor.com/Oyv2HlPS6f4AAAAM/morning-good.gif', 'https://media.tenor.com/FRpxz1E5A-kAAAAM/good-morning.gif', 'https://media.tenor.com/wwBVMtv9ArAAAAAM/sunday.gif', 'https://media.tenor.com/U0TUK1V54lEAAAAM/good-morning.gif', 'https://media.tenor.com/fu9EITcr6j8AAAAM/text-flashy.gif', 'https://media.tenor.com/jG6DsMFP90YAAAAM/fatdog-dog.gif', 'https://media.tenor.com/Z-Y-SUYp3ZUAAAAM/sunday-sunday-blessings.gif', 'https://media.tenor.com/tTzSb0Hq7rwAAAAM/go-to.gif', 'https://media.tenor.com/BXKyQOs6-8IAAAAM/what-a-sunny-day.gif', 'https://media.tenor.com/6T3JrkgN-mcAAAAM/good-morning.gif', 'https://media.tenor.com/QsbF9K0JdDEAAAAM/happy-sunday-good-morning.gif', 'https://media.tenor.com/CEcDfd7IAygAAAAM/sunday-quotes.gif', 'https://media.tenor.com/C-biv9wpKWAAAAAM/happy-sunday.gif', 'https://media.tenor.com/YJDzmSFQqRMAAAAM/sunday-blessings.gif', 'https://media.tenor.com/uJBDcyvDLm8AAAAM/sunday.gif', 'https://media.tenor.com/_s_TwgSj_YEAAAAM/sunday-good.gif', 'https://media.tenor.com/ZvnRSV_r4akAAAAM/good-morning-goodmorning.gif', 'https://media.tenor.com/KRoKw1bGi8MAAAAM/snejni-mische-good-morning.gif', 'https://media.tenor.com/YNdy7jIDu9QAAAAM/happy-sunday.gif', 'https://media.tenor.com/5YM03aJYcC8AAAAM/happy-sunday.gif', 'https://media.tenor.com/hK1w8G_oihwAAAAM/happy-sunday.gif', 'https://media.tenor.com/0NNdQUE5LY4AAAAM/sunday-blessings-have-a-blessed-day.gif', 'https://media.tenor.com/uRZak9t3KIwAAAAM/have-a-blessed-sunday-sunday.gif', 'https://media.tenor.com/t04ESEjIT7sAAAAM/happy-sunday.gif', 'https://media.tenor.com/z6f9ruQnGpcAAAAM/sunday.gif', 'https://media.tenor.com/IuabRmnI3MwAAAAM/butterfly-yellow-rose.gif', '/assets/img/gif-maker-entrypoints/search-entrypoint-optimized.gif', 'https://media.tenor.com/NttKL4XTVvsAAAAM/good-morning.gif', 'https://media.tenor.com/mSGwQkvVL8gAAAAM/happy-good.gif', 'https://media.tenor.com/fyAgLlTipQAAAAAM/sunday-good.gif', 'https://media.tenor.com/CF2HMXWhYvIAAAAM/1.gif', 'https://media.tenor.com/mAiSztoxZY4AAAAM/happy-sunday-blessings-for-a-wonderful-day.gif', 'https://media.tenor.com/HN_kRnTbWsIAAAAM/sunday-blessings.gif', 'https://media.tenor.com/BWnmGw5MpL0AAAAM/happy-sunday.gif', 'https://media.tenor.com/gxyTMV4AUL8AAAAM/good-morning.gif', 'https://media.tenor.com/j2iwVzuJhwYAAAAM/sunday-good.gif', 'https://media.tenor.com/fiMJzaNM2ZAAAAAM/sunday-good.gif', 'https://media.tenor.com/6UXJulkQDTUAAAAM/good-morning.gif', 'https://media.tenor.com/ypQ_Tjo_9i8AAAAM/sunday.gif', 'https://media.tenor.com/M6Jeks7LTnEAAAAM/sunday-afternoon.gif', 'https://media.tenor.com/M5KViIQAz7UAAAAM/sunday.gif', 'https://media.tenor.com/MT4dqIqJI-AAAAAM/sunday-good.gif', 'https://media.tenor.com/yjYZgndad7MAAAAM/fatdog-dog.gif']
days = {'monday': monday, 'tuesday': tuesday, 'wednesday': wednesday, 'thursday': thursday, 'friday': friday, 'saturday': saturday, 'sunday': sunday}
user_list = ['<@1170992311690342402>', '<@351008123320008704>', '<@992475596078719108>', '<@475155592290238469>', '<@567711558159826984>', '<@440544732888694789>', '<@1000260118266531860>', '<@793437786619248661>', '<@192513193359310848>']
timezone_dict = {}

def now_time():
    return datetime.datetime.now()


bot = commands.Bot(command_prefix="$", intents=intents)
TOKEN = os.getenv('TOKEN')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.tree.sync()
    gm.start()


@bot.hybrid_command()
async def snap(ctx, snap_username):
    url = f"https://www.snapchat.com/add/{snap_username}"

    def t():
        retries = 0
        while retries < 5:
            try:
                response = requests.request("GET", url)
                soup = BeautifulSoup(response.content, 'html.parser')
                res = soup.find('img')['srcset']
                return res
            except TypeError:
                retries += 1

    print('snap', ctx.message.author, snap_username)
    t = t()
    if t is not None:
        await ctx.send(t, ephemeral=False)
    else:
        await ctx.send('𝖓𝖔 𝖇𝖎𝖙𝖒𝖔𝖏𝖎 💔', ephemeral=False)


@bot.hybrid_command()
async def snap_secret(ctx, snap_username):
    url = f"https://www.snapchat.com/add/{snap_username}"

    def t():
        retries = 0
        while retries < 5:
            try:
                response = requests.request("GET", url)
                soup = BeautifulSoup(response.content, 'html.parser')
                res = soup.find('img')['srcset']
                return res
            except TypeError:
                retries += 1

    print('snap_secret', ctx.message.author, snap_username)
    t = t()
    if t is not None:
        await ctx.send(t, ephemeral=True)
    else:
        await ctx.send('𝖓𝖔 𝖇𝖎𝖙𝖒𝖔𝖏𝖎 💔', ephemeral=True)


@bot.hybrid_command()
async def in_days(ctx, num: int):
    now_time()
    print('in_days', ctx.message.author, num)
    if ctx.message.author.id not in timezone_dict and os.getenv(str(ctx.message.author.id)) is None:
        await ctx.send('please set your timezone first using the /timezone command', ephemeral=True)
    else:
        timezone_dict[str(ctx.message.author.id)] = os.getenv(str(ctx.message.author.id))
        try:
            time_change = datetime.timedelta(hours=int(timezone_dict[str(ctx.message.author.id)]))
            date1 = datetime.datetime.now()
            end_date = date1 + datetime.timedelta(days=int(num))
            final = datetime.datetime.timestamp(end_date) + time_change.total_seconds()
            await ctx.send(f'<t:{int(final)}:R>')
        except Exception as e:
            # Convert the exception to a string before sending it
            await ctx.send(f'invalid input --> {str(e)}')
            


@bot.hybrid_command()
async def in_time(ctx, year=now_time().year, month_number=now_time().month, day=now_time().day, hour=now_time().hour, minute=now_time().minute):
    now_time()
    print('in_time_est', ctx.message.author, year, month_number, day, hour, minute)
    if ctx.message.author.id not in timezone_dict and os.getenv(str(ctx.message.author.id)) is None:
        await ctx.send('please set your timezone first using the /timezone command', ephemeral=True)
    else:
        timezone_dict[str(ctx.message.author.id)] = os.getenv(str(ctx.message.author.id))
        try:
            time_change = datetime.timedelta(hours=int(timezone_dict[str(ctx.message.author.id)]))
            test = datetime.datetime.strptime(f'{year} {month_number} {day} {hour} {minute}', '%Y %m %d %H %M') + time_change
            test1 = int(datetime.datetime.timestamp(test))
            await ctx.send(f'<t:{test1}:R>')
        except Exception as e:
            await ctx.send(f"invalid date --> '{year} {month_number} {day} {hour} {minute}' does not match format 'year month day hour minute'")


@bot.hybrid_command()
async def date_time(ctx, year=now_time().year, month_number=now_time().month, day=now_time().day, hour=now_time().hour, minute=now_time().minute):
    now_time()
    print('in_time_est', ctx.message.author, year, month_number, day, hour, minute)
    if ctx.message.author.id not in timezone_dict and os.getenv(str(ctx.message.author.id)) is None:
        await ctx.send('please set your timezone first using the /timezone command', ephemeral=True)
    else:
        timezone_dict[str(ctx.message.author.id)] = os.getenv(str(ctx.message.author.id))
        try:
            time_change = datetime.timedelta(hours=int(timezone_dict[str(ctx.message.author.id)]))
            test = datetime.datetime.strptime(f'{year} {month_number} {day} {hour} {minute}', '%Y %m %d %H %M') + time_change
            test1 = int(datetime.datetime.timestamp(test))
            print('date_time_est', ctx.message.author.id, year, month_number, day, hour, minute)
            await ctx.send(f'<t:{test1}:F>')
        except Exception as e:
            await ctx.send(f"invalid date --> '{year} {month_number} {day} {hour} {minute}' does not match format 'year month day hour minute'")


@bot.hybrid_command()
async def c_to_f(ctx, temp):
    print('c_to_f', ctx.message.author, temp)
    try:
        await ctx.send(f'{int((int(temp) * 1.8) + 32)} degree fahrenheit')
    except Exception as e:
        await ctx.send('invalid input -->      ', ephemeral=True)

@bot.hybrid_command()
async def f_to_c(ctx, temp):
    print('f_to_c', ctx.message.author, temp)
    try:
        await ctx.send(f'{(int(int(temp) - 32) * (5 / 9))} degree celsius')
    except Exception as e:
        await ctx.send('invalid input -->      ', ephemeral=True)

@bot.hybrid_command()
async def timezone(ctx, current_hour_for_you: int):
    try:
        if not 0 <= current_hour_for_you < 24:
            await ctx.send("Hour must be between 0 and 23.", ephemeral=True)
        else:
            current_est_hour = datetime.datetime.now().hour
            diff = current_hour_for_you - current_est_hour
            if diff > 19:
                diff -= 24
            timezone_dict[ctx.message.author.id] = diff
            with open('users.env', 'a') as f:
                f.write(f"{ctx.message.author.id}={diff}\n")
            print('timezone', ctx.message.author, current_hour_for_you, diff)
            await ctx.send("timezone has been set 😂😂😂😂😂😂", ephemeral=True)
    except Exception as e:
        print('timezone', ctx.message.author, current_hour_for_you, 'invalid')
        await ctx.send('invalid input', ephemeral=True)

@bot.hybrid_command()
async def funny_text(ctx, text):
    my_dict = {
        "a": "𝓪",
        "b": "𝓫",
        "c": "𝓬",
        "d": "𝓭",
        "e": "𝓮",
        "f": "𝓯",
        "g": "𝓰",
        "h": "𝓱",
        "i": "𝓲",
        "j": "𝓳",
        "k": "𝓴",
        "l": "𝓵",
        "m": "𝓶",
        "n": "𝓷",
        "o": "𝓸",
        "p": "𝓹",
        "q": "𝓺",
        "r": "𝓻",
        "s": "𝓼",
        "t": "𝓽",
        "u": "𝓾",
        "v": "𝓿",
        "w": "𝔀",
        "x": "𝔁",
        "y": "𝔂",
        "z": "𝔃",
        "A": "𝓐",
        "B": "𝓑",
        "C": "𝓒",
        "D": "𝓓",
        "E": "𝓔",
        "F": "𝓕",
        "G": "𝓖",
        "H": "𝓗",
        "I": "𝓘",
        "J": "𝓙",
        "K": "𝓚",
        "L": "𝓛",
        "M": "𝓜",
        "N": "𝓝",
        "O": "𝓞",
        "P": "𝓟",
        "Q": "𝓠",
        "R": "𝓡",
        "S": "𝓢",
        "T": "𝓣",
        "U": "𝓤",
        "V": "𝓥",
        "W": "𝓦",
        "X": "𝓧",
        "Y": "𝓨",
        "Z": "𝓩",
    }

    print('funny_text', ctx.message.author, text)
    await ctx.send(str(''.join([my_dict.get(i, i) for i in str(text)])), ephemeral=True)

# morning = datetime.time(hour=17, minute=12, second=0)
# print(morning)
# print(datetime.datetime.now())
# time_change = datetime.timedelta(seconds=15)
# print(time_change)
# test4 = datetime.datetime.now() + time_change
# test4 = test4.time()
# print(test4)

@tasks.loop(hours=24)
async def gm():
    print('started')
    target_time = 7
    now = datetime.datetime.now()
    target_datetime = now.replace(hour=target_time, minute=0, second=0, microsecond=0)
    if now > target_datetime:
        target_datetime += datetime.timedelta(days=1)
    delay = (target_datetime - now).total_seconds()
    print('THE DELAY IS', delay)
    await asyncio.sleep(delay)
    channel_id = 647615056426696705
    channel = bot.get_channel(channel_id)
    day_week = str(calendar.day_name[datetime.datetime.now().weekday()]).lower()
    await channel.send(f'{user_list[random.randint(0, len(user_list) - 1)]}')
    await channel.send(f'{days[day_week][random.randint(0, 49)]}')
    print('gm successful')

@gm.before_loop
async def before_gm():
    await bot.wait_until_ready()


bot.run(TOKEN)
