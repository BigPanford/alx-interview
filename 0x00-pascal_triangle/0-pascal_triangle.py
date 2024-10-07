def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Starting with the first row
    
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # Every row starts with a 1
        # Generate the values of the row based on the previous row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Every row ends with a 1
        triangle.append(row)
    
    return triangle

# Example usage:
n = 5
print(pascal_triangle(n))
