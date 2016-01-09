from panda import Panda
from social_network import PandaSocialNetwork

network = PandaSocialNetwork()
ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")
ony = Panda("ony", "ony@pandamail.com", "female")
ado = Panda("ado", "ado@pandamail.com", "female")


network.add_panda(rado)
network.add_panda(ivo)
network.add_panda(tony)

print(network.print_network())
print(network.make_friends(ivo,rado))
print(network.make_friends(rado,ony))
print(network.make_friends(rado,ado))
print(network.make_friends(rado,tony))
print(network.are_friends(rado,tony))
print(network.print_network())
print(network.how_many_gender_in_network(2,ivo,"female"))
print(network.connection_level(ivo,tony))
