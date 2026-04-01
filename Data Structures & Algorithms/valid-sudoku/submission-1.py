class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        table = defaultdict(list)
        """
        將數字跟出現的位置存入字典
       {'1': [[0, 0], [7, 4]], 
       '2': [[0, 1], [5, 4], [6, 6]], 
       '3': [[0, 4], [2, 8], [4, 5]], 
       '4': [[1, 0], [3, 8], [7, 3]], 
       '5': [[1, 3], [3, 0], [4, 8]], 
       '9': [[2, 1], [7, 5], [8, 8]], 
       '8': [[2, 2], [4, 3], [7, 8], [8, 4]], 
       '6': [[3, 4], [5, 8]], 
       '7': [[5, 0], [8, 7]]}
        """

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    table[num].append([i,j])
        print(table)

        # 讀取字典裏面的key 跟 value
        for key, value in table.items():

            # 將每一個數字存入的rows存入rows比對
            rows = [pos[0] for pos in value]

            # 如果rows的長度不等於rows集合後的長度，那rows中就有重複,因為集合會自動剔除重複
            if len(rows) != len(set(rows)):
                return False

            # 如rows
            column = [pos[1] for pos in value]
            if len(column) != len(set(column)):
                return False

            # 將rows 跟 column 的位置都除3後放入block,這樣就可以算出小九宮格的位置是否有重複
            block = [(pos[0] // 3, pos[1] // 3) for pos in value]
            # 一樣如果有重複的，經過set會被剔除
            if len(block) != len(set(block)):
                return False

        return True

            


            