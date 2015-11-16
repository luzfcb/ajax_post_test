from braces.views import AjaxResponseMixin, JsonRequestResponseMixin
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.views import generic
from .forms import Formulario
from .models import Document


class BaseDefault(object):
    template_name = 'base.html'
    model = Document


class DocumentList(BaseDefault, generic.ListView):
    template_name = 'document_list.html'


class DocumentUpdate(BaseDefault, generic.UpdateView):
    template_name = 'document_form.html'
    form_class = Formulario
    success_url = reverse_lazy('document_list')

    def form_valid(self, form):
        if self.request.is_ajax():
            form.save()
            obj = self.get_object()
            return JsonResponse(data={"pk": obj.pk, 'save_counter': obj.save_counter})
        return super(DocumentUpdate, self).form_valid(form)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(data={"pk": self.get_object().pk, 'invalido': 'invalido'})
        return super(DocumentUpdate, self).form_invalid(form)
