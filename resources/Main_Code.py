from pyspectator.computer import Computer
import click
import notifier

computer = Computer()


def os_details():  # Get the OS details
    return computer.os


def processor_details():  # Get the processor details
    return computer.processor.name


def architecture():  # Architecture details
    return computer.architecture


def hostname():  # Get the host name
    return computer.hostname


def python_version():  # Get the python version
    return computer.python_version


def up_time():  # Get the uptime
    return computer.uptime


def boottime(): # Get the boot_time
    return computer.boot_time


def gettemp(): # Get the load
    return str(computer.processor.temperature)


def getload(): # Get the CPU Temp
    return str(computer.processor.load)

# Notification Main Section


@click.command()
@click.option('--os', is_flag=True, help="Lists the OS Details")
@click.option('--processor', '-p', is_flag=True, help="Lists the processor details")
@click.option('--arch', is_flag=True, help="Lists the architecture details")
@click.option('--host', '-h', is_flag=True, help = "Lists the host details")
@click.option('--python', is_flag=True, help="Lists the python version being used")
@click.option('--uptime', '-ut', is_flag=True, help="Lists the uptime")
@click.option('--bt', is_flag=True, help="Lists the boot time")
@click.option('--temp', is_flag=True, help="Lists the CPU temperatures")
@click.option('--load', is_flag=True, help="Lists the CPU load")


def cli(os,processor,arch,host,python,uptime,bt,temp,load) :

    if os:
        r = os_details()
        notifier.send_notification("Operating System", r)
    elif processor:
        p = processor_details()
        notifier.send_notification("Processor", p)
    elif arch:
        a = architecture()
        notifier.send_notification("Architecture", a)
    elif host:
        h = hostname()
        notifier.send_notification("Host Name", h)
    elif python:
        v = python_version()
        notifier.send_notification("Python Version", v)
    elif uptime:
        ut = up_time()
        notifier.send_notification("Uptime", ut)
    elif bt:
        b = boottime()
        notifier.send_notification("Boot time", b)
    elif temp:
        t = gettemp()
        notifier.send_notification("Temperature in Celcius", t)
    elif load:
        l = getload()
        notifier.send_notification("CPU load in %", l)

if __name__ == '__main__':
    cli()
