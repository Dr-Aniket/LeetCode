class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def valid_coord(coord):
            if len(coord) != 2:
                return False
            elif coord[0] not in 'abcdefgh':
                return False
            elif coord[1] not in '12345678':
                return False
            
            return True

        if not valid_coord(coordinate1):
            return False
        elif not valid_coord(coordinate2):
            return False
        
        def get_sq_color(coord):
            i,j = '.abcdefgh'.index(coord[0]), int(coord[1])

            if (i+j)%2 == 0:
                return 'b'
            else:
                return 'w'
        
        return get_sq_color(coordinate1) == get_sq_color(coordinate2)

