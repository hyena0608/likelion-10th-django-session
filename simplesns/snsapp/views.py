from django.shortcuts import render

def home(request):
    # Board 넘겨주기
    
    # 페이지네이션
    
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

# def create(request):

def detail(request, board_id):
    # Board 넘겨주기
    
    # Comment 넘겨주기
    
    return render(request, 'detail.html')

# def create_comment(request, board_id):