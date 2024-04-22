# from django.template.loader import get_template
# from django.http import HttpResponse
# from weasyprint import HTML, CSS
#
# from django.shortcuts import render
# from django.db.models import Q
#
from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
#
# from user.models import User
# from course.models import CourseModel
#
#
class CertificateViewSet(viewsets.ViewSet):
    pass
#     @action(detail=False, methods=['get'])
#     def my_page(self, request):
#         name = "My Name"
#
#         return render(request, 'index.html', {'name': name})
#
#     @action(detail=False, methods=['get'])
#     def generate_pdf(self, request):
#         user_id = request.query_params.get("user_id")
#         course_id = request.query_params.get("course_id")
#         try:
#             user = User.objects.get(id=user_id)
#             course = CourseModel.objects.get(id=course_id)
#         except Exception as e:
#             return Response({"message": "something didn't find"})
#
#         template = get_template('index.html')
#
#         html_content = template.render({'name': user.name, 'course': course.name})
#
#         html = HTML(string=html_content)
#         pdf_file = html.write_pdf(stylesheets=[CSS(string='@page { size: landscape; }')])
#
#         response = HttpResponse(pdf_file, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
#         return response
