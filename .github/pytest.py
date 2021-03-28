def masgen(my_filename, fext2,n):
    
    def __init__(self):
        self.field = [ list('.')*10 for _ in range(10) ]
   
    def shoot(self, row, col, result):
        
        def correct(x):
            if x<0 :
                x = 0
            elif x>9:
                x = 9
            return x
            
        if result == 'sink':
            line_row = [correct(x) for x in (row-1,row,row+1)]
            line_col = [correct(x) for x in (col-1,col,col+1)]
            
            for i in line_row:
                for x in line_col:
                    self.field[i][x] = '*'
            self.field[row][col] = 'x'
        elif result == 'miss':
            self.field[row][col] = '*'
        else:   
            self.field[row][col] = 'x'
 
    def cell(self, row, col):
        return self.field[row][col]