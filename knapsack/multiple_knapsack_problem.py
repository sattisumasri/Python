# Python3 code for the extended
# Knapsack Approach

# To store the dp values
dp=[]

def maxProfit(profit, weight, n, max_W,
			max_E):

	# for each element given
	for i in range(1,n+1) :

		# For each possible
		# weight value
		for j in range(1,max_W+1) :

			# For each case where
			# the total elements are
			# less than the constra
			for k in range(1, max_E+1) :

				# To ensure that we dont
				# go out of the array
				if (j >= weight[i - 1]) :

					dp[i][j][k] = max(
						dp[i - 1][j][k],
						dp[i - 1][j - weight[i - 1]][k - 1]
							+ profit[i - 1])
				
				else :
					dp[i][j][k] = dp[i - 1][j][k]


	return dp[n][max_W][max_E]


# Driver Code
if __name__ == '__main__':
	n = 5
	profit = [2, 7, 1, 5, 3 ]
	weight = [ 2, 5, 2, 3, 4 ]
	max_weight = 8
	max_element = 2

	dp = [[[0 for j in range(max_element + 1)]for i in range(max_weight + 1)] for k in range(n+1)]
	print(maxProfit(profit, weight, n, max_weight,
					max_element))
