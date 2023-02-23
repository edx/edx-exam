""" API v1 URLs. """

from django.urls import path, re_path

from edx_exams.apps.api.v1.views import (
    CourseExamAttemptView,
    CourseExamConfigurationsView,
    CourseExamsView,
    ExamAccessTicketsView,
    ExamAttemptView,
    ProctoringProvidersView
)
from edx_exams.apps.core.constants import CONTENT_ID_PATTERN, COURSE_ID_PATTERN, EXAM_ID_PATTERN

app_name = 'v1'

urlpatterns = [
    re_path(fr'exams/course_id/{COURSE_ID_PATTERN}',
            CourseExamsView.as_view(),
            name='exams-course_exams'),
    re_path(fr'configs/course_id/{COURSE_ID_PATTERN}',
            CourseExamConfigurationsView.as_view(),
            name='course-exam-config'),
    re_path(r"^providers?$",
            ProctoringProvidersView.as_view(),
            name="proctoring-providers-list",),
    re_path(fr'access_tokens/exam_id/{EXAM_ID_PATTERN}',
            ExamAccessTicketsView.as_view(),
            name="exam-access-tickets"),
    path('exams/attempt/<int:attempt_id>',
         ExamAttemptView.as_view(),
         name='exams-attempt',),
    path('exams/attempt',
         ExamAttemptView.as_view(),
         name='exams-attempt',),
    re_path(fr'exams/attempt/course_id/{COURSE_ID_PATTERN}/content_id/{CONTENT_ID_PATTERN}',
            CourseExamAttemptView.as_view(),
            name='exams-course_attempt')
]
