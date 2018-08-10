class player:

    def __init__(self, str_name, time):
        self.name = str_name
        self.alive_time = time
        self.score = 0
        self.kill_num = 0
        self.killed_by = 0

    def __str__(self):
        return self.name + ' ' + str(self.score)


class turn:
    
    def __init__(self, Q, M, dict, list1, A, B, list2):
        self.Q = Q
        self.M = M
        self.rank_sco_dict = dict
        self.kill_sco_list = list1
        self.A = A
        self.B = B
        self.game_process = list2
        self.player_list = []
        self.player_list.append(player('', 0))
        self.rank_dict = {}
    
    def add_player(self):
        self.player_list.append(player(self.game_process[-1][1], int(self.game_process[-1][0])))
        self.rank_dict[self.game_process[-1][1]] = 1      
        r = 2
        for i in self.game_process[-1:: -1]:
            p = player(i[2], int(i[0]))
            self.rank_dict[i[2]] = r
            self.player_list.append(p)
            p.killed_by = self.rank_dict[i[1]]
            self.player_list[self.rank_dict[i[1]]].kill_num += 1
            r += 1
    
    def update_score(self):
        for p in self.player_list[-1::-1]:
            if not p.name:
                continue
            else:
                if p.killed_by != 0 and p.killed_by != self.rank_dict[p.name]:
                    if p.kill_num < self.M:
                        self.player_list[p.killed_by].score += self.kill_sco_list[p.kill_num]
                    else:
                        self.player_list[p.killed_by].score += self.kill_sco_list[self.M]   
                p.score += self.A * p.alive_time + self.B    #alive_score
                p.score += self.rank_sco_dict[self.rank_dict[p.name]]     #rank_score  
 
    def res(self):
        self.player_list.sort(key = lambda x: x.name)
        for i in self.player_list:
            if not i.name:
                continue
            else:
                print(i.__str__())


def input_one_turn():
    Q, N, M = map(int,input().split())
    rank_sco_dict = {}
    for i in range(N):
        low, high, sco = map(int,input().split())
        for i in range(low, high + 1):
            rank_sco_dict[i] = sco
    kill_sco_list = [i for i in map(int, input().split())]
    A, B =  map(int,input().split())
    game_process = []
    while True:
        i = input()
        if not i:
            break
        else:
            game_process.append(i.split()[:3])
    t = turn(Q, M, rank_sco_dict, kill_sco_list, A, B, game_process)
    return t

T = int(input())
input()
turn_list = []
for i in range(T):
    turn_list.append(input_one_turn())
for j in turn_list:
    j.add_player()
    j.update_score()
    j.res()
    #print()