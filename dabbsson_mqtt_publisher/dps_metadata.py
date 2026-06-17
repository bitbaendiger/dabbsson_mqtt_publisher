batteryPercentage = {"unit_of_measurement": "%", "device_class": "battery"}
powerWatts        = {"unit_of_measurement": "W", "device_class": "power"}

DPS_METADATA = {
    # === Allgemein / Batterie ===
    "1":   {"name": "Batterie SoC",                   "type": "int",  "writable": False, "payload": batteryPercentage},
    "2":   {"name": "Verbleibende Zeit",              "type": "int",  "writable": False},
    "10":  {"name": "Temperatur",                     "type": "int",  "writable": False, "payload": {"unit_of_measurement": "°C", "device_class": "temperature"}},
    "101": {"name": "Batterie lädt",                  "type": "bool", "writable": False},
    "125": {"name": "Erweiterungsbatterie verbunden", "type": "bool", "writable": False},
    "138": {"name": "Erweiterungsbatterie 1",         "type": "int",  "writable": False, "payload": batteryPercentage},
    "139": {"name": "Erweiterungsbatterie 2",         "type": "int",  "writable": False, "payload": batteryPercentage},

    # === AC/USB/DC Steuerung ===
    "25":  {"name": "Beep (Tonsignal)",               "type": "bool", "writable": True},
    "109": {"name": "AC Ausgang EIN/AUS",             "type": "bool", "writable": True},
    "111": {"name": "DC 12V EIN/AUS",                 "type": "bool", "writable": True},
    "112": {"name": "USB 5V EIN/AUS",                 "type": "bool", "writable": True},
    "126": {"name": "P-BOOST",                        "type": "bool", "writable": True},

    # === Anzeige- & LED-Zustände ===
    "102": {"name": "LED-Status",                     "type": "str",  "writable": True},
    "127": {"name": "Systemmodus",                    "type": "str",  "writable": False},
    "128": {"name": "Smart Charging EIN/AUS",         "type": "bool", "writable": True},

    # === Leistungsmessung ===
    "103": {"name": "PV Eingang",                     "type": "int",  "writable": False, "payload": powerWatts},
    "104": {"name": "AC Eingang",                     "type": "int",  "writable": False, "payload": powerWatts},
    "105": {"name": "Batterie1 Out",                  "type": "int",  "writable": False, "payload": powerWatts},
    "106": {"name": "Batterie2 Out",                  "type": "int",  "writable": False, "payload": powerWatts},
    "107": {"name": "Ausgang Gesamt",                 "type": "int",  "writable": False, "payload": powerWatts},
    "108": {"name": "AC Ausgang Leistung",            "type": "int",  "writable": False, "payload": powerWatts},
    "110": {"name": "12V Ausgang",                    "type": "int",  "writable": False, "payload": powerWatts},
    "113": {"name": "USBA1 Leistung",                 "type": "int",  "writable": False, "payload": powerWatts},
    "114": {"name": "USBA2 Leistung",                 "type": "int",  "writable": False, "payload": powerWatts},
    "115": {"name": "USBA3 Leistung",                 "type": "int",  "writable": False, "payload": powerWatts},
    "116": {"name": "USBC1 Leistung",                 "type": "int",  "writable": False, "payload": powerWatts},
    "117": {"name": "USBC2 Leistung",                 "type": "int",  "writable": False, "payload": powerWatts},
    "118": {"name": "USBC3 Leistung",                 "type": "int",  "writable": False, "payload": powerWatts},
    "131": {"name": "Eingang Gesamtleistung",         "type": "int",  "writable": False, "payload": powerWatts},

    # === Lademodi & Leistung ===
    "123": {"name": "AC Ziel-Ladeleistung",           "type": "int",  "writable": True,  "payload": powerWatts},
    "124": {"name": "Fast/Slow Charge Hinweis",       "type": "bool", "writable": False},

    # === Zeitsteuerung ===
    "120": {"name": "AC Einschaltzeit",               "type": "str",  "writable": True},
    "121": {"name": "LCD Aus-Zeit",                   "type": "str",  "writable": True},
    "122": {"name": "AC Auto-Ausschaltzeit",          "type": "str",  "writable": True},

    # === Geräteinformationen ===
    "130": {"name": "PD Firmware",                    "type": "str",  "writable": False},
    "132": {"name": "BMS Firmware",                   "type": "str",  "writable": False},
    "133": {"name": "Inverter Firmware",              "type": "str",  "writable": False},
    "140": {"name": "Seriennummer",                   "type": "str",  "writable": False},
    "143": {"name": "OTA Update-Zeit",                "type": "int",  "writable": False},

    # === Steuerfunktionen ===
    "129": {"name": "Gerät ausschalten",              "type": "bool", "writable": True},
    "142": {"name": "Werksreset",                     "type": "bool", "writable": True},
    "144": {"name": "App-Heartbeat",                  "type": "bool", "writable": True},
    "145": {"name": "Netzspannung einstellen",        "type": "int",  "writable": True,  "payload": {"unit_of_measurement": "V", "device_class": "voltage"}},

    # === Fehlerstatus ===
    "134": {"name": "Inverter Fehler",                "type": "int",  "writable": False},
    "135": {"name": "USB PD Fehler",                  "type": "int",  "writable": False},
    "136": {"name": "BMS Fehler",                     "type": "int",  "writable": False},
    "137": {"name": "BMS Fehler 1",                   "type": "int",  "writable": False}
}
