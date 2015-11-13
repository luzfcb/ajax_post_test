from braces.views import AjaxResponseMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .forms import Formulario
from .models import Document


class BaseDefault(object):
    template_name = 'base.html'
    model = Document


class DocumentList(BaseDefault, generic.ListView):
    template_name = 'document_list.html'


class DocumentUpdate(AjaxResponseMixin, BaseDefault, generic.UpdateView):
    template_name = 'document_form.html'
    form_class = Formulario
    success_url = reverse_lazy('document_list')

    def post_ajax(self, request, *args, **kwargs):
        print("eh ajax: post_ajax")
        super(DocumentUpdate, self).post_ajax(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            print("eh ajax")
        return super(DocumentUpdate, self).post(request, *args, **kwargs)
