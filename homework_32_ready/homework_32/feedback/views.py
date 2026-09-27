from django.shortcuts import redirect, render

from .forms import FeedbackForm
from .models import Feedback


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            Feedback.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect('success')
    else:
        form = FeedbackForm()

    return render(
        request,
        'feedback/form.html',
        {'form': form}
    )


def success(request):
    return render(
        request,
        'feedback/success.html'
    )
