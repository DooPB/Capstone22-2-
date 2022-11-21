from django.shortcuts import render, redirect
from .models import CoinBoard
from .forms import BoardAdd
from django.urls import reverse
# Create your views here.

def board_list(request):
    boardlist = CoinBoard.objects.order_by('-write_time')
    context = {'boardlist':boardlist}
    return render(request,'board/board_list.html',context=context)

def board_view(request, board_id):
    board_detail = CoinBoard.objects.get(id=board_id)
    context = {'board_detail':board_detail}
    return render(request,'board/board_view.html',context=context)

def board_add(request):
    if request.method == 'POST':
        boardform = BoardAdd(request.POST)
        if boardform.is_valid():
            boardform.save()
            return redirect(reverse('board:list'))
    else:
        boardform = BoardAdd()
    return render(request,'board/board_add.html',context={'boardform':boardform})
