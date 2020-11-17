from django.contrib import admin
from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    
    path("lista_proyectos/", views.ListProyecto.as_view(), name="proyectos"),
    path("lista_personal/", views.ListPersonal.as_view(), name="Lpersonal"),
    path("lista_g_admin/", views.ListGastoAdministrativo.as_view(), name="gadmin"),
    path('list_electric_cost/',views.ListElectricCost.as_view(), name='listElectricCost'),
    path('list_gas_cost/',views.ListGasCost.as_view(), name='listGascost'),
    path('list_fertilizer_cost/',views.ListFertilizerCost.as_view(), name='listFertilizercost'),
    path('list_substrate_cost/',views.ListSubstrateCost.as_view(), name='listSubstratecost'),
    path('list_shipping_cost/',views.ListShippingCost.as_view(), name='listShippingCost'),
    path('list_seeds_cost/',views.ListSeedsCost.as_view(), name='listSeedsCost'),
    path('list_fuel_cost/',views.ListFuelCost.as_view(), name='listFuelCost'),
    path('list_cleaning_cost/',views.ListCleaningCost.as_view(), name='listCleaningCost'),
    path('list_various_cost/',views.ListVariousCost.as_view(), name='listVariousCost'),
    path('list_tax_rate/',views.ListTaxRate.as_view(), name='listTaxRate'),
    path('list_Macro_Ind/',views.ListMacroeconomicsIndicator.as_view(), name='listMacroind'),
    # path("pagina/<str:slug>", views.page, name="page"),
]