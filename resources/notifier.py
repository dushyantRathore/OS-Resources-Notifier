import notify2


def send_notification(title, message):
    notify2.init("OS Resources Notifier")
    n = notify2.Notification(title, message)
    n.show()