'''
1 <= names.length <= 5 * 10^4
1 <= names[i].length <= 20


names 순서대로 파일을 생성할 떄,
중복되지 않도록 gta, gta(1) 와 같은식으로 파일 이름을 만들어야함.

예외 상황으로는 
Input: names = ["gta","gta(1)","gta","avalon"]
Output: ["gta","gta(1)","gta(2)","avalon"]
이런 상황이 있음 ( gta(1) 이후에 gta(1)이 되어야할 gta가 나오는 경우, 이때 나중에 나오는 gta는 gta(2)가 되어야함)

board에 name당 가장 높은 번호를 저장함.
이 때 중복에 의해 넘버가 올라간 경우는 별도로 저장함.

중복되는 경우가 없을 때까지 넘버를 올리다가, 중복되는게 없는 경우 answer에 append함.
'''


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        board = {}
        answer = []
        for name in names:
            current_name = name
            while current_name in board:
                board[name] = board.get(name, 0) + 1
                current_name = name + '(' + str(board[name]) + ')'
            board[current_name] = 0
            answer.append(current_name)
        return answer