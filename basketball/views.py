from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Candidate, VoteRecord, Activity
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from blog.forms import SignupForm
from blog.sql import find_user, update_user, insert_user, find_user_voted_time, update_user_voted_time
from .decorators import custome_login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from django.template import loader
from django.core.paginator import Paginator
import datetime


@csrf_exempt
def vote_index(request):
    candidate_list = Candidate.objects.all().order_by('name')
    candidate_count = candidate_list.count()
    paginator = Paginator(candidate_list, 5)
    if request.method == 'POST':
        data = {}
        page = int(request.POST.get('page'))
        print(page)
        candidate_list = paginator.get_page(page)
        print(paginator.num_pages)

        if candidate_list.has_next():
            data['has_next'] = candidate_list.has_next()
            data['next_page_num'] = candidate_list.next_page_number()
        print(data)
        data['html'] = loader.render_to_string('basketball/lazy_load_candidates.html',
                                               {'candidate_list': candidate_list})
        return JsonResponse(data)
    else:
        activity = get_object_or_404(Activity, slug='basketball')
        activity.increase_views()
        candidate_list = paginator.get_page(1)
        votes_count = VoteRecord.objects.count()

        print(votes_count)
        context = {'candidate_list': candidate_list,
                   'candidate_count': candidate_count,
                   'votes_count': votes_count,
                   'activity': activity}
        return render(request, 'basketball/template.html', context)


@csrf_exempt
def lazy_load_candidates(request):
    if request.method == 'POST':
        data = {}
        page = int(request.POST.get('page', 1))
        print(page)
        candidate_list = Candidate.objects.all()[2:]
        paginator = Paginator(candidate_list, 2)
        candidate_list = paginator.get_page(page)
        print(paginator.num_pages)
        if page > paginator.num_pages:
            data['stop_sign'] = True
            return JsonResponse(data)
        data['html'] = loader.render_to_string('basketball/lazy_load_candidates.html',
                                               {'candidate_list': candidate_list})
        return JsonResponse(data)


@csrf_exempt
def search(request):
    if request.method == 'POST':
        data = {}
        name = request.POST.get('q')
        candidate_list = Candidate.objects.filter(name=name)
        if candidate_list.exists():
            data['result'] = loader.render_to_string('basketball/lazy_load_candidates.html',
                                                     {'candidate_list': candidate_list})
        else:
            data['result'] = '没有搜索结果'
        return JsonResponse(data)


@csrf_exempt
def vote(request, candidate_id):
    if request.method == 'POST':
        current_time = datetime.datetime.now()
        data = {}
        mobile = request.session.get('mobile_auth', None)
        print(mobile)
        voted_time = find_user_voted_time(mobile)
        print(voted_time)
        if current_time - voted_time > datetime.timedelta(days=1):
            candidate = get_object_or_404(Candidate, pk=candidate_id)
            candidate.increase_votes()
            vote_record = VoteRecord(mobile=mobile, candidate=candidate)
            vote_record.save()
            update_user_voted_time(mobile)
            data['success_message'] = "感谢你宝贵的一票"
        else:
            data['error_message'] = '亲，一天只能投一票'
        return JsonResponse(data)


@custome_login_required(login_url='/basketball/vote_login/')
def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    vote_record_list = VoteRecord.objects.filter(candidate=candidate)
    context = {'candidate': candidate,
               'vote_record_list': vote_record_list}
    return render(request, 'basketball/template_detail.html', context)


def vote_login(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request=request)
        if form.is_valid():
            try:
                del request.session['verify_code']
            except KeyError:
                pass
            dealer_id = request.session.get('dealer_id', None)
            phone = form.cleaned_data['phone']
            row = find_user(phone)
            if row:
                if dealer_id is not None:
                    update_user(phone, dealer_id)
            else:
                insert_user(phone, dealer_id)
            request.session['mobile_auth'] = phone
            redirect_to = request.POST.get(
                'next',
                request.GET.get('next', '')
            )
            print(redirect_to)
            return HttpResponseRedirect(redirect_to)

    else:
        dealer_id = request.GET.get('dealer', None)
        request.session['dealer_id'] = dealer_id
        form = SignupForm()

    return render(request, 'basketball/vote_login.html', {'form': form})