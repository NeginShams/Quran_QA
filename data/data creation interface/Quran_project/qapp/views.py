from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import QuestionData, FactoidQuestion, NonFactoidQuestion, FactoidDone, AutomaticQuestion, MultipleAutomatic, QUQAComplete, QUQA, QaraatiFirst, QaraatiSecond, QaraatiThird, RuleBased

# Create your views here.

def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')

def first_run(request):
    with open('C:/Users/Partiran/django_project/Quran_project/qapp/nonfactoid.jsonl', 'r',encoding="utf8") as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        data = QuestionData()
        data.context = result['context']
        data.question = result['question']
        data.answer = result['answers']
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("Questions saved in database")


def save_factoid_questions(request):
    with open('C:/Users/Partiran/django_project/Quran_project/qapp/translated_factoid_undone.jsonl', 'r',encoding="utf8") as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        data = FactoidQuestion()
        data.context = result['context']
        data.question = result['question']
        data.answer = result['answers']
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("Factoid Questions saved in database")

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def dump_jsonl(data, output_path, append=False):
    """
    Write list of objects to a JSON lines file.
    """
    mode = 'a+' if append else 'w'
    with open(output_path, mode, encoding='utf-8') as f:
        for line in data:
            json_record = json.dumps(line, ensure_ascii=False)
            f.write(json_record + '\n')
    print('Wrote {} records to {}'.format(len(data), output_path))


def create_dataset(request):
    data_list = FactoidQuestion.objects.all()

    dict_data_list = []

    for data in data_list:
        result = {}
        result['context'] = data.context
        result['question'] = data.question
        result['answers'] = data.answer
        result['pq_id'] = data.pq_id
        dict_data_list.append(result)
    
    output_path = 'C:/Users/Partiran/django_project/Quran_project/qapp/farsi_factoid_v2.jsonl'
    dump_jsonl(dict_data_list, output_path)

    return HttpResponse("Dataset created successfully")

def save_nonfactoid_questions(request):
    with open('C:/Users/Partiran/django_project/Quran_project/qapp/translated_nonfactoid_2.jsonl', 'r',encoding="utf8") as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        data = NonFactoidQuestion()
        data.context = result['context']
        data.question = result['question']
        data.answer = result['answers']
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("NonFactoid Questions successfully saved in database")

def save_factoid_done(request):
    with open('C:/Users/Partiran/django_project/Quran_project/qapp/translated_factoid_done.jsonl', 'r',encoding="utf8") as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        data = FactoidDone()
        data.context = result['context']
        data.question = result['question']
        data.answer = result['answers']
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("Factoid Done Questions successfully saved in database")

def save_quqa_done(request):
    # C:\Users\Partiran\Desktop\Quran_project\qapp\data\QUQA_translated
    with open('C:/Users/Partiran/Desktop/Quran_project/qapp/data/QUQA_translated/QUQA_complete.jsonl' , 'r', encoding="utf8") as f:
        json_list = list(f)
    
    for json_str in json_list:
        result = json.loads(json_str)
        data = QUQAComplete()
        data.context = result['context']
        data.question = result['question']
        data.answer = result['answer']
        data.pq_id = result['pq_id']
        data.save()
    
    return HttpResponse("QUQA Complete Questions successfully saved in database")

def save_quqa(request):
    with open('C:/Users/Partiran/Desktop/Quran_project/qapp/data/QUQA_translated/QUQA_not_complete.jsonl' , 'r', encoding="utf8") as f:
        json_list = list(f)
    
    for json_str in json_list:
        result = json.loads(json_str)
        data = QUQA()
        data.context = result['context']
        data.question = result['question']
        data.answer = result['answer']
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("QUQA not Complete Questions successfully saved in database")

def save_qaraatiFirst(request):
    with open('C:/Users/Partiran/Desktop/Quran_project/qapp/data/Qaraati/Qaraati_part1.json' , 'r', encoding="utf_8_sig") as f:
        json_list = json.load(f)
    
    for result in json_list:
        # result = json.loads(json_str)
        data = QaraatiFirst()
        data.context = result['verse_content']
        data.question = result['question']
        answer_str = ''

        for answer in result['answers']:
            answer_str += answer
            answer_str += '_'

        data.answer = answer_str
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("QaraatiFirst Questions successfully saved in database")

def save_qaraatiSecond(request):
    with open('C:/Users/Partiran/Desktop/Quran_project/qapp/data/Qaraati/Qaraati_part2.json' , 'r', encoding="utf_8_sig") as f:
        json_list = json.load(f)
    
    for result in json_list:
        # result = json.loads(json_str)
        data = QaraatiSecond()
        data.context = result['verse_content']
        data.question = result['question']
        answer_str = ''

        for answer in result['answers']:
            answer_str += answer
            answer_str += '_'

        data.answer = answer_str
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("QaraatiSecond Questions successfully saved in database")

