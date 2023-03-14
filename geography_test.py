import random
with open('stolice.txt','r') as f:
    country_and_capital=f.readlines()
    f.close()

students=int(input('Enter the number of students: '))
questions=int(input('Enter the number of questions on the test: '))

letters=['A','B','C','D']

for i in range(students):
    with open('test_'+str(i+1)+'.txt','w+') as f:
        f.write('Enter name: \n\n')

        with open('test_'+str(i+1)+'_answers.txt', 'w+') as f1:
            f1.write('Test answers: \n\n')
            
            for j in range(questions):
                country=random.choice(country_and_capital)
                capital=country.split(', ')[1].strip()
                f.write(country.split(', ')[0]+' has a capital: \n')

                
                answers=random.sample(country_and_capital, 3)
                answers=[x.split(', ')[1].strip() for x in answers]
                answers.append(capital)
                answers=list(set(answers))
                
                answer=[]
                answer=random.sample(answers, 4)
                
                for k in range(4):
                    f.write(letters[k]+') '+answer[k]+'\n')
                f1.write(str(j+1)+letters[answer.index(capital)]+'\n')
                country=None
            f1.close()
        f.close()

print('Tests generated successfully.')
