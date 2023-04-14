import psutil
from plyer import notification

battery = psutil.sensors_battery()
percentage = battery.percent

if percentage >= 70:
    notification.notify(
        title='Battery Warning',
        message= f'{percentage}% Full Battery',
        timeout=5
    )

elif 70 > percentage > 20:
    notification.notify(
        title='Battery Warning',
        message= f'{percentage}% Good Battery',
        timeout=5
    )

else:
    notification.notify(
        title='Battery Warning',
        message= f'{percentage}% It Needs to be charged!! ',
        timeout=5
    )