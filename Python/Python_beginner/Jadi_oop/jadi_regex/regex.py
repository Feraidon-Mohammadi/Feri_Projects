import re
# library RegularExpression


"""

    .       ->dot in regex that mean everything
    [abc]   -> a or b or c
    [A-Z]   -> from A to Z 
    \d      -> digit
    \w      -> word - aplhabet
    \s      -> whitspace    r"\s....\s
    *       -> many 0 - 999...    example if want to know how many A i have in text  =>  A*   from 0 start   if a exist take it if no than nothing
    +       -> 1 to 999...         example if want to know how many A i have in text  => A+   from 1 start    minimum 1 A
    ()      -> add in to a group
    4{n}    -> 4 times n     z.b  {N,M} -> from N ta M   minimum n and maximum M
    [^ABC]  -> everything without ABC =>                 []  -> all what dont want  put inside braket


    ^       -> start of sentence  # exampl  ^1  start from 1
    $       -> end of sentence
        from x to z forexample
    [^\d]   -> start with digit  -> number i mean
    ?       -> lazy  or slower effect regex or greedy regex



    \t      -> tabe
    \n      -> new line or begining of sentences
    \r      -> return


"""
a = ".*$" # . everything and * everymuch to $end of the existing
x = r" @(.*)\.   "

"""

r"^email:(.\*)$          
exampl = email:jadijadi@gmail.com

#get phone number 
r"^phone:(\d{11})$  #give me the phone numbers which are digits and have a length of 11 and after 11 finished



greedy regex :
r" this .*? end     -> because of special charachter -> ?       it take first part from this to end and second this to end  
this ist the end of line . and this is the 2nd end 

rfc5322 for email regex 



#a complex regex
r" ^(\w+)\.*(\w*)\.(w+)
amir.jadi.mirmirani
ali.rezayi



"""
def regexs():

    x = 'Salam jadi. salam feri. Salam Mori'

    return x
f = regexs()
print(f)

result = re.search(r'Salam',str)



print(result)




