def save_rule_based(request):
    with open('C:/Users/Partiran/Desktop/Quran_project/qapp/data/rule_based.json' , 'r', encoding="utf_8_sig") as f:
        json_list = json.load(f)
    
    for result in json_list:
        # result = json.loads(json_str)
        data = RuleBased()
        data.context = result['context']
        data.question = result['question']
        data.answer = result['answer']
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("RuleBased Questions successfully saved in database")

def save_qaraatiThird(request):
    with open('C:/Users/Partiran/Desktop/Quran_project/qapp/data/Qaraati/Qaraati_part3.json' , 'r', encoding="utf_8_sig") as f:
        json_list = json.load(f)
    
    for result in json_list:
        # result = json.loads(json_str)
        data = QaraatiThird()
        data.context = result['verse_content']
        data.question = result['question']
        answer_str = ''

        for answer in result['answers']:
            answer_str += answer
            answer_str += '_'

        data.answer = answer_str
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("QaraatiThird Questions successfully saved in database")

def save_automatic_questions(request):
    with open('C:/Users/Partiran/Desktop/Quran_project/qapp/automatic_data.jsonl', 'r',encoding="utf8") as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        data = AutomaticQuestion()
        data.context = result['context']
        data.question = result['question']
        data.answer = result['answers'][0]['text']
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("Automatic Questions successfully saved in database")

def save_multiple_automatic(request):
    with open('C:/Users/Partiran/Desktop/Quran_project/qapp/automatic_multiple_occurence.jsonl', 'r',encoding="utf8") as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        data = MultipleAutomatic()
        data.context = result['context']
        data.question = result['question']
        data.answer = result['answers']
        data.pq_id = result['pq_id']
        data.save()

    return HttpResponse("Automatic Multiple Questions successfully saved in database")

def delete_bad_questions(request):
    # AutomaticQuestion.objects.filter(answer='زید').delete()
    # AutomaticQuestion.objects.filter(answer='نان').delete()
    # AutomaticQuestion.objects.filter(answer='سیر').delete()

    MultipleAutomatic.objects.filter(answer='زید').delete()
    MultipleAutomatic.objects.filter(answer='نان').delete()
    MultipleAutomatic.objects.filter(answer='سیر').delete()
    MultipleAutomatic.objects.filter(answer="").delete()

    return HttpResponse("Wrong Questions Deleted successfully")

# def delete_everything(self):
#     MultipleAutomatic.objects.all().delete()
#     return HttpResponse("All Questions Deleted successfully")

def mt5_questions(request):
    all_questions = AutomaticQuestion.objects.all()
    all_multiple = MultipleAutomatic.objects.all()

    good_questions = []
    mild_questions = []
    bad_questions = []
    unknown = []

    for q in all_questions:
        if q.score == '3' and q.id:
            good_questions.append(q)
        elif q.score == '2':
            mild_questions.append(q)
        elif q.score == '1':
            bad_questions.append(q)
        else:
            unknown.append(q)

    for m in all_multiple:
        if m.score == '3' and q.id:
            good_questions.append(m)
        elif m.score == '2':
            mild_questions.append(m)
        elif m.score == '1':
            bad_questions.append(m)
        else:
            unknown.append(m)

    print(len(good_questions))
    print(len(mild_questions))
    print(len(bad_questions))
    print(len(unknown))

    dict_data_list = []
    my_questions = good_questions + mild_questions

    for question in my_questions:
        new_data = {}
        new_data['pq_id'] = question.pq_id
        new_data['question'] = question.question
        answers_list = []
        answer_dict = {}
        if question.context.count(question.answer) == 1:
            new_data['context'] = question.context
            answer_dict['text'] = question.answer
            answer_dict['start_char'] = question.context.find(question.answer)
        elif question.context.count(question.answer) > 1 and "*" in question.context:
            markers = findOccurrences(question.context, '*')
            answer_dict['text'] = question.answer
            answer_dict['start_char'] = markers[0]
            new_data['context'] = question.context.replace('*', '')
            
        answers_list.append(answer_dict)
        new_data['answers'] = answers_list
        dict_data_list.append(new_data)

    
    output_path = 'C:/Users/Partiran/Desktop/Quran_project/qapp/data/automatic.jsonl'
    dump_jsonl(dict_data_list, output_path)

    print('ok')

    return HttpResponse("check cmd")

# def hanldle_unknown_questions(request):
#     scores = ['1', '2', '3']
#     all_questions = AutomaticQuestion.objects.all()

#     for q in all_questions:
#         if q.score not in scores:
#             print(q)
#     return HttpResponse("check cmd")


