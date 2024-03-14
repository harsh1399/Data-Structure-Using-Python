class Solution:
    def topologicalSort(self, graph, char_mapping):
        inOrder = [0] * len(char_mapping)
        sortedOrder = []
        queue = []
        for vertex_ind in range(len(graph)):
            for adj_node in graph[vertex_ind]:
                inOrder[adj_node] += 1
        for i in range(len(inOrder)):
            if inOrder[i] == 0:
                queue.append(i)
        while len(queue) != 0:
            vertex = queue.pop(0)
            sortedOrder.append(char_mapping[vertex])
            for adj_node in graph[vertex]:
                inOrder[adj_node] -= 1
                if inOrder[adj_node] == 0:
                    queue.append(adj_node)
        return sortedOrder

    def findOrder(self, alien_dict, N, K):
        graph = [[] for i in range(K)]
        char_mapping = {}
        charToNum = {}
        count = 0
        for i in range(1, N):
            smallest_len = 0
            print(i)
            if len(alien_dict[i - 1]) < len(alien_dict[i]):
                smallest_len = len(alien_dict[i - 1])
            else:
                smallest_len = len(alien_dict[i])
            j = 0
            while j < smallest_len:
                if alien_dict[i - 1][j] != alien_dict[i][j]:
                    if alien_dict[i-1][j] not in charToNum:
                        char_mapping[count] = alien_dict[i - 1][j]
                        charToNum[alien_dict[i-1][j]] = count
                        count += 1
                    if alien_dict[i][j] not in charToNum:
                        char_mapping[count] = alien_dict[i][j]
                        charToNum[alien_dict[i][j]] = count
                        count += 1
                    graph[charToNum[alien_dict[i-1][j]]].append(charToNum[alien_dict[i][j]])
                    break
                j += 1
        sortedOrder = self.topologicalSort(graph, char_mapping)
        if len(sortedOrder) != K:
            a = 97
            sortedOrder.append(chr(97+K-1))
        return sortedOrder

if __name__ == "__main__":
    sol = Solution()
    input = ['bhhb','blkbggfecalifjfcbkjdicehhgikkdhlachlgbhji' ,'cfjjhcifladadbgcleggjgbcieihabcglblflgajgkejccj', 'dlgdhiha' ,'ehggedljjhfldcajeceaeehkalkfeidhigkifjl' ,'gdalgkblahcldahledfghjb' ,'geldbblaaflegjhlfjlgblfbdc' ,'ibjceciedbiilkjliijgklcgliaeeic' ,'jcebjkfgfibfckfiikklecihik', 'jdkcabjjjckgdblkljf' ,'jijlbjbliigkffhkchkclkhafbiiiblcglhfjkflbjjkih' ,'kfd' ,'lhdgidialgabfklffahiihceflebfidl']
    sol.findOrder(input,13,12)