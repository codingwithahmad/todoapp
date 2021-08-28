from django.shortcuts import redirect

class FieldsMixin:
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			self.fields = ["title","time","desc","writer"]
		elif request.user.is_staff:
			self.fields = ["title","time","desc"]
		else:
			return redirect("todo:home")

		return super().dispatch(request, *args, **kwargs)


class FormValid:
	def form_valid(self, form):
		if self.request.user.is_superuser:
			form.save()
		else:
			self.obj = form.save(commit=False)
			self.obj.writer = self.request.user

		return super().form_valid(form)
