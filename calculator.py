def calc(exam):
    err_exam_1 = [',','?','!',';',':','&','@','#','$','%','^','=']
    err_exam_3 = ['+(','-(','*(','/(','-','*','/']
    err_exam_4 = [')+',')-',')*',')/','+','-' ,'*','/']
    err_exam_5 = ['(+','(-','(*','(/','+)','-)','*)','/)','++','+-','+*','+/','-+','--','-*','-/','*+','*-','**',
                '*/','/+','/-','/*','//']
#    err_exam_6
    mess_1 = "You entered invalid symbols"
    mess_2 = "You entered alphabetic symbols"
    mess_3 = "Number is missing at the start of line"
    mess_4 = "Number is missing at the end of line"
    mess_5 = "Number is missing"

    exam_list = exam.split(' ')
    str_beg = exam_list[0]
    str_end = exam_list[-1]

    if list(set(exam_list)&set(err_exam_1)):
        return mess_1
    elif [a_b for a_b in exam_list if a_b.isalpha()]:
        return mess_2
    elif [s for s in err_exam_3 if str_beg == s]:
        return mess_3
    elif [w for w in err_exam_4 if str_end == w]:
        return mess_4
    elif list(set(exam_list)&set(err_exam_5)):
        return mess_5
    else:
        return eval(exam)