from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalcIncomeForm
# Create your views here.

def index(request):
    params = {
        'title':'Think monney',
        'forms': CalcIncomeForm(),
        'answer':'あなたの総支給を教えてくれ、手取りを教えてやろう',
        'message': '金額によって伝えたいことがある',
        'name':''
    }
    
    if request.method == 'POST' and  int(request.POST['monney']) <=550999:
        k =int((request.POST['monney']))
        k=round(k)
        params['answer'] = 'あなたの手取りは' + str(k) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = '財布が軽ければ心が重い'
        params['name'] = 'ヨハン・ヴォルフガング・フォン・ゲーテ'
    
    elif request.method == 'POST' and 551000 <= int(request.POST['monney']) <=1618999:
        j = int(request.POST['monney'])-55000
        j=round(j)
        params['answer'] = 'あなたの手取りは' + str(j) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = '若いときの自分は、金こそ人生でもっとも大切な物だと思っていた。今、歳をとってみると、その通りだと知った。'
        params['name'] = 'オスカー・ワイルド'
    
    elif request.method == 'POST' and 1619000 <= int(request.POST['monney']) <=1619999:
        i = 1069000
        params['answer'] = 'あなたの手取りは' + str(i) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = '人生に必要なもの。それは勇気と想像力、そして少しのお金だ。'
        params['name'] = 'チャールズ・スペンサー・チャップリン・ジュニア'
    
    elif request.method == 'POST' and 1620000 <= int(request.POST['monney']) <=1621999:
        h = 1070000
        params['answer'] = 'あなたの手取りは' + str(h) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = '幸福はお金では買えないと言った人々は、どこで買えばいいか知らなかったのだ。'
        params['name'] = 'ガートルード・スタイン'
    
    elif request.method == 'POST' and 1622000 <= int(request.POST['monney']) <=1623999:
        g = 1072000
        params['answer'] = 'あなたの手取りは' + str(g) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = 'あなたが欲しいと思うものを買ってはいけない。あなたが必要とするものを買うようにしなさい。'
        params['name'] = 'カトー'

    
    elif request.method == 'POST' and 1624000 <= int(request.POST['monney']) <=1627999:
        f = 1074000
        params['answer'] = 'あなたの手取りは' + str(f) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = '幸福はお金では買えないと言った人々は、どこで買えばいいか知らなかったのだ。'
        params['name'] = 'ガートルード・スタイン'

    
    elif request.method == 'POST' and 1628000 <= int(request.POST['monney']) <=1799999:
        e = int(request.POST['monney'])*0.6+100000
        e=round(e)
        params['answer'] = 'あなたの手取りは' + str(e) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = '富は宝を所有することではなく、それを使用するところにある。'
        params['name'] = 'ナポレオン・ボナパルト'

    
    elif request.method == 'POST' and 1800000 <= int(request.POST['monney']) <= 3599999:
        d = int(request.POST['monney'])*0.7-80000
        d=round(d)
        params['answer'] = 'あなたの手取りは' + str(d) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = '人間よりは金のほうがはるかに頼りになりますよ。頼りにならんのは人の心です。'
        params['name'] = '尾崎紅葉'

    
    elif request.method == 'POST' and 3600000 <= int(request.POST['monney']) <=6599999:
        c = int(request.POST['monney'])*0.8-440000
        c=round(c)
        params['answer'] = 'あなたの手取りは' + str(c) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = '余生を過ごせるだけの金は持っているよ。ただし、何も買わなければだが。'
        params['name'] = 'ジャッキー・メーソ'

    
    elif request.method == 'POST' and 6600000 <= int(request.POST['monney']) <=8499999:
        b = int(request.POST['monney'])*0.9-1100000
        b=round(b)
        params['answer'] = 'あなたの手取りは' + str(b) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = '富は海の水に似ている。それを飲めば飲むほど、のどが渇いてくる。'
        params['name'] = 'アルトゥル・ショーペンハウアー'

    

    elif request.method == 'POST' and int(request.POST['monney']) >= 8500000:
        a = int(request.POST['monney'])-1950000
        a=round(a)
        params['answer'] = 'あなたの手取りは' + str(a) + '円だ。'
        params['forms'] = CalcIncomeForm(request.POST)
        params['message'] = 'つまらぬ財産を持つより、立派な希望を持つほうがマシだ。'
        params['name'] = 'ミゲル・デ・セルバンテス'


    return render(request, 'calcincome/index.html', params)

    

    

    


    


    
    
