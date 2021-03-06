# Javier Perez 10/01/2020
# This program finds the first, 7 (or n) digit, prime, palindromic number in the digits of Pi
# Written in Python3 v3.8.1
# Code Challenge 1


def main():
    #read in pi as a string
    f = open("1-Million-Digits-of-Pi-π.txt", "r")
    pi_string = f.read()

    i = 2 #skip past "3." of pi, for while loop
    num_of_digits = 7 #can change
    found_answer = False #becomes True when ans is found
    pi_substring = "" #passed into funcs for readability 

    #loop breaks if length of pi is exceeded or if the answer is found
    while((i < (len(pi_string) - num_of_digits)) and (found_answer == False)):

        #substring of size num_of_digits, based on i
        pi_substring = pi_string[i : (i + num_of_digits)]

        #if a substring is palindromic and a prime number, ans is found
        if( is_palindromic(pi_substring) and is_prime(int(pi_substring)) ):
            found_answer = True 

        i += 1 #end of while
    
    if(found_answer):
        print("The first, " + str(num_of_digits) + " digit, prime, palindromic number in the digits of Pi is " + pi_substring)
    else:
        print("Could not find a " + str(num_of_digits) + " digit, prime, palindromic number in the digits of Pi")


# reverse a string and compares 
def is_palindromic(string):
    if(string == string[::-1]):
        return True
    else:
        return False


#first 2 ifs aren't needed,
#for this challenge
def is_prime(num):
    #1 and 0 are not prime
    if(num <= 1):
        return False
    #2 is prime
    if(num == 2):
        return True
    #filters out even numbers, not primes
    if((num % 2) == 0):
        return False

    #only need to go up to half the num
    # +1, because we have odd nums only
    half_num = int(num // 2) + 1

    #look for num that it is divisible by
    #checks only odd numbers
    for index in range(3, half_num, 2):
        if((num % index) == 0):
            return False
    return True   


if __name__ == "__main__":
    main()