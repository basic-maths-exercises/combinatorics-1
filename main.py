def allseq( inseq, a ) : 
  final_seq = [] 
  n = len(inseq)+1
  for i in range(n) : 
    newseq = n*[0] 
    newseq[i] = a 
    # Your code to insert the remainder of the symbols into the list called newseq
    # goes here
  
    final_seq.append( newseq )
  
  return final_seq
  

# This tests the code that you have written by printing out the sequences that 
# you have generated as discussed in the description on the right
print( allseq( [1,2,3], 4 ) )
