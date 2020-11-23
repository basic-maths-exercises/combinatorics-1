# Generating new sequences

The video and comprehension exercises that you have just completed explained the theory of combinations and permutations.  The proofs in these videos are important as they come up in both statistics and in the pure maths modules.  It is thus really important that you remember all the formulas.  On the plus side, however, if you understand the proofs then remembering the formulas is extremely easy.  Furthermore, these expressions for the number of combinations and the number of permutations come up all over the place so it is worth getting a handle on this material now.  In these programming exercises, we are thus going to do some exercises to consolidate the key ideas in these proofs so as to help you remember how the expressions for the number of permutations and combinations are derived.

We will start with the equations for the number of permutations.  You will remember from the video that one of the steps in the derivation of the number of permutations of `n` distinguishable objects involved generating lists of length `n` from a list of symbols of length `n-1`.  We noted that there are `n` places in the list of length `n-1` where we can insert the `n`th object.  If we have the 3-symbol list `[1,2,3]` and we insert the symbol 4, for instance, we can create the following four sequences:

````
[4,1,2,3]     [1,4,2,3]       [1,2,4,3]       [1,2,3,4]
````

 Your task is to complete the function on the right called `allseq`.  The first argument that is passed to this function `inseq` is a list containing a set of `n-1` distinguishable symbols.  The code should return `final_seq` which is a list of the `n` lists that can be constructed by inserting the symbol in the variable called a in the `n` different positions where it can be inserted in `inseq`.  

If you run this code now you will see that I have got you started by creating the list of `n` lists called `final_seq`.  I have done this by creating a list called `newseq`, which has a length of `n`, within a loop that places the new symbol (a) into the `n` possible locations in the new sequences.  Furthermore, I have placed these new sequences into the list of lists called `final_seq` that the function returns by using the command:

````
final_seq.append( newseq ) 
````

which appends the variable newseq onto the end of the list called `final_seq`.  Your task is thus to simply insert the `n-1` symbols from `inseq` into the `n-1` locations that I have not used in `newseq`.  You can test your code by seeing if the output for inserting 4 into [1,2,3] is as described above.

_In this exercise, I am using python lists rather than NumPy arrays because the output is better.  To create an empty Python list you do:_

````
empty_list = []
````

_You can then create the content of the list by using append as described above.  Alternatively,  the equivalent of `a = np.zeros(n)` for Python lists is:_

````
a = n*[0]
````

_I have used NumPy arrays rather than Python lists in previous exercises because these are better suited for doing mathematical operations._
