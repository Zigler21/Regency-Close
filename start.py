import pyautogui
import time

hotkey = pyautogui.hotkey

click = pyautogui.click

write = pyautogui.typewrite

locate = pyautogui.locateOnScreen

wait = time.sleep

presskey = pyautogui.press

#Reports back on any clicked images and their pos.
def click_on_image(image_path):
    try:
        image_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
        click(image_location)
        print(f"Found and clicked on image at {image_location}")
    except Exception as e:
        print(f"Could not find image: {e}")

defaultwait = time.sleep(0)

confirm = input('Make sure there is nothing on RTS, just login and press enter to continue')

#Gets the ticket report box, prints it and saves it as a PDF.
if confirm == '':
    wait(5)
    hotkey('alt', 'r')
    wait(.5)
    write('t')
    wait(.5)
    hotkey('enter')
    wait(.5)
    write('d')
    wait(.5)
    click_on_image('view-ticket.png')
    #This opens the view ticket document
    wait(5)
    presskey('right')
    wait(.5)
    hotkey('enter')
    wait(7)
    click_on_image('printbutton.PNG')
    wait(1)
    hotkey('enter')
    wait(.5)
    click_on_image('savebutton.PNG')
    wait(.5)
    click_on_image('pdfbutton.PNG')
    wait(1)
    hotkey('enter')
    wait(.3)
    hotkey('enter')
    wait(3)
    #after this we close the document and the pop up window for it
    click_on_image('closedoc.PNG')
    wait(1)
    click_on_image('closeblue.PNG')
    wait(.5)
    #here we get the deposit report
    hotkey('alt', 'r')
    wait(.2)
    hotkey('enter')
    wait(.3)
    click_on_image('total.png')
    wait(2)
    click_on_image('viewdep.png')
    wait(7)
    click_on_image('printbutton.PNG')
    wait(1)
    hotkey('enter')
    wait(.5)
    click_on_image('savebutton.PNG')
    wait(1)
    click_on_image('pdfbutton.PNG')
    wait(1)
    hotkey('enter')
    wait(.3)
    hotkey('enter')
    wait(3)
     #closes document and popup
    click_on_image('closedoc.PNG')
    wait(1)
    click_on_image('depclose.png')
    wait(3)
    #open inv report
    hotkey('alt', 'r')
    wait(.3)
    write('i')
    wait(.2)
    for i in range(2):
        write('c')
        time.sleep(0.2)
    hotkey('enter')
    wait(.5)
    hotkey('enter')
    wait(7)
    click_on_image('savebutton.PNG')
    wait(.5)
    click_on_image('pdfbutton.PNG')
    wait(3)
    hotkey('enter')
    input('Press Enter to continue')