def temp_dataset(request):
    data_list = FactoidQuestion.objects.all()
    data_list2 = FactoidDone.objects.all()
    data_list3 = NonFactoidQuestion.objects.all()
    data_list4 = AutomaticQuestion.objects.all()
    data_list5 = MultipleAutomatic.objects.all()
    data_list6 = QUQAComplete.objects.all()
    data_list7 = QUQA.objects.all()
    data_list8 = QaraatiFirst.objects.all()
    data_list9 = QaraatiSecond.objects.all()
    data_list10 = QaraatiThird.objects.all()
    data_list11 = RuleBased.objects.all()

    dict_data_list = []

    for data in data_list:
        if data.answer != 'امرأت فرعون':
            result = {}
            result['context'] = data.context
            result['question'] = data.question
            result['answers'] = data.answer
            result['pq_id'] = data.pq_id
            dict_data_list.append(result)

    for data in data_list2:
        result = {}
        result['context'] = data.context
        result['question'] = data.question
        result['answers'] = data.answer
        result['pq_id'] = data.pq_id
        dict_data_list.append(result)

    for data in data_list3:
        if data.question and not data.answer:
            print('EXCEPTION!')
        if not data.question and data.answer:
            print('EXCEPTION!!!')

        if data.question and data.answer:
            result = {}
            result['context'] = data.context
            result['question'] = data.question
            result['answers'] = data.answer
            result['pq_id'] = data.pq_id
            dict_data_list.append(result)


    good_questions = []
    mild_questions = []
    bad_questions = []

    for q in data_list4:
        if q.score == '3' and q.id:
            good_questions.append(q)
        elif q.score == '2':
            mild_questions.append(q)
        elif q.score == '1':
            bad_questions.append(q)

    for q in data_list5:
        if q.score == '3' and q.id:
            good_questions.append(q)
        elif q.score == '2':
            mild_questions.append(q)
        elif q.score == '1':
            bad_questions.append(q)
    
    my_questions = good_questions + mild_questions

    for question in my_questions:
        new_data = {}
        new_data['pq_id'] = question.pq_id
        new_data['question'] = question.question
        # answers_list = []
        # answer_dict = {}
        # if question.context.count(question.answer) == 1:
        #     new_data['context'] = question.context
        #     answer_dict['text'] = question.answer
        #     answer_dict['start_char'] = question.context.find(question.answer)
        # elif question.context.count(question.answer) > 1 and "*" in question.context:
        #     markers = findOccurrences(question.context, '*')
        #     answer_dict['text'] = question.answer
        #     answer_dict['start_char'] = markers[0]
        #     new_data['context'] = question.context.replace('*', '')
            
        # answers_list.append(answer_dict)
        # new_data['answers'] = answers_list

        new_data['context'] = question.context
        new_data['answers'] = question.answer

        dict_data_list.append(new_data)

    for data in data_list6:
        if data.question and not data.answer:
            print('EXCEPTION!')
        if not data.question and data.answer:
            print('EXCEPTION!!!')

        if data.question and data.answer:
            result = {}
            result['context'] = data.context
            result['question'] = data.question
            result['answers'] = data.answer
            result['pq_id'] = data.pq_id
            dict_data_list.append(result)

    for data in data_list7:
        if data.question and not data.answer:
            print('EXCEPTION!')
        if not data.question and data.answer:
            print('EXCEPTION!!!')

        if data.question and data.answer:
            result = {}
            result['context'] = data.context
            result['question'] = data.question
            result['answers'] = data.answer
            result['pq_id'] = data.pq_id
            dict_data_list.append(result)

    for data in data_list8:
        if data.question and not data.answer:
            print('EXCEPTION!')
        if not data.question and data.answer:
            print('EXCEPTION!!!')

        if data.question and data.answer:
            result = {}
            result['context'] = data.context
            result['question'] = data.question
            result['answers'] = data.answer
            result['pq_id'] = data.pq_id
            dict_data_list.append(result)

    for data in data_list9:
        if data.question and not data.answer:
            print('EXCEPTION!')
        if not data.question and data.answer:
            print('EXCEPTION!!!')

        if data.question and data.answer:
            result = {}
            result['context'] = data.context
            result['question'] = data.question
            result['answers'] = data.answer
            result['pq_id'] = data.pq_id
            dict_data_list.append(result)

    for data in data_list10:
        if data.question and not data.answer:
            print('EXCEPTION!')
        if not data.question and data.answer:
            print('EXCEPTION!!!')

        if data.question and data.answer:
            result = {}
            result['context'] = data.context
            result['question'] = data.question
            result['answers'] = data.answer
            result['pq_id'] = data.pq_id
            dict_data_list.append(result)

    for data in data_list11:
        if data.question and not data.answer:
            print('EXCEPTION!')
        if not data.question and data.answer:
            print('EXCEPTION!!!')

        if data.question and data.answer:
            result = {}
            result['context'] = data.context
            result['question'] = data.question
            result['answers'] = data.answer
            result['pq_id'] = data.pq_id
            dict_data_list.append(result)

    output_path = 'C:/Users/Partiran/Desktop/Quran_project/qapp/data/total_temp.jsonl'
    dump_jsonl(dict_data_list, output_path)

    return HttpResponse("Dataset created successfully")