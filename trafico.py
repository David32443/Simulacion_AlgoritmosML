# Description: Este script crea una red virtual con dos hosts y un switch, y ejecuta una prueba de ping entre los dos hosts. Luego,
# captura el tráfico de los hosts con tcpdump y genera tráfico de prueba entre los hosts. Finalmente, detiene la red virtual.

from mininet.net import Mininet # liberia de mininet para crear la red virtual
from mininet.node import Controller, DefaultController # libreria de mininet para crear el controlador
from mininet.link import TCLink # libreria de mininet para crear los enlaces
from mininet.log import setLogLevel # libreria de mininet para establecer el nivel de log

def simple_topology():
    # Crear la red
    net = Mininet(controller=DefaultController, link=TCLink)

    print("Creando nodos...")
    h1 = net.addHost('h1') #crea un host con el nombre h1 #un host es un dispositivo final que se conecta a una red y tiene una dirección IP asignada
    h2 = net.addHost('h2') #crea un host con el nombre h2
    s1 = net.addSwitch('s1') #crea un switch con el nombre s1
    c0 = net.addController('c0') #crea un controlador con el nombre c0

    print("Creando enlaces...")
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    print("Iniciando la red...")
    net.start()
    c0.start()
    s1.start([c0])

    print("Ejecutando prueba de ping...")
    net.ping([h1, h2])

    print("Capturando tráfico con tcpdump...")
    h1.cmd('tcpdump -w h1-traffic.pcap &')
    h2.cmd('tcpdump -w h2-traffic.pcap &')

    print("Generando tráfico de prueba...")
    h1.cmd('ping -c 10 {}'.format(h2.IP()))

    print("Deteniendo la red...")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simple_topology()
