import sys
import time

def jalanin_lagu():
    lirik = [

        ("Ittai doushiyou kono omoi wo", 2.0),
        ("Doushiyou abara no oku wo", 1.9),
        ("Zarame ga tokete gero ni narisou (Bang!)", 3.5),
        ("Doukou bachi hiraite obore shinisou", 2.9),
        ("Ima kono yo de kimi dake daiseikai", 3.8)
    ]

    for teks, tempo in lirik:
        print(teks)
        sys.stdout.flush()
        time.sleep(tempo)

jalanin_lagu()
