import random

#DKT_FILENAME = 'driving-knowledge-test-questions-car.txt'
DKT_FILENAME = 'proc2.txt'
print DKT_FILENAME

# CLASS DEFINITION
class Exam:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices
        self.answer = choices[0]

    def __str__(self):
        random.shuffle(self.choices)
        return "Question: {0}\n\t1.{1}\n\t2.{2}\n\t3.{3}".format(self.question, self.choices[0]
                                                                        , self.choices[1]
                                                                        , self.choices[2])

listExams = []
quesCounter = 0
choices = []
question = ''

# FILE OPEN
with open(DKT_FILENAME, 'r') as f:
    line = None
    while (line != ''):
        line = f.readline();
        if (line == '\n'): continue
        line = line.strip()

        # found = line.find('particular')
        # print ('found =' + str(found))
        #
        #
        # if (found != -1):
        #     print 'weh = ' + line[-1] + line

        try:
            if line[-1] == '?' or line[-1] == '-':
                question = line
                quesCounter+=1
                choices = [] #clear choices

                print 'Question #{}:{}'.format(quesCounter, question)
            else:

                choices.append(line)
                #print (line)
                if (len(choices)== 3 and question != ''):
                    #print ('Adding Question:{} with choices {}'.format(question, choices))
                    ExamItem = Exam(question, choices)
                    listExams.append(ExamItem)
                    choices = []
                    question = '' #reset question field

        except:
            pass
f.closed
# FILE CLOSE

print 'ques counter= '+str(quesCounter)

# Local functions
def show_exam():
    random.shuffle(listExams)
    for i in range(0,45):
        exam = listExams[i]
        print exam
        ans = raw_input()
        index = int(ans)
        if(exam.answer == exam.choices[index-1]):
            print "Answer is correct"
        else:
            print "Answer is wrong, correct answer is " + exam.answer

def take_exam():
    opt = ''
    while(opt != '1' or  opt != '2'):
        print 'Welcome to NSW DKT Exam'
        print '[1] Start exam'
        print '[2] Exit program'
        opt = raw_input()
        if opt == '1':
            show_exam()
        elif opt == '2':
            exit()
        else:
            print 'Invalid input'
            raw_input()


if __name__ == '__main__':
    take_exam()






