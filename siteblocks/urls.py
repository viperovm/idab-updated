from django.urls import path
from .views import RatingViewSet, HistoryViewSet, ContactViewSet, CategoryViewSet, ProgramViewSet, ManagmentViewSet, LeaderViewSet, TeacherViewSet, EventViewSet, ReviewViewSet, ReviewVideoViewSet, FaqViewSet, SectionViewSet, GalleryViewSet, AdmittanceDateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'programs', ProgramViewSet, basename='program')
router.register(r'managments', ManagmentViewSet, basename='managment')
router.register(r'leader', LeaderViewSet, basename='leader')
router.register(r'teachers', TeacherViewSet, basename='teacher')
router.register(r'events', EventViewSet, basename='event')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'reviewsvideos', ReviewVideoViewSet, basename='reviewvideo')
router.register(r'faqs', FaqViewSet, basename='faq')
router.register(r'history', HistoryViewSet, basename='history')
router.register(r'pages', SectionViewSet, basename='page')
router.register(r'galleries', GalleryViewSet, basename='gallery')
router.register(r'admittancedate', AdmittanceDateViewSet, basename='admittancedate')
router.register(r'rating', RatingViewSet, basename='rating')

urlpatterns = router.urls