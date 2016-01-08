from collections import deque
from panda import Panda

class PandaSocialNetwork():

    def __init__(self):
        self.social_network = {}

    def has_panda(self, panda):
        if panda in self.social_network.keys():
            return True
        return False

    def bfs(self, graph, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    def connection_level(self, panda1, panda2):
        if self.has_panda(panda1) and self.has_panda(panda2):
            if self.bfs(self.social_network, panda1, panda2) is None:
                return -1
            len_connection = len(self.bfs(self.social_network, panda1, panda2))
            if len_connection == 2:
                return 1
            elif len_connection > 2:
                return len_connection - 1
        else:
            return False

    def add_panda(self, panda):
        dict_panda = {}
        if self.has_panda(panda) is True:
        else:
            dict_panda[panda] = []
            self.social_network.update(dict_panda)

    def print_network(self):
        return self.social_network

    def are_friends(self, panda1, panda2):
        if self.has_panda(panda1) is True and self.has_panda(panda2) is True:
            if len(self.social_network.get(panda1)) > 0:
                if panda2 in self.social_network.get(panda1):
                    return True
                else:
                    return False
        return False

    def make_friends(self, panda1, panda2):
        if self.are_friends(panda1, panda2):
        else:
            if not self.has_panda(panda1):
                self.add_panda(panda1)
            if not self.has_panda(panda2):
                self.add_panda(panda2)
            self.social_network[panda1].append(panda2)
            self.social_network[panda2].append(panda1)
            

    def are_connected(self,panda1, panda2):
        if not self.connection_level(panda1,panda2):
            return False
        else:
            return True

    def friends_of(self, panda):
        return self.social_network.get(panda)

    def how_many_gender_in_network(self, level, panda, gender):
        gen = 0
        for el in self.social_network:
            if self.connection_level(el, panda) == level and el.gender() == gender:
                gen+=1
        return gen

