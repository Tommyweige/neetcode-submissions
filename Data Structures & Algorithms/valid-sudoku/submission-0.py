class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = defaultdict(list)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    table[num].append([i,j])
        print(table.items)
        for key, value in table.items():
            print(f"數字 {key} 出現的位置有：{value}")

            rows = [pos[0] for pos in value]
            if len(rows) != len(set(rows)):
                return False

            column = [pos[1] for pos in value]
            if len(column) != len(set(column)):
                return False

            block = [(pos[0] // 3, pos[1] // 3) for pos in value]
            if len(block) != len(set(block)):
                return False
                
        return True

            


            