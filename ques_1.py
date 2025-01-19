"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 1a

def calc_prob(alice_wins, bob_wins):
    #solved using dynamic programming
    
    dp=[[0]*(max(bob_wins+1,3)) for i in range(max(alice_wins+1,3))]#created dp array
    #dp[a][b] represents the probability of making a wins and b loses in a+b matches for Alice
    dp[1][1]=1#first two games'result is already given as 1 win and 1 loss
    dp[2][1]=mod_divide(1, 2)#probability of 2 wins and 1 loss for Alice
    dp[1][2]=mod_divide(1, 2)#probability of 1 win and 2 losses for Alice

    for i in range(3,alice_wins+1):#setting up probabilities for 1 loss and number of wins ranging from 3 to total we need
        mod_divide(dp[i-1][1],i)
        dp[i][1]=mod_divide(dp[i-1][1],i)

    for i in range(3,bob_wins+1):    #setting up probabilities for 1 win and number of losses ranging from 3 to total we need    
        dp[1][i]=mod_divide(dp[1][i-1],i)

    for i in range(2,bob_wins+1):#using the base cases we found above ,all other cases required to finally find req. no. of wins and losses is done
        for j in range(2,alice_wins+1):
             dp[j][i]=mod_add(mod_multiply(dp[j][i-1],mod_divide(j,j+i-1)),mod_multiply(dp[j-1][i],mod_divide(i,j+i-1)))            
            
    return (dp[alice_wins][bob_wins])

#print(calc_prob(97,34))
#590987433

# Problem 1b (Expectation)      

def calc_expectation(t):
    result=0
    for i in range(1,t):#iterating through all possible wins=i , so losses=t-i,wins-losses=i-(t-i)=2*i-t
        y=mod_add(mod_multiply(2,i),-t)
        result=mod_add(result,mod_multiply(y,calc_prob(i,t-i)))

    return (result) 

#print(calc_expectation(34))
#0

# Problem 1b (Variance)
def calc_variance(t):
    result=0
    for i in range(1,t):#iterating through all possible wins=i , so losses=t-i,wins-losses=i-(t-i)=2*i-t
        y=mod_add(mod_multiply(2,i),-t)
        y=mod_multiply(y,y)
        result=mod_add(result,mod_multiply(y,calc_prob(i,t-i)))

    return (result) 

#print(calc_variance(34))
#333333347
    
  

    
