# spiral traversal of matrix
def spiral_traversal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # rows
    top = 0
    bottom = rows-1
    # cols
    left = 0
    right = cols-1
    # 0 right 1 down, 2 left, 3 up
    direction = 0
    ans = []
    while(left <= right and top <= bottom):
        if(direction % 4 == 0):
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1
            # direction+=1
        elif(direction % 4 == 1):
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            # direction += 1
        elif(direction % 4 == 2):
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            # direction+=1
        elif(direction % 4 == 3):
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left += 1
            # direction+=1
        else:
            print('Some Error')
        direction += 1
    return ans
