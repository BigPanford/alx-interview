Explanation:
The function first checks if n is less than or equal to 0 and returns an empty list in that case.
It initializes the triangle with the first row [[1]].
Then, for each subsequent row, it starts with [1], calculates the intermediate values using the sum of the two elements directly above from the previous row, and ends with 1.
The resulting triangle is built iteratively and returned as a list of lists.



Example Output for n = 5:


[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
