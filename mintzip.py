import re
import parser


def evaluate_exp():
    '''This function will parse the Algebraic Expression and Evalute that
	Sample input :-
            Enter Expression : A * (C / E) + B / (F + D)
            Enter value A : 23
            Enter value B : 200
            Enter value C : 234
            Enter value D : 1.34
            Enter value E : 22.45
            Enter value F : 23
        Sample Output :-
            Evaluated Ans :  247.94966629
            Want to Execute more (Y/N) : n
            Bye Bye
    '''
    print evaluate_exp.__doc__
    while True:
        input_st = raw_input("Enter Expression : ")
        st = parser.expr(input_st)

        variables = sorted(set(filter(None, re.split("[^a-zA-Z]*", input_st))))

        for vv in variables:
            in_v = input("Enter value %s : " % vv)
            exec("%s = %f" % (vv, in_v))
        code = st.compile()
        print "Evaluated Ans : ", eval(code)
        m = raw_input("Want to Execute more (Y/N) : ")
        if m == 'Y' or m == 'y':
            continue
        else:
            print "Bye Bye"
            break

evaluate_exp()
