from rest_framework.routers import DefaultRouter

from simulator.views.financial_trial import FinancialTrialViewSet


router = DefaultRouter()
router.register(r'fin_trial', FinancialTrialViewSet, basename='fin_trial')
urlpatterns = router.urls
