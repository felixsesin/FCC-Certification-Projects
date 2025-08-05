# Solution to 'Build An Arithmetic Formatter Project' #

# INSTRUCTIONS: Students in primary school often arrange arithmetic problems vertically to make them easier to solve. [...] Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed. #

# MORE INFO:https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project #



def arithmetic_arranger(problems, show_answers=False):
    # too many problem error
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # set up four lines
    ones = []
    twos = []
    threes = []
    fours = []

    for prob in problems:
        # split problems into parts
        part = prob.split()

        # error check parts of problems
        for n in part[0]+part[2]:
            if not n.isdigit():
                return 'Error: Numbers must only contain digits.'
        if len(part[0]) > 4 or len(part[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not part[1] in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # get parts of arithmetic problems
        a = int(part[0])
        x = part[1]
        b = int(part[2])
        c = None
        if x == '+':
            c = a + b
        elif x == '-':
            c = a - b
        
        # format problem lines and spacing
        width = 2 + max(len(part[0]), len(part[2]))
        ones.append( ' '*(width-len(part[0])) + part[0])
        twos.append( x + ' '*(width-len(part[2])-1) + part[2])
        threes.append('-' * width)
        fours.append( ' '*(width-len(str(c))) + str(c))

    # return joined lines
    if show_answers:
        return ('    '.join(ones)) + '\n' + ('    '.join(twos)) + '\n' + ('    '.join(threes)) + '\n' + ('    '.join(fours))

    elif not show_answers:
        return ('    '.join(ones)) + '\n' + ('    '.join(twos)) + '\n' + ('    '.join(threes))