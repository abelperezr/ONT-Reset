import telnetlib

#Host puede ser modificado a la IP correspondiente
HOST = "192.168.1.1" 
#user = el nombre del superusuario de la ONT
user = "aqui va nombre"
#password = contraseña de la ONT por telnet
password = "aqui va pass"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
#estos comandos son los que ejecutan el reinicio de fabrica depende del fabricante
tn.write(b"su admin\n")
tn.write(b"flash default cs\n")
tn.write(b"reboot\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
