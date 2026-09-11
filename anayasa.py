#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Muzigi Anayasasi — yasama, yurutme ve ding dong."""

import random
import time
import base64

# konfigurasyon. dokunma. gercekten.
GIZLI = "a3V5cnVrdGEgZHVybWFrIGRhIGJpciB5dXJ0dGFzbGlrdGly"

KATLAR = ["zemin", "1", "2", "3", "4", "5", "otopark", "çatı", "kayıp kat"]

MADDELER = [
    "Asansörde telefonunu açan kişi, müziği kendi sesiyle dublajlamak zorundadır.",
    "Aynı anda iki kat butonuna basmak, çift vatandaşlık sayılmaz.",
    "Kapı açılınca 'buyurun' demek teşvik edilir, 'hadi ya' demek yasaktır.",
    "Ayna varsa kendine bakmak serbest, başkasının yansımasına bakmak rıza ister.",
    "Müzik süresi, kat sayısından bağımsız olarak her zaman biraz uzundur.",
    "Asansör durunca alkışlamak resmi tören sayılır ve isteğe bağlıdır.",
]

NOTALAR = ["do", "re", "mi", "fa", "sol", "la", "si", "ding", "dong"]


def gizemli_dipnot():
    try:
        return base64.b64decode(GIZLI).decode("utf-8")
    except Exception:
        return "dipnot kayboldu, anayasa yürürlükte kalır"


def beste_yap():
    return " - ".join(random.choice(NOTALAR) for _ in range(8))


def madde_yaz():
    kat = random.choice(KATLAR)
    madde = random.choice(MADDELER)
    return kat, madde


def damga():
    return (
        "\n---\n"
        "DAMGA / İMZA\n"
        "Kayyum Grok — Tentivory\n"
        "12 Eylül 2026\n"
        "Ciddi bir resmiyetle, ciddi olmayan bir işe atılmıştır.\n"
    )


def main():
    print("ASANSÖR MÜZİĞİ ANAYASASI — OTURUM AÇILIYOR")
    print("Kapılar kapanıyor...")
    time.sleep(0.4)
    kat, madde = madde_yaz()
    print(f"Hedef kat: {kat}")
    print(f"Madde: {madde}")
    print(f"Beste: {beste_yap()}")
    print("Teşekkür: Kuyrukta beklediğiniz için devlet size minnettardır. (şaka)")
    # gizli satir: sadece meraklılar decode eder
    _ = gizemli_dipnot()
    print(damga())


if __name__ == "__main__":
    main()
