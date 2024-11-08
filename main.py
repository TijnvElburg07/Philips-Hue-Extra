from phue import Bridge
import time

def access_lights():
    b = Bridge('192.168.2.3')
    b.connect()
    lights = b.get_light_objects('name')
    return lights

def spook_lights():
    lights = access_lights()
    for light_name, light in lights.items():
        light.on = True
        time.sleep(0.5)
        light.on = False
        time.sleep(0.5)
        light.on = True

def all_lights_on():
    lights = access_lights()
    for light_name, light in lights.items():
        if not light.on:
            light.on = True
        else:
            print(f"{light_name} is already on.")

def all_lights_off():
    lights = access_lights()
    for light_name, light in lights.items():
        if light.on:
            light.on = False
        else:
            print(f"{light_name} is already off.")       

def display_lights_name():
    lights = access_lights()
    for light_name in lights.keys():
        print(light_name)

def change_light_color(color):
    lights = access_lights()
    for light_name, light in lights.items():
        light.on = True
        light.hue = color
        time.sleep(1)
        

def changeIntensityUp(amount):
    lights = access_lights()
    for light_name, light in lights.items():
        light.brightness = min(light.brightness + amount, 254)

def changeIntensityDown(amount):
    lights = access_lights()
    for light_name, light in lights.items():
        light.brightness = max(light.brightness - amount, 0)


while True:
    print("----------------------------------------------------------------")
    print("0. Exit")
    print("1. Spook lights")
    print("2. All lights on")
    print("3. All lights off")
    print("4. Display lights name")
    print("5. Change light color (Kan je alleen gebruiken met kleurlampen van hue)")
    print("6. Change light intensity up")
    print("7. Change light intensity down")
    print("----------------------------------------------------------------")
    choice = input("Enter your choice: ")
    print("----------------------------------------------------------------")
    if choice == "1":
        spook_lights()
    elif choice == "2":
        all_lights_on()
    elif choice == "3":
        all_lights_off()
    elif choice == "4":
        display_lights_name()
    elif choice == "5":
        returnColor = int(input("Enter the color number (0 - 65535): "))
        change_light_color(returnColor)
    elif choice == "6":
        returnNumber = int(input("Enter the amount to increase the intensity: "))
        changeIntensityUp(returnNumber)
    elif choice == "7":
        returnNumber = int(input("Enter the amount to decrease the intensity: "))
        changeIntensityDown(returnNumber)
    elif choice == "0":
        break
    else:
        print("Invalid choice")
