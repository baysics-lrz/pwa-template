import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import DeleteView
from observations.models import Category4, Category3, Category2, Category1


class DeleteCategory1(LoginRequiredMixin, DeleteView):
    model = Category1
    template_name = 'deletion-forms/category1_delete_form.html'
    success_url = '/observations/show-my-list/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Check if the user is allowed to delete the observation
        if self.object.user != request.user:
            return HttpResponse(status=403)
        Category1.objects.get(id=self.object.id).Photo.delete(save=True)
        success_url = self.get_success_url()
        # delete thumbnails
        model_obj = self.object
        all_fields = [field.name for field in Category1._meta.get_fields()]
        for f in all_fields:
            value = getattr(model_obj, f, None)
            if value is not None and f == 'Photo':
                print('key: ', f, " Value: ", value)
                new_fp = "media/thumbnails/" + str(value)[:-4] + "_small.jpg"
                try:
                    os.remove(new_fp)
                    print("thumbnail file Removed!")
                except:
                    print("error while removing thumbnail")
        self.object.delete()
        messages.success(self.request, 'Entry successfully deleted!')
        return redirect(success_url)


class DeleteCategory2(LoginRequiredMixin, DeleteView):
    model = Category2
    template_name = 'deletion-forms/category2_delete_form.html'
    success_url = '/observations/show-my-list/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Check if the user is allowed to delete the observation
        if self.object.user != request.user:
            return HttpResponse(status=403)
        Category2.objects.get(id=self.object.id).Photo.delete(save=True)
        success_url = self.get_success_url()
        # delete thumbnails
        model_obj = self.object
        all_fields = [field.name for field in Category2._meta.get_fields()]
        for f in all_fields:
            value = getattr(model_obj, f, None)
            if value is not None and f == 'Photo':
                print('key: ', f, " Value: ", value)
                new_fp = "media/thumbnails/" + str(value)[:-4] + "_small.jpg"
                try:
                    os.remove(new_fp)
                    print("thumbnail file Removed!")
                except:
                    print("error while removing thumbnail")
        self.object.delete()
        messages.success(self.request, 'Entry successfully deleted!')
        return redirect(success_url)



class DeleteCategory3(LoginRequiredMixin, DeleteView):
    model = Category3
    template_name = 'deletion-forms/category3_delete_form.html'
    success_url = '/observations/show-my-list/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Check if the user is allowed to delete the observation
        if self.object.user != request.user:
            return HttpResponse(status=403)
        Category3.objects.get(id=self.object.id).Photo.delete(save=True)
        success_url = self.get_success_url()
        # delete thumbnails
        model_obj = self.object
        all_fields = [field.name for field in Category3._meta.get_fields()]
        for f in all_fields:
            value = getattr(model_obj, f, None)
            if value is not None and f == 'Photo':
                print('key: ', f, " Value: ", value)
                new_fp = "media/thumbnails/" + str(value)[:-4] + "_small.jpg"
                try:
                    os.remove(new_fp)
                    print("thumbnail file Removed!")
                except:
                    print("error while removing thumbnail")
        self.object.delete()
        messages.success(self.request, 'Entry successfully deleted!')
        return redirect(success_url)


class DeleteCategory4(LoginRequiredMixin, DeleteView):
    model = Category4
    template_name = 'deletion-forms/category4_delete_form.html'
    success_url = '/observations/show-my-list/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Check if the user is allowed to delete the observation
        if self.object.user != request.user:
            return HttpResponse(status=403)
        Category4.objects.get(id=self.object.id).Photo.delete(save=True)
        success_url = self.get_success_url()
        # delete thumbnails
        model_obj = self.object
        all_fields = [field.name for field in Category4._meta.get_fields()]
        for f in all_fields:
            value = getattr(model_obj, f, None)
            if value is not None and f == 'Photo':
                print('key: ', f, " Value: ", value)
                new_fp = "media/thumbnails/" + str(value)[:-4] + "_small.jpg"
                try:
                    os.remove(new_fp)
                    print("thumbnail file Removed!")
                except:
                    print("error while removing thumbnail")
        self.object.delete()
        messages.success(self.request, 'Entry successfully deleted!')
        return redirect(success_url)
