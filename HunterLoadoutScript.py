import pyautogui
import time

time.sleep(0.1)

x, y = pyautogui.position()
print(f"Current position: X={x}, Y={y}")

def healths_chunks():
    # Cordinates of healths chunks bar
    x = 342
    y = 780
    # Click on cordinates
    pyautogui.moveTo(x, y)
    pyautogui.click()

    # Cordinates of q button
    x_q = 786
    y_q = 812
    # Click on cordinates
    pyautogui.moveTo(x_q, y_q)
    for _ in range(6):
        pyautogui.click()
        time.sleep(0.1)


    # Cordinates of e button
    x_e = 1043
    y_e = 811
    # Click on cordinates
    pyautogui.moveTo(x_e, y_e)
    for _ in range(6):
        pyautogui.click()
        time.sleep(0.1)

    # Cordinates of enter button
    x_enter = 1494
    y_enter = 820
    # Click on cordinates
    pyautogui.moveTo(x_enter, y_enter)
    pyautogui.click()

def hunter_perks():
    # Cordinates of perks button
    x = 200
    y = 470
    # Click on cordinates
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(0.2)

    ##Remove all start perks given
    #Cordinate of first perk
    x_perk = 1458
    y_perk = 238
    x_enter_1 = 1604
    y_enter_1 = 1037
    x_enter_2 = 1470
    y_enter_2 = 813
    for x in range(5):
        pyautogui.moveTo(x_perk, y_perk)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(x_enter_1, y_enter_1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(x_enter_2, y_enter_2)
        pyautogui.click()
        time.sleep(0.1)

    ##Equip new perks
    # Cordinate of search bar
    x_search_bar = 575
    y_search_bar = 583

    # Cordinate of perk from not equiped
    x_not_in_slot_perk = 227
    y_not_in_slot_perk = 682

    pyautogui.moveTo(x_search_bar, y_search_bar)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write('necromancer', interval=0.1)
    time.sleep(0.2)
    pyautogui.moveTo(x_not_in_slot_perk, y_not_in_slot_perk)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(x_enter_1, y_enter_1)
    pyautogui.click()
    time.sleep(0.2)

    pyautogui.moveTo(x_search_bar, y_search_bar)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write('resilience', interval=0.1)
    time.sleep(0.2)
    pyautogui.moveTo(x_not_in_slot_perk, y_not_in_slot_perk)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(x_enter_1, y_enter_1)
    pyautogui.click()
    time.sleep(0.2)

    x_esc = 58
    y_esc = 135
    pyautogui.moveTo(x_esc, y_esc)
    pyautogui.click()

def hunter_loadout():
    time.sleep(0.2)
    x_loadouts = 1546
    y_loadouts = 217
    pyautogui.moveTo(x_loadouts, y_loadouts)
    pyautogui.click()
    time.sleep(0.2)

    x_loadout = 1122
    y_loadout = 596
    pyautogui.moveTo(x_loadout, y_loadout)
    pyautogui.click()
    time.sleep(0.2)

    x_equip = 99
    y_equip = 1038
    pyautogui.moveTo(x_equip, y_equip)
    pyautogui.click()
    time.sleep(0.2)

#Call of all functions
healths_chunks()
hunter_perks()
hunter_loadout()